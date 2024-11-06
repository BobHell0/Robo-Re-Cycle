# Import libraries
import cv2
import numpy as np
import random
import math
from matplotlib import pyplot as plt

def nothing(x): pass

# Load image
original = cv2.imread("img\\final_maze3.jpg")
full_image = original[250:1970, 410:3460]
height, width, channels = full_image.shape
avg_cell_width = width / 9
avg_cell_height = height / 5
separator_left = int(4 * avg_cell_width)
separator_right = int(7 * avg_cell_width)
left_grid = full_image[0:height, 0:separator_left]
middle_cont = full_image[0:height, separator_left:separator_right]
right_grid = full_image[0:height, separator_right:width]

image = left_grid
# Create a window
cv2.namedWindow('image', cv2.WINDOW_NORMAL) 
cv2.resizeWindow('image', 900, 700)

# Create trackbars for color change
# Hue is from 0-179 for Opencv
cv2.createTrackbar('HMin', 'image', 0, 179, nothing) 
cv2.createTrackbar('SMin', 'image', 0, 255, nothing) 
cv2.createTrackbar('VMin', 'image', 0, 255, nothing) 
cv2.createTrackbar('HMax', 'image', 0, 179, nothing) 
cv2.createTrackbar('SMax', 'image', 0, 255, nothing) 
cv2.createTrackbar('VMax', 'image', 0, 255, nothing)

# Set default value for Max HSV trackbars
cv2.setTrackbarPos('HMax', 'image', 179) 
cv2.setTrackbarPos('SMax', 'image', 255) 
cv2.setTrackbarPos('VMax', 'image', 255)

# Initialize HSV min/max values
hMin = sMin = vMin = hMax = sMax = vMax = 0 
phMin = psMin = pvMin = phMax = psMax = pvMax = 0

while(1):

    # Get current positions of all trackbars
    hMin = cv2.getTrackbarPos('HMin', 'image')
    sMin = cv2.getTrackbarPos('SMin', 'image')
    vMin = cv2.getTrackbarPos('VMin', 'image')
    hMax = cv2.getTrackbarPos('HMax', 'image')
    sMax = cv2.getTrackbarPos('SMax', 'image')
    vMax = cv2.getTrackbarPos('VMax', 'image')

    # Set minimum and maximum HSV values to display
    lower = np.array([hMin, sMin, vMin])
    upper = np.array([hMax, sMax, vMax])

    # Convert to HSV format and color threshold
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower, upper)
    result = cv2.bitwise_and(image, image, mask=mask)
    
    # Convert grayscale image to color image for displaying simultaneous
    mask_3_channel = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    
    # Stack images
    numpy_horizontal = np.hstack((image, result, mask_3_channel))
    
    # Display HSV values of some colours
    cv2.putText(numpy_horizontal, 'Black: (0, 0, 0)', (130, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0,255,255), 1, cv2.LINE_AA)
    cv2.putText(numpy_horizontal, 'White: (0, 0, 255)', (130, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0,255,255), 1, cv2.LINE_AA)
    cv2.putText(numpy_horizontal, 'Red: (0, 255, 255)', (130, 45), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0,255,255), 1, cv2.LINE_AA)
    cv2.putText(numpy_horizontal, 'Green: (60, 255, 255)', (130, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0,255,255), 1, cv2.LINE_AA)
    cv2.putText(numpy_horizontal, 'Blue: (120, 255, 255)', (130, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0,255,255), 1, cv2.LINE_AA)

    # Print if there is a change in HSV value
    if((phMin != hMin) | (psMin != sMin) | (pvMin != vMin) | (phMax != hMax) | (psMax != sMax) | (pvMax != vMax) ):
        print("(hMin = %d , sMin = %d, vMin = %d), (hMax = %d , sMax = %d, vMax = %d)" % (hMin , sMin , vMin, hMax, sMax , vMax))
        phMin = hMin
        psMin = sMin
        pvMin = vMin
        phMax = hMax
        psMax = sMax
        pvMax = vMax

    # Display stacked image, press q to quit
    cv2.imshow('image', numpy_horizontal)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
