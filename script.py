import subprocess
import os
import time

"""
1. Change folder (os.chdir(""))
2. Run program (subprocess.run(["", ""]))
3. Return folder (os.chdir("../"))
"""

# Clamp ON
#os.chdir("./foldername")
#subprocess.run(["./program", ""])
#os.chdir("../")
print("Turning on clamp...")

clampOnFlag = False
print("Is clamp on? (y/n)")
while clampOnFlag is False:
	val = input()
	if val == "y":
		clampOnFlag = True;

no_screws = False
ret_val = False
while no_screws is False:
	
	# CNC move table
	os.chdir("./GCodeGen")
	subprocess.run(["./program", "move-table"])
	os.chdir("../")
	print("Moving table...")
	
	moveTableFlag = False
	print("Moved table? (y/n)")
	while moveTableFlag is False:
		val = input()
		if val == "y":
			moveTableFlag = True;
	
	# send file to Roland PC
	
	# Turn cam on (rpicam)
	print("Taking pictures...")
	subprocess.run(["rpicam-still", "--roi", "0.325,0.325,0.35,0.35", 
					"--output", "img.jpg"])
					
	# Detect screws
	print("Detecting screws...")
	subprocess.run(["./computerVision/computerVision/bin/python3", 
					"./computerVision/computerVision/predictStillImages.py"])
	
	anyScrewsFlag = False
	while anyScrewsFlag is False:
		print("Are there any screws left? (y/n)")
		val = input()
		if val == "n":
			ret_val = True
			anyScrewsFlag = True
		elif val == "y":
			anyScrewsFlag = True
	
	if (ret_val):
		no_screws = True
		print("No screws detected!")
	else:
		# CNC drill screws
		print("Screws detected. Drilling screws...")
		os.chdir("./GCodeGen")
		subprocess.run(["./program", "drill-screws"])
		time.sleep(1)
		os.chdir("../")
		#ret_val = True # need to change this logic soon
		
		drillScrewsFlag = False
		print("Drill screws? (y/n)")
		while drillScrewsFlag is False:
			val = input()
			if val == "y":
				drillScrewsFlag = True;
	
	# how to detect when drilling completes? 
	# Wait for several minutes? Wait for manual input?

# Grip ON
#os.chdir("./grippies")
#subprocess.run(["./program", ""])
#os.chdir("../")
print("Turning on gripper...")

gripperFlag = False
print("Gripper? (y/n)")
while gripperFlag is False:
	val = input()
	if val == "y":
		gripperFlag = True;

# wait for grip to finish
#time.sleep(3)

# Clamp OFF
#os.chdir("./clamppies")
#subprocess.run(["./program", ""])
#os.chdir("../")
print("Turning off clamp...")

clampOffFlag = False
print("Clamper off? (y/n)")
while clampOffFlag is False:
	val = input()
	if val == "y":
		clampOffFlag = True;
		
print("Top plate disassembly complete!")
