# Import libraries
import cv2
import numpy as np
import random
import math
from matplotlib import pyplot as plt

def findOrigin(f: str):
	im = cv2.imread(f)
	hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
	hsv = cv2.blur(hsv, (5,5))

	imCopy2 = im.copy()


	lower = np.array([70, 0, 0])
	upper = np.array([80, 255, 100])

	mask = cv2.inRange(hsv, lower, upper)

	

	# flipping the mask so that the green is black and the hard drive is white
	# mask = cv2.bitwise_not(mask)
	im = cv2.bitwise_and(im, im, mask=mask)

	cv2.imshow('adding inverted pink filter mask', im)
	cv2.waitKey(0)

	# threshold to make a
	im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

	# cv2.imshow('greyed out', im)
	# cv2.waitKey(0)
	ret, im = cv2.threshold(im, 0 , 255, cv2.THRESH_BINARY)
	# im = cv2.erode(im, np.ones((2,2), np.uint8), iterations=15)
	# im = cv2.dilate(im, np.ones((2,2), np.uint8), iterations=15)
	ret, im = cv2.threshold(im, 1, 255, cv2.THRESH_BINARY)

	cv2.imshow('threshold image', im)
	cv2.waitKey(0)

	# img_edge = cv2.Canny(im, 200, 300)
	# cv2.imshow('edge detection', img_edge)
	# cv2.waitKey(0)



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
	

	corners =  [box[0], box[1], box[2], box[3]]

	corners.sort(key=lambda x:x[0])
	mid_x = (corners[0][0] + corners[2][0]) / 2

	corners.sort(key=lambda x:x[1])
	mid_y = (corners[0][1] + corners[2][1]) / 2

	print(mid_x, mid_y)



	


	
	# cv2.imshow('Origin Finding', imCopy2)
	# cv2.waitKey(0)

	cv2.imwrite("OriginFinding.jpg", imCopy2)

	return (mid_x, mid_y)


if __name__ == "__main__":
	findOrigin("/Users/unswaccount/Desktop/picsWIthGreenOrigin/test1.jpg")
