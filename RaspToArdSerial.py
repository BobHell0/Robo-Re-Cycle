import serial
import sys
import time
def openSerial():
    #print("Hello world")
    ser = serial.Serial('COM4', 115200, timeout = 5)
    return ser
def readCmdResponse(ser):
    response = ser.readlines()
    return response
    
def printCmdResponse(lineData):
	for lines in lineData:
		print(lines.decode('utf-8').strip())
    
def status(ser):
    ser.write(b'status\n')
    response = readCmdResponse()
    printCmdResponse(response)
    #print("This is the last line of the response to status" + response[-1].decode('utf-8').strip())
    
def setMotor(ser, param1, param2):
    cmdStr = "setMotor " + str(param1) + ", " + str(param2)
    byteCmdStr = cmdStr.encode('utf-8')
    ser.write(byteCmdStr)
    printCmdResponse(readCmdResponse())
    time.sleep(1.5)
    #print(sum(ser))
    
def reset(ser):
	ser.write(b'reset\n')
	printCmdResponse(readCmdResponse())
	time.sleep(1.5)
def manualOn(ser):
    ser.write(b'manual on\n')
    printCmdResponse(readCmdResponse())
    time.sleep(1.5)
def manualOff(ser):
	ser.write(b'manual off\n')
	response = readCmdResponse()
	print(response.length())
	printCmdResponse(response)
	time.sleep(1.5)
    
def readBoot():
    print("waiting for start up\n")
    time.sleep(5)
    print("ready\n")
    status()
    printCmdResponse(readCmdResponse())
    print("End of Boot Up\n")
def rotate(ser, param1, param2):
    cmdStr = "rotate " + str(param1) + ", " + str(param2)
    byteCmdStr = cmdStr.encode('utf-8')
    ser.write(byteCmdStr)
    printCmdResponse(readCmdResponse())
    time.sleep(1.5)
def close(ser):
    ser.close
    return
"""
openSerial()
readBoot()
rotate(330, 1)
setMotor(1, 120)
setMotor(3, 160)
setMotor(1, 180)
setMotor(3, 120)
#suction on
setMotor(3, 160)
setMotor(1, 140)
rotate(380, -1)
#drop plate
rotate(100, 1)
reset()
rotate(50, -1)
print("Closing Connection")
close(ser)
"""