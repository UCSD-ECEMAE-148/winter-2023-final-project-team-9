#Referenced Donkey car source code and github code 
import serial
import binascii
from LidarCalc import CalcLidarData
import matplotlib.pyplot as plt
import math

#Initialize graph
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection='polar')
ax.set_title('lidar',fontsize=12)

#Read from port 
ser = serial.Serial(port='/dev/tty.usbserial-0001',
                    baudrate=230400,
                    timeout=5.0,
                    bytesize=8,
                    parity='N',
                    stopbits=1)

tmpString = ""
lines = list()
angles = list()
distances = list()


#cycle 40 times as it can cover all segment in from LiDAR
i = 0
while True:
    loopFlag = True
    flag2c = False

    #reset every 40 cucle
    if(i % 40 == 39):
        if('line' in locals()):
            line.remove()
        line = ax.scatter(angles, distances, c="pink", s=5)

        ax.set_theta_offset(math.pi / 2)
        plt.pause(0.01)
        angles.clear()
        distances.clear()
        i = 0
        
    #Start loop 
    while loopFlag:
        b = ser.read()
        tmpInt = int.from_bytes(b, 'big')
        
        #If byte is 54(starting byte)
        if (tmpInt == 0x54):
            tmpString +=  b.hex()+" "
            flag2c = True
            continue
        
        #If byte is 2c(length byte)
        elif(tmpInt == 0x2c and flag2c):
            tmpString += b.hex()
            #check every full byte
            if(not len(tmpString[0:-5].replace(' ','')) == 90 ):
                tmpString = ""
                loopFlag = False
                flag2c = False
                continue

            lidarData = CalcLidarData(tmpString[0:-5])
            angles.extend(lidarData.Angle_i)
            distances.extend(lidarData.Distance_i)
                
            tmpString = ""
            loopFlag = False
        #Read byte
        else:
            tmpString += b.hex()+" "
        
        flag2c = False
    
    i += 1