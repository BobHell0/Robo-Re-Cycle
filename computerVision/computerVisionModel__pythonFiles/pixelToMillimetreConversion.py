from math import sqrt

def pythag(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y1 - y2) ** 2)

PX_TO_MM = 0.041867523809523806 
# Based on the experiment conducted on images taken on Term 3 Week 4 Thursday (3rd October 2024)
# The set up was: 
# - hard drive placed in the wooden bed with the cutout slot for the HDD that Jack and Dharma made 
# - raspberry pi camera placed such that the hard drive was placed in the centre of field of view BEFORE roi values were applied 
# - ROI values <0.36,0.34,0.35,0.35> were applied

# NOTE: if any of these conditions were to change (e.g. the wooden bed is replaced or camera position is altered), this number is 
# subjected to change
# Once the Computer Vision Model is reliably accurate, you could use it to determine pixel coordinates of a hard drive with pre-known
# distances between screws (in mm), and automate the experiment

def convertPxToMm(pixel_dimension):
    return pixel_dimension * PX_TO_MM
