
<a name="readme-top"></a>


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="img/logo.png" alt="Logo" width=50% height=50%>
  </a>

  <h3 align="center">ECE/MAE 148 Winter 2023 Team 9</h3>
    
  <p align="center">
    JetBuddy<br>
    Indoor Delivery Bot based on DepthAI, OpenCV and LiDAR<br>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary><b>Table of Contents</b></summary>
    <li><a href="#team-members">Team Members</a></li>
    <li>
      <a href="#hardware">Hardware and Schematics</a>
      <ul>
        <li><a href="#parts">Parts</a></li>
        <li><a href="#schematics"> Schematics</a></li>
      </ul>
    </li>
    <li><a href="#final-project">Final Project</a></li>
     <ul>
        <li><a href="#abstract">Abstract</a></li>
        <li><a href="#part-1-human-detection-and-following-with-depthai-and-pyvesc">Part 1: Human Detection and Following with Depthai and PyVesc</a></li>
        <li><a href="#part-2-stopping-mechanism-with-lidar"> Part 2: Stopping Mechanism with Lidar</a></li>
        <li><a href="#part-3-facial-recognition"> Part 3: Facial Recognition</a></li>
        <li><a href = "#Part-4-Spatial-Detection-with-DepthAI"> Part 4: Spatial Detection with DepthAI</a></li>
      </ul>
     <li><a href="#reflection">Reflection</a></li>
     <ul>
        <li><a href="#challenges">Challenges</a></li>
        <li><a href="#potential-improvements"> Potential Improvements</a></li>
      </ul>
    <li><a href="#presentations">Presentation Files</a></li>
    <li><a href="#reference">Reference</a></li>

</details>
<!-- ABOUT THE TEAM -->

## Team members

* Ben Zhang (ECE)
* Joseph Katona (ECE) 
* Yichen Yang (ECE)
* Zijian Wang (MAE)

<img src="img/Team.png" alt="The Team" width=40% height=40%>

<!-- ABOUT THE PROJECT HARDWARE -->
## Hardware

### Parts

#### Full Assembly

<img src="img/Robot.png" alt="The robot" width=30% height=30%>


#### Mounting Plate
<img src="img/board2.png" alt="Mounting Board" width=30% height=30%>


#### Jetson Case
<img src="img/bot.png" alt="Case Top" width=30% height=30%>
<img src="img/bottom.png" alt="Case Bottom" width=30% height=30%>

#### Camera LiDAR Mount

<img src="img/caml.png" alt="The Camera and LiDAR mount" width=30% height=30%>

#### Final Project Delivery Box

<img src="img/box.png" alt="The box" width=30% height=30%>

### Schematics

### Wire Diagram

<img src="img/wire.png" alt="The Wire diagram" width=50% height=50%>

<!-- Final Project -->
## Final Project

### Abstract<a name="abstract"></a>
This project aims to develop a delivery system for our robocar that can detect and follow humans while also incorporating a stopping mechanism to prevent collisions. Additionally, the robot will utilize facial recognition to identify individuals and personalize interactions.

### Part 1: Human Detection and Following with Depthai and PyVesc
The OAKD camera will be used to detect and track humans in the robot's vicinity. The PyVesc motor controllers will then be used to move the robot in the direction of the detected human.

#### Required Components
* Tiny-Yolov3 model integrated in DepthAi for object detection
* PyVesc Python package for robocar control

#### Algorithm Workflow
* Use Tiny-Yolov3 to detect the bounding box of the person in the OAKD camera's field of view.
* Determine the position of the person by finding the central line of the bounding box, and denote the x-axis value as x0.
* Calculate the error between the central line of the frame (416x416 pixels), e = x - x0.
* Calculate the steering value using the formula: v = (Kp * e) / 416 + 0.5, where Kp = 1.
* Use PyVesc to control steering by calling vesc.set_servo(v).

#### Additional Settings
* Use vesc.set_rpm() to run the car once it detects people.
* The steering value is sampled at a rate of 5Hz to prevent frequent drifting.

<img src="img/obj.png" alt="The object recognization and following" width=40% height=40%>

### Part 2: Stopping Mechanism with Lidar

The Lidar sensor will be used to detect obstacles in the robot's path. If an obstacle is detected, the robot will stop moving and wait for the obstacle to clear before continuing on its path.

#### The LiDAR on this robot aim to

* Detect anything that is in a close range
* If the position is too clase, the robot will stop to avoid collision
* The robot will back up after it stop for a while and still detect obstacle is close
* Transform raw binary data from LiDAR to numerical data through BinASCII library

#### How to read LiDAR?

* Each measurement data point of LiDAR is consists of a distance value of 2 bytes and a confidence of 1 byte
* We transform this data through chopping it to bytes and translate it.
* We get the angle by getting the start angle and end angle.

* Putting all the distance into a list and it will stop the car if there’s an object within certain distance that LiDAR detected.

<img src="img/lidar.png" alt="The Reading From LiDAR and how bytes work" width=60% height=60%>


### Part 3: Facial Recognition

The robot will be equipped with a facial recognition system, using a webcam, that will allow it to identify individuals and personalize interactions. Once it recognizes the right person, the delivery box will open. The facial recognition software uses a simple python import of facial_recognition. In the facial_recognition library all we do is use openCV to capture images for the frames and use facial_recognitions "matching" function to to add a box around the persons face. In our case when this value is detected over an interval then a true value is then sent to the box to open.

<img src="img/face.png" alt="Facial Recognization" width=40% height=40%>


### Part 4: Spatial Detection with DepthAI

Utilizing Depthai's pipeline system we take their spatial location pipeline to simply calculate the distance of individual from the camera. The
Object detection pipeline detects a person and creates a bounded box, then with the x and y coordinates from the bounded box we can pinpoint where we want the camera to point. After these coordinates are gathered the z location is stored in a circular list. This is because the bounded box and tracker of object distance aren't always in sync so some erroneous values are given. Once we have around 50 samples then we take the average to get a good idea of what the distance of the person from the car is. Finally we utilize pyvescs set_rpm() features to give out a more smooth acceleration system. So, basically if you're far away the robot will speed up and slow down as it moves closer to you.
<br></br>
<a href = "https://homepages.inf.ed.ac.uk/rbf/CVonline/LOCAL_COPIES/OWENS/LECT9/node2.html">Get more info on Spatial Depth here</a>
<img src = "/img/SpatialDepth.png" alt = "Spatial Depth" width = 50% height = 50%>
## Gantt Chart

<img src="img/gantt.png" alt="The Gantt Chart" width=80% height=80%>

## Demonstrations

The Video might not show up, please go to img folder for full demo.

![demo1](img/demo1.gif)
![demo2](img/demo2.mov)
![demo3](img/demo3.mp4)

<video width=80% controls>
  <source src="img/demo1.gif" type="video/gif">
  <source src="img/demo2.MOV" type="video/mov">
  <source src="img/demo3.mp4" type="video/mp4">
  Your browser does not support HTML video.
</video>


## Reflection

### Challenges

* Getting everything to work together
    - Different libraries working together and all send signals to PyVESC
    - Everything worked fine on a local machine but when running on the Jetson, crashes would occur
* Scope of the original idea
    - Mapping the path for future references using SLAM
* Depth ai pipeline caused crashes
    - X-Link Problem(Serial bus issues)
* Translate raw LiDAR output to data we need
* Making the car look smooth
* Better algorithm to adjust speed(rpm)

### Potential Improvements

* Implement all the features together flawlessly
    - Currently cannot run together good due to delay from different components
* Get the locking mechanism working
    - Locking mechanism to make sure the right receiver get the package
* LiDar also scans the path for future path planning
    - Trying to find a person if it cannot detect anything

Maybe try different frameworks since we can use different libraries without limitation in ROS or donkeycar



## Presentations

 <li><a href="https://docs.google.com/presentation/d/1vZR8SQN1TiYbnnbAlBYmKsXzOSSQFPH9sE0spc0SiLc/edit?usp=sharing">Project Proposal & Progress Report</a></li>
  <li><a href="https://docs.google.com/presentation/d/1nHktegokEYfigWinu62BJ4joUQMxiHzlaY9nhIGGi0c/edit?usp=sharing">Final Presntation</a></li>

## Reference

We would like to give special thanks to:

* Professor Jack Silberman
* TA Moises Lopez
* TA Kishore Nukala
* All The teams that helped us on the way
