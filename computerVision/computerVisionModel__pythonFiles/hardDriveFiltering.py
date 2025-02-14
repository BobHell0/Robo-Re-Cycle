# Import libraries
import cv2
import numpy as np
import random
import math
from matplotlib import pyplot as plt

def getPixelToMMRatio(f: str):
	im = cv2.imread(f)
	hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
	hsv = cv2.blur(hsv, (5,5))

	imCopy = im.copy()
	# make middle white
	imCopy[0:,500:4200] = [255,255,255]
	# make outside regions black
	imCopy[0:,0:500] = [0,0,0]
	imCopy[0:,4200:] = [0,0,0]

	imCopy2 = im.copy()

	imCopy = cv2.cvtColor(imCopy, cv2.COLOR_BGR2GRAY)
	_, imCopy = cv2.threshold(imCopy, 254, 255, cv2.THRESH_BINARY)



	im = cv2.bitwise_and(im, im, mask=imCopy)
	# cv2.imshow('filtering wood', im)
	# cv2.waitKey(0)


	# filtering the pink 

	lower = np.array([130, 0, 0], np.uint8)
	upper = np.array([200, 255, 255], np.uint8)

	mask2 = cv2.inRange(hsv, lower, upper)

	# filtering the brown 
	lower = np.array([20, 0, 0])
	upper = np.array([120, 255, 255])

	mask = cv2.inRange(hsv, lower, upper)

	overallMask = cv2.bitwise_or(mask, mask2)

	

	# flipping the mask so that the green is black and the hard drive is white
	# mask = cv2.bitwise_not(mask)
	im = cv2.bitwise_and(im, im, mask=mask)

	cv2.imshow('adding inverted pink filter mask', im)
	cv2.waitKey(0)

	# threshold to make a
	im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

	# cv2.imshow('greyed out', im)
	# cv2.waitKey(0)
	ret, im = cv2.threshold(im, 15 , 255, cv2.THRESH_BINARY)
	im = cv2.erode(im, np.ones((2,2), np.uint8), iterations=15)
	im = cv2.dilate(im, np.ones((1,1), np.uint8), iterations=15)
	ret, im = cv2.threshold(im, 1, 255, cv2.THRESH_BINARY)

	cv2.imshow('threshold image', im)
	cv2.waitKey(0)

	contours, hierarchy = cv2.findContours(im, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	

	# if you want to see all significant contours, uncomment the below code:

	filtered = []
	# Looping over all found contours
	for c in contours:
		#If it has significant area, add to list
		if cv2.contourArea(c) < 1000: continue
		filtered.append(c)
		
	objects = np.zeros([im.shape[0],im.shape[1],3], 'uint8')

	# Looping over filtered contours
	for c in filtered:
		# Select a random color to draw the contour
		col = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
		# Draw the contour on the image with above color
		cv2.drawContours(objects,[c], -1, col, 2)


	cv2.imshow('objects', objects)
	cv2.waitKey(0)

	# we get the largest contour and use that to locate the hard drive
	objects = np.zeros([im.shape[0],im.shape[1],3], 'uint8')

	c = max(contours, key = cv2.contourArea)


	cv2.drawContours(objects,[c], -1, (255, 255, 0), 2)

	cv2.imshow('largest contour', objects)
	cv2.waitKey(0)

	# getting 'best fit' rectangle around the largest contour 
	rect = cv2.minAreaRect(c)
	boxPoints = cv2.boxPoints(rect)
	box = np.intp(boxPoints)
	cv2.drawContours(imCopy2,[box],0,(255,255,0),2)

	# box has four coordinates, one for each corner of the rectangle.
	# However there does not seem to be a consitent order to these coordinates
	

	corner1 = box[0]
	corner2 = box[1]
	corner3 = box[2]
	corner4 = box[3]


	# getting distances width, height and diagonal – but i dont know which is which

	dist1 = math.sqrt((corner1[0] - corner2[0]) ** 2 + (corner1[1] - corner2[1]) ** 2)

	dist2 = math.sqrt((corner1[0] - corner3[0]) ** 2 + (corner1[1] - corner3[1]) ** 2)
	dist3 = math.sqrt((corner1[0] - corner4[0]) ** 2 + (corner1[1] - corner4[1]) ** 2)


	dists = [dist1, dist2, dist3]
	# by sorting, the height of the hard drive will be the first element, and the 
	# width will be the second element
	dists.sort()

	width = dists[1]
	height = dists[0]

	print(f"pixel width = {width}; pixel height = {height}")
	HARD_DRIVE_WIDTH = 146
	HARD_DRIVE_HEIGHT = 101

	horizontalRatio = HARD_DRIVE_WIDTH / width
	verticalRatio = HARD_DRIVE_HEIGHT / height

	print(horizontalRatio, verticalRatio)
	cv2.imshow('finalBox', imCopy2)
	cv2.waitKey(0)

	cv2.imwrite("FinalBox.jpg", imCopy2)

	return (horizontalRatio, verticalRatio)

if __name__ == "__main__":
	horiRatio, vertRatio = getPixelToMMRatio("/Users/unswaccount/Desktop/img.jpg")
	
