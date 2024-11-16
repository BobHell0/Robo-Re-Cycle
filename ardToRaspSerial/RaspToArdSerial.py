import serial
import sys
import time

#ser = serial.Serial('COM4', 115200, timeout = 5)
ser = serial.Serial('/dev/ttyUSB0', 115200, timeout = 5)

def readCmdResponse():
    response = ser.readlines()
    return response
    
def printCmdResponse(lineData):
	for lines in lineData:
		print(lines.decode('utf-8').strip())
		
def invalidCheck(byteCmdStr):
	time.sleep(2)
	serResponse = readCmdResponse()
	for lines in serResponse:
		temp = lines.decode('utf-8').strip()
		if "invalid" in temp:
			print('invalid command recieved, resending byteCmdStr')
			time.sleep(0.5)
			ser.write(byteCmdStr)
			serResponse = readCmdResponse()
	printCmdResponse(serResponse)
    
def status():
    ser.write(b'status\n')
    response = readCmdResponse()
    printCmdResponse(response)
    #print("This is the last line of the response to status" + response[-1].decode('utf-8').strip())
	
def setMotor(param1, param2):
    cmdStr = "setMotor " + str(param1) + ", " + str(param2)
    byteCmdStr = cmdStr.encode('utf-8')
    ser.write(byteCmdStr)
    invalidCheck(byteCmdStr)

    
def reset():
	ser.write(b'reset\n')
	serResponse = readCmdResponse()
	invalidCheck(b'reset\n')
	time.sleep(2.5)
    
def readBoot():
    print("waiting for start up\n")
    time.sleep(5)
    print("ready\n")
    status()
    printCmdResponse(readCmdResponse())

    print("End of Boot Up\n")

def rotate(param1, param2):
    cmdStr = "rotate " + str(param1) + ", " + str(param2)
    byteCmdStr = cmdStr.encode('utf-8')
    ser.write(byteCmdStr)
    invalidCheck(byteCmdStr)
    time.sleep(2.5)
    
def clampOn():
	cmdStr = "clamp on"
	byteCmdStr = cmdStr.encode('utf-8')
	ser.write(byteCmdStr)
	invalidCheck(byteCmdStr)
	time.sleep(2.5)
    
def clampOff():
	cmdStr = "clamp off"
	byteCmdStr = cmdStr.encode('utf-8')
	ser.write(byteCmdStr)
	invalidCheck(byteCmdStr)
	time.sleep(2.5)

def suckerOn():
	cmdStr = "sucker on"
	byteCmdStr = cmdStr.encode('utf-8')
	ser.write(byteCmdStr)
	invalidCheck(byteCmdStr)
	time.sleep(2.5)

def suckerOff():
	cmdStr = "sucker off"
	byteCmdStr = cmdStr.encode('utf-8')
	ser.write(byteCmdStr)
	invalidCheck(byteCmdStr)
	time.sleep(2.5)

readBoot()

rotate(330, 1)

setMotor(1, 120)

setMotor(3, 160)

setMotor(1, 180)

setMotor(3, 110)

#suction on
suckerOn();

setMotor(3, 160)

setMotor(1, 140)

rotate(380, -1)

#drop plate
suckerOff();

rotate(100, 1)

reset()

rotate(50, -1)

print("Closing Connection")
ser.close()
