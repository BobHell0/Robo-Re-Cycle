#!/Library/Frameworks/Python.framework/Versions/3.12/bin/python3
from ultralytics import YOLO
from writeCoordsToFile import writeCoords, clearCoordsFile
from pixelToMillimetreConversion import *
from originFinding import *

ORIGIN_POINT = (110.5, 122)
MAX_ALLOWED_DISCREP = 2

if __name__ == "__main__":

	# ORIGIN_POINT_MM = 

	# Load a model


	# Run batched inference on a list of images
	modelFile = "runs/detect/train/weights/best.pt"

	model = YOLO(f"{modelFile}")  # pretrained YOLOv8n model
	imageFiles = f"/Users/unswaccount/Desktop/picsWIthGreenOrigin/test1.jpg"

	horizontalRatio, verticalRatio = calculateHorizontalAndVerticalRatio(imageFiles)
	pixelOrigin = findOrigin(imageFiles)


	results = model.predict(f"{imageFiles}", save=True, imgsz=320, conf=0.50, iou=0.1)

	# Extract bounding boxes, classes, names, and confidences
	boxes = results[0].boxes.xyxy.tolist()
	classes = results[0].boxes.cls.tolist()
	names = results[0].names
	confidences = results[0].boxes.conf.tolist()

	# Iterate through the results
	clearCoordsFile()
	
        
	for box, cls, conf in zip(boxes, classes, confidences):
			
		x1, y1, x2, y2 = box
		confidence = conf
		detected_class = cls
		name = names[int(cls)]
		centreX = (x1 + x2) / 2
		centreY = (y1 + y2) / 2


		displacementX = centreX - pixelOrigin[0]
		displacementY = centreY - pixelOrigin[1]

		convertedDisplacementX = convertPxToMm(displacementX, horizontalRatio)
		convertedDisplacementY = convertPxToMm(displacementY, verticalRatio)

        # Current way of handling distortion
        # Read up on raspberry pi camera documenation at RasberryPiCamera.md
        # TODO: undistort images

        # if converted_CentreY < 120:
        #     converted_CentreX += 2

		estimateX = ORIGIN_POINT[0] - convertedDisplacementX
		estimateY = ORIGIN_POINT[1] + convertedDisplacementY

		writeCoords(estimateX, estimateY)
        
