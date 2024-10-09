# Code taken from: https://dipankarmedh1.medium.com/real-time-object-detection-with-yolo-and-webcam-enhancing-your-computer-vision-skills-861b97c78993
# The file used to test a computer vision model using a webcam.
# Useful for IF we choose to use a live camera to detect objects.

from ultralytics import YOLO
import cv2
import math 
import time

# start webcam
cap = cv2.VideoCapture(0)

# model
modelFile = "./Object Detection Data/runs/detect/train/weights/best.pt"
model = YOLO(modelFile)

# object classes
classNames = ["hole", "torx-screw"]


while True:
    success, img = cap.read()
    results = model(img, stream=True)

    # coordinates
    for r in results:
        boxes = r.boxes

        for box in boxes:
            # bounding box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2) # convert to int values

            # put box in cam
            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

            # confidence
            confidence = math.ceil((box.conf[0]*100))/100
            print("Confidence --->",confidence)

            # class name and coordinates (in pixels)
            cls = int(box.cls[0])
            print(f"Class name --> {classNames[cls]}")
            print(f"Coordinates: {x1} {y1} and {x2} {y2}")

            # object details
            org = [x1, y1]
            font = cv2.FONT_HERSHEY_SIMPLEX
            fontScale = 1
            color = (255, 0, 0)
            thickness = 2

            cv2.putText(img, classNames[cls], org, font, fontScale, color, thickness)


    cv2.imshow('Webcam', img)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()