#!/usr/bin/env python3

"""
The code is the same as for Tiny Yolo V3 and V4, the only difference is the blob file
- Tiny YOLOv3: https://github.com/david8862/keras-YOLOv3-model-set
- Tiny YOLOv4: https://github.com/TNTWEN/OpenVINO-YOLOV4
"""

from pathlib import Path
import sys
import cv2
import depthai as dai
import numpy as np
import time
from calc import HostSpatialsCalc
from utility import *
import math
import collections
# from pyvesc import VESC

# Set up VESC
# vesc = VESC("/dev/ttyACM0", 115200)

# Get argument first
nnPath = str((Path(__file__).parent / Path('../depthai-python/examples/models/yolo-v4-tiny-tf_openvino_2021.4_6shave.blob')).resolve().absolute())
if 1 < len(sys.argv):
    arg = sys.argv[1]
    if arg == "yolo3":
        nnPath = str((Path(__file__).parent / Path('../depthai-python/examples/models/yolo-v3-tiny-tf_openvino_2021.4_6shave.blob')).resolve().absolute())
    elif arg == "yolo4":
        nnPath = str((Path(__file__).parent / Path('../depthai-python/examples/models/yolo-v4-tiny-tf_openvino_2021.4_6shave.blob')).resolve().absolute())
    else:
        nnPath = arg
else:
    print("Using Tiny YoloV4 model. If you wish to use Tiny YOLOv3, call 'tiny_yolo.py yolo3'")

if not Path(nnPath).exists():
    import sys
    raise FileNotFoundError(f'Required file/s not found, please run "{sys.executable} install_requirements.py"')

# tiny yolo v4 label texts
labelMap = [
    "person",         "bicycle",    "car",           "motorbike",     "aeroplane",   "bus",           "train",
    "truck",          "boat",       "traffic light", "fire hydrant",  "stop sign",   "parking meter", "bench",
    "bird",           "cat",        "dog",           "horse",         "sheep",       "cow",           "elephant",
    "bear",           "zebra",      "giraffe",       "backpack",      "umbrella",    "handbag",       "tie",
    "suitcase",       "frisbee",    "skis",          "snowboard",     "sports ball", "kite",          "baseball bat",
    "baseball glove", "skateboard", "surfboard",     "tennis racket", "bottle",      "wine glass",    "cup",
    "fork",           "knife",      "spoon",         "bowl",          "banana",      "apple",         "sandwich",
    "orange",         "broccoli",   "carrot",        "hot dog",       "pizza",       "donut",         "cake",
    "chair",          "sofa",       "pottedplant",   "bed",           "diningtable", "toilet",        "tvmonitor",
    "laptop",         "mouse",      "remote",        "keyboard",      "cell phone",  "microwave",     "oven",
    "toaster",        "sink",       "refrigerator",  "book",          "clock",       "vase",          "scissors",
    "teddy bear",     "hair drier", "toothbrush"
]

syncNN = True

# Create pipeline
pipeline = dai.Pipeline()

# Define sources and outputs
camRgb = pipeline.create(dai.node.ColorCamera)
detectionNetwork = pipeline.create(dai.node.YoloDetectionNetwork)
xoutRgb = pipeline.create(dai.node.XLinkOut)
nnOut = pipeline.create(dai.node.XLinkOut)
monoLeft = pipeline.create(dai.node.MonoCamera)
monoRight = pipeline.create(dai.node.MonoCamera)
stereo = pipeline.create(dai.node.StereoDepth)

xoutRgb.setStreamName("rgb")
nnOut.setStreamName("nn")

# Properties
camRgb.setPreviewSize(416, 416)
camRgb.setResolution(dai.ColorCameraProperties.SensorResolution.THE_1080_P)
camRgb.setInterleaved(False)
camRgb.setColorOrder(dai.ColorCameraProperties.ColorOrder.BGR)
camRgb.setFps(40)
monoLeft.setResolution(dai.MonoCameraProperties.SensorResolution.THE_400_P)
monoLeft.setBoardSocket(dai.CameraBoardSocket.LEFT)
monoRight.setResolution(dai.MonoCameraProperties.SensorResolution.THE_400_P)
monoRight.setBoardSocket(dai.CameraBoardSocket.RIGHT)

stereo.initialConfig.setConfidenceThreshold(255)
stereo.setLeftRightCheck(True)
stereo.setSubpixel(False)

# Network specific settings
detectionNetwork.setConfidenceThreshold(0.5)
detectionNetwork.setNumClasses(80)
detectionNetwork.setCoordinateSize(4)
detectionNetwork.setAnchors([10, 14, 23, 27, 37, 58, 81, 82, 135, 169, 344, 319])
detectionNetwork.setAnchorMasks({"side26": [1, 2, 3], "side13": [3, 4, 5]})
detectionNetwork.setIouThreshold(0.5)
detectionNetwork.setBlobPath(nnPath)
detectionNetwork.setNumInferenceThreads(2)
detectionNetwork.input.setBlocking(False)

# Linking
camRgb.preview.link(detectionNetwork.input)
if syncNN:
    detectionNetwork.passthrough.link(xoutRgb.input)
else:
    camRgb.preview.link(xoutRgb.input)

detectionNetwork.out.link(nnOut.input)

monoLeft.out.link(stereo.left)
monoRight.out.link(stereo.right)

xoutDepth = pipeline.create(dai.node.XLinkOut)
xoutDepth.setStreamName("depth")
stereo.depth.link(xoutDepth.input)

xoutDepth = pipeline.create(dai.node.XLinkOut)
xoutDepth.setStreamName("disp")
stereo.disparity.link(xoutDepth.input)

