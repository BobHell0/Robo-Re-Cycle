# The file used to test a computer vision model using images.
# Useful for IF we choose to use periodic photographs to detect objects.

from ultralytics import YOLO
from glob import glob
import cv2
import math 
import time

PX_TO_MM = 0.04356333272

# Load a model
modelFile = "/Users/unswaccount/Documents/Studying/Year 2/VIP - Robo-Re-Cycle/Object Detection Data/runs/detect/train2/weights/best.pt"

model = YOLO(f"{modelFile}")  # pretrained YOLOv8n model

# Run batched inference on a list of images
imageFiles = "/Users/unswaccount/Documents/Studying/Year 2/VIP - Robo-Re-Cycle/Object Detection Data/topPlate datasets/v1.0_annotatedDataset/obj_Train_data/images"

model.predict(f"{imageFiles}", save=True, imgsz=320, conf=0.05, show_boxes=True, iou=0.1)


print(imageFiles)
results = model.predict(f"{imageFiles}", save=False, imgsz=320, conf=0.01)

# Extract bounding boxes, classes, names, and confidences
boxes = results[0].boxes.xyxy.tolist()
classes = results[0].boxes.cls.tolist()
names = results[0].names
confidences = results[0].boxes.conf.tolist()

# Iterate through the results
for box, cls, conf in zip(boxes, classes, confidences):
    x1, y1, x2, y2 = box
    confidence = conf
    detected_class = cls
    name = names[int(cls)]
    print(f"Found a {cls}")
    print(f"Top Left coords = {x1}, {y1} | Bottom Right coords = {x2}, {y2}")
    centreX = (x1 + x2) / 2
    centreY = (y1 + y2) / 2
    
    print(f"centreX = {centreX}; centreY = {centreY} in PIXELS")
    print(f"centreX = {centreX * PX_TO_MM}; centreY = {centreY * PX_TO_MM} in MM")
