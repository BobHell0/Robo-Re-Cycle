import serial
import sys
import time

ser = serial.Serial('/dev/ttyUSB0', 115200, timeout = 5)

def readCmdResponse():
    response = ser.readlines()
    return response
    
def printCmdResponse(lineData):
	for lines in lineData:
		print(lines.decode('utf-8').strip())
    
def status():
    ser.write(b'status\n')
    response = readCmdResponse()
    printCmdResponse(response)
    #print("This is the last line of the response to status" + response[-1].decode('utf-8').strip())
    
def setMotor(param1, param2):
    cmdStr = "setMotor " + str(param1) + ", " + str(param2)
    byteCmdStr = cmdStr.encode('utf-8')
    ser.write(byteCmdStr)
    printCmdResponse(readCmdResponse())
    time.sleep(1.5)
    
def reset():
	ser.write(b'reset\n')
	printCmdResponse(readCmdResponse())
	time.sleep(1.5)

def manualOn():
    ser.write(b'manual on\n')
    printCmdResponse(readCmdResponse())
    time.sleep(1.5)

def manualOff():
	ser.write(b'manual off\n')
	response = readCmdResponse()
	print(response.length())
	printCmdResponse(response)
	time.sleep(1.5)
    
def readBoot():
    print("waiting for start up\n")
    time.sleep(3)
    print("ready\n")
    status()
    printCmdResponse(readCmdResponse())

    print("End of Boot Up\n")

readBoot()

setMotor(3, 180)
setMotor(1, 120)
reset()

print("Closing Connection")
ser.close()
