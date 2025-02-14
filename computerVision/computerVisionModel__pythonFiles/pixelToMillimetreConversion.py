# PX_TO_MM = 0.04323285714285714
from math import sqrt
from hardDriveFiltering import *

# PX_TO_MM = 0.04610285714285714
def pythag(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y1 - y2) ** 2)

def calculateHorizontalAndVerticalRatio(f):
    return getPixelToMMRatio(f)

def convertPxToMm(pixel_dimension, ratio):
    return pixel_dimension * ratio