# Connect to device and start pipeline
with dai.Device(pipeline) as device:
    d = collections.deque(maxlen=50)
    # Output queues will be used to get the rgb frames and nn data from the outputs defined above
    qRgb = device.getOutputQueue(name="rgb", maxSize=4, blocking=False)
    qDet = device.getOutputQueue(name="nn", maxSize=4, blocking=False)
    depthQueue = device.getOutputQueue(name="depth")
    dispQ = device.getOutputQueue(name="disp")

    
    frame = None
    detections = []
    startTime = time.monotonic()
    counter = 0
    color2 = (255, 255, 255)
    
    text = TextHelper()
    hostSpatials = HostSpatialsCalc(device)
    y = 200
    x = 300
    step = 3
    delta = 5
    hostSpatials.setDeltaRoi(delta)
    # hostSpatials.setDeltaRoi(delta)
    i = 0
    print("Use WASD keys to move ROI.\nUse 'r' and 'f' to change ROI size.")
    # nn data, being the bounding box locations, are in <0..1> range - they need to be normalized with frame width/height
    def frameNorm(frame, bbox):
        normVals = np.full(len(bbox), frame.shape[0])
        normVals[::2] = frame.shape[1]
        return (np.clip(np.array(bbox), 0, 1) * normVals).astype(int)

    def displayFrame(name, frame):
        color = (255, 0, 0)
        for detection in detections:
            bbox = frameNorm(frame, (detection.xmin, detection.ymin, detection.xmax, detection.ymax))
            cv2.putText(frame, labelMap[detection.label], (bbox[0] + 10, bbox[1] + 20), cv2.FONT_HERSHEY_TRIPLEX, 0.5, 255)
            cv2.putText(frame, f"{int(detection.confidence * 100)}%", (bbox[0] + 10, bbox[1] + 40), cv2.FONT_HERSHEY_TRIPLEX, 0.5, 255)
            cv2.rectangle(frame, (bbox[0], bbox[1]), (bbox[2], bbox[3]), color, 2)
        # Show the frame
        cv2.imshow(name, frame)

    start_time = time.time()
    while True:
        if syncNN:
            inRgb = qRgb.get()
            inDet = qDet.get()
        else:
            inRgb = qRgb.tryGet()
            inDet = qDet.tryGet()

        if inRgb is not None:
            frame = inRgb.getCvFrame()
            cv2.putText(frame, "NN fps: {:.2f}".format(counter / (time.monotonic() - startTime)),
                        (2, frame.shape[0] - 4), cv2.FONT_HERSHEY_TRIPLEX, 0.4, color2)

        if inDet is not None:
            detections = inDet.detections
            counter += 1

        if frame is not None:
            displayFrame("rgb", frame)

        bbox = None
        if detections is not None:
            is_found = False
            for detection in detections:
                if labelMap[detection.label] == 'person':
                    bbox = frameNorm(frame, (detection.xmin, detection.ymin, detection.xmax, detection.ymax))
                    line = cv2.line(frame, (int((bbox[2] + bbox[0]) / 2), bbox[1]), (int((bbox[2] + bbox[0]) / 2), bbox[3]),
                             (0, 0, 255), 2)
                    
                    x = int((bbox[0] + bbox[2])/2)
                    y = int(((bbox[1] + bbox[3])/2))
                    cv2.imshow('rgb', line)
                    is_found = True
                    break
            if is_found:
                i = 0
                # vesc.set_rpm(rpm)
            else:
                bbox = None
                # vesc.set_rpm(0)
                
        else:
            # vesc.set_rpm(0)
            bbox = None

        

        if cv2.waitKey(1) == ord('q'):
            break
        
        
        depthData = depthQueue.get()
        
        # Calculate spatial coordiantes from depth frame
        spatials, centroid = hostSpatials.calc_spatials(depthData, (x + 50,y)) # centroid == x/y in our case

        # Get disparity frame for nicer depth visualization
        disp = dispQ.get().getFrame()
        disp = (disp * (255 / stereo.initialConfig.getMaxDisparity())).astype(np.uint8)
        disp = cv2.applyColorMap(disp, cv2.COLORMAP_JET)
        print("bottom", x,y)
        text.rectangle(disp, (x, y), (x, y))
        text.putText(disp, "X: " + ("{:.1f}m".format(spatials['x']/1000) if not math.isnan(spatials['x']) else "--"), (x + 10, y + 20))
        text.putText(disp, "Y: " + ("{:.1f}m".format(spatials['y']/1000) if not math.isnan(spatials['y']) else "--"), (x + 10, y + 35))
        text.putText(disp, "Z: " + ("{:.1f}m".format(spatials['z']/1000) if not math.isnan(spatials['z']) else "--"), (x + 10, y + 50))

        # Show the frame
        cv2.imshow("depth", disp)
        i += 1
        print(i)
        if (i < 50):
            try:
                z = spatials['z']/1000
            except ValueError:
                continue
            d.append(z)
            z = np.average(d)
            if (z < 1):
                vesc.set_rpm(200)
            if (z > 1 and z < 2):
                vesc.set_rpm(300)
            if (z > 2 and z < 3):
                vesc.set_rpm(700)
            if (z > 3 and z < 5):
                vesc.set_rpm(1000)
            if (z > 5):
                vesc.set_rpm(2000)
            if time.time() - start_time > 0.5:
                pid_p = 1
                center_frame = 208
                center_person = x
                error = round((center_person - center_frame) / 416 + 0.5, 2)
                # vesc.set_servo(error * pid_p)
                print("moving:", error)
                start_time = time.time()
            