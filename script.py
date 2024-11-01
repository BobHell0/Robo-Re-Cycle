import subprocess
import os
import time
import serial
import RaspToArdSerial as rta
#include 

"""
1. Change folder (os.chdir(""))
2. Run program (subprocess.run(["", ""]))
3. Return folder (os.chdir("../"))
"""

#----------------START OF THE SCRIPT------------------#
# Clamp ON
# Put code here.

print("Turning on clamp...")

clampOnFlag = False

while clampOnFlag is False:
    key = input("Is clamp engaged? (y/n)")
    if key == 'y':
        clampOnFlag = True


no_screws = False
ret_val = False # change this to check screw, Anujan program should output
while no_screws is False:
 
    # CNC move table
    os.chdir("./GCodeGenerator")
    subprocess.run(["./program", "move-table"])
    os.chdir("../")
    print("Moving table...")
    moveTableFlag = False
    while moveTableFlag is False:
        key = input("Has table moved? (y/n)")
        if key == 'y':
            moveTableFlag = True
    
 
    # send file to Roland PC
     
    # Computer Vision Detect Screws
    # Put code here.
    # Check for return values (ret_val)
    print("Detecting screws...")
    screwDetectFlag = False
    while screwDetectFlag is False:
        key = input("Screws detected? (y/n)")
        if key == 'y':
            screwDetectFlag = True
     
    if (ret_val):
        no_screws = True
        print("No screws detected!")
    else:
        # CNC drill screws
        print("Screws detected. Drilling screws...")
        os.chdir("./GCodeGenerator")
        subprocess.run(["./program", "drill-screws"])
        os.chdir("../")
        ret_val = True
        print("Detecting screws...")
        drillFlag = False
        while drillFlag is False:
            key = input("Finish drilling? (y/n)")
            if key == 'y':
                drillFlag = True

# Grip ON
print("Turning on gripper...")
# Gripper sequence
""" Jack
ser = rta.openSerial()
rta.readBoot()
rta.rotate(ser, 330, 1)
rta.setMotor(ser, 1, 120)
rta.setMotor(ser, 3, 160)
rta.setMotor(ser, 1, 180)
rta.setMotor(ser, 3, 120)

#suction on
rta.setMotor(ser, 3, 160)
rta.setMotor(ser, 1, 140)
rta.rotate(ser, 380, -1)

#drop plate
rta.rotate(ser, 100, 1)
rta.reset(ser)
rta.rotate(ser, 50, -1)

print("Closing Connection")
rta.close(ser)
"""
# Check if gripper finished its sequence
gripFlag = False
while gripFlag is False:
    key = input("Gripped lid away? (y/n)")
    if key == 'y':
        gripFlag = True

# Clamp OFF
# Put code here.
print("Turning off clamp...")
clampOffFlag = False
while clampOffFlag is False:
    key = input("Is clamp disengaged? (y/n)")
    if key == 'y':
        clampOffFlag = True


print("Top plate disassembly complete!")
