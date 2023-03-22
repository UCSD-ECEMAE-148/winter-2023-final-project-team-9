import time
from pyvesc import VESC

# Set up communication with the VESC
vesc = VESC('/dev/ttyACM0', 115200)

vesc.set_servo(0.8)

time.sleep(1)

vesc.set_rpm(4000)

time.sleep(4)

vesc.set_rpm(0)

time.sleep(1)

vesc.set_servo(0.5)
