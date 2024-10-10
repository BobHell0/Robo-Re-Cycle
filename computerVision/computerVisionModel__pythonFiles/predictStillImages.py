from ultralytics import YOLO
from writeCoordsToFile import writeCoords, clearCoordsFile
from pixelToMillimetreConversion import convertPxToMm

ORIGIN_POINT = (266.7, 71.0)    # How this was achieved can be read about in findingOrigin.md
if __name__ == "__main__":

    modelFile = "example.pt"        # This is the .pt file you get AFTER training an computer vision model
    model = YOLO(f"{modelFile}")    # Lets us load up the already trained YOLOv8n model

    # Run batched inference on a list of images
    imageFiles = "exampleImages"        # can either be a path to one image or a whole directory with images

    # capturing the results in a variable called "results"
    #   - save=True saves the images WITH bounding boxes in the same direcotry
    #   - conf=0.01 lets you set the THRESHOLD CONFIDENCE (to 1% in this case)
    #   - iou refers to likelyhood of overlap – 0.1 means there shouldn't be overlapping bounding boxes

    results = model.predict(f"{imageFiles}", save=True, imgsz=320, conf=0.01, iou=0.1)

    # Extract bounding boxes, classes, names, and confidences
    boxes = results[0].boxes.xyxy.tolist()
    # classes = results[0].boxes.cls.tolist()
    # names = results[0].names
    # confidences = results[0].boxes.conf.tolist()

    # Iterate through the results
    clearCoordsFile()
    # for box, cls, conf in zip(boxes, classes, confidences):
    for box in boxes:
        x1, y1, x2, y2 = box
        # confidence = conf
        # detected_class = cls
        # name = names[int(cls)]

        centreX = (x1 + x2) / 2
        centreY = (y1 + y2) / 2
        
        # This conversion process requires the PIXEL_TO_MM ratio. How this ratio
        # was determined can be read about in findingPxToMMRatio.md
        converted_CentreX = convertPxToMm(centreX)
        converted_CentreY = convertPxToMm(centreY)


        # Writes the finalised, global coordinates to a file for the Roland to use
        # to approach a screw    
        writeCoords(ORIGIN_POINT[0] - converted_CentreX, ORIGIN_POINT[1] + converted_CentreY)
        