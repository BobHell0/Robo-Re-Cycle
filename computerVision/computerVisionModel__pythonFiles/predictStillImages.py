from ultralytics import YOLO
from writeCoordsToFile import writeCoords, clearCoordsFile
from pixelToMillimetreConversion import pythag, convertPxToMm

ORIGIN_POINT = (266.7, 71.0)
if __name__ == "__main__":

    # ORIGIN_POINT_MM = 

    # Load a model
    modelFile = "/Users/unswaccount/Documents/Studying/Year 2/VIP - Robo-Re-Cycle/Object Detection Data/pythonFiles.py/runs/detect/screwsAndHoles_5/weights/best.pt"
    model = YOLO(f"{modelFile}")  # pretrained YOLOv8n model

    # Run batched inference on a list of images
    imageFiles = "/Users/unswaccount/Desktop/VIP Wk 4 Thursday/LinedPaper__30_35_37_37/test1.jpg"

    model.predict(f"{imageFiles}", save=True, imgsz=320, conf=0.05, show_boxes=True, iou=0.1)

    results = model.predict(f"{imageFiles}", save=False, imgsz=320, conf=0.01)

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
        # print(f"Found a {cls}")
        # print(f"Top Left coords = {x1}, {y1} | Bottom Right coords = {x2}, {y2}")
        centreX = (x1 + x2) / 2
        centreY = (y1 + y2) / 2
        
        # print(f"centreX = {centreX}; centreY = {centreY} in PIXELS")

        converted_CentreX = convertPxToMm(centreX)
        converted_CentreY = convertPxToMm(centreY)


        
        writeCoords(ORIGIN_POINT[0] - converted_CentreX, ORIGIN_POINT[1] + converted_CentreY )
        
