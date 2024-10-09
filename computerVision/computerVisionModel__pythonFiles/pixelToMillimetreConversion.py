# PX_TO_MM = 0.04323285714285714
from math import sqrt

# PX_TO_MM = 0.04610285714285714
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
# distnaces between screws (in mm), and automate the experiment

def convertPxToMm(pixel_dimension):
    return pixel_dimension * PX_TO_MM






# # A, B, C, D, E, F, G
# # allPxCoords = [(2314, 2096), (537, 781), (1063, 1693), (1652, 354), (1381, 1672), (3316, 2000), (2716, 768), (2136, 1285)]
# # allPxCoords = [(4049, 2178), (157, 1288), (648, 2152), (3356, 1585), (2587, 2177), (4427, 1223), (3451, 881), (2054, 1213)]

# allPxCoords = [(542, 306), (2037, 231), (3415, 303), (529, 2229), (2261, 2285), (3444, 2217), (2719, 1530)]

# pointLabels = ["A", "B", "C", "D", "E", "F", "G"]
# i = 0
# counter = 1
# while i < len(allPxCoords):
#     j = i + 1
#     currCoord = allPxCoords[i]
#     currPoint = pointLabels[i]
#     while j < len(allPxCoords):
#         adjCoord = allPxCoords[j]
#         adjPoint = pointLabels[j]

#         distance = pythag(currCoord[0], currCoord[1], adjCoord[0], adjCoord[1])

#         print(f"{counter}. Estimated distance between {currPoint} and {adjPoint} is {round(convertPxToMm(distance), 3)} mm")
#         j += 1
#         counter += 1
#     i += 1

