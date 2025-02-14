from ultralytics import YOLO

NUM_EPOCHS = 150
# Load a model
# model = YOLO("yolov8n.yaml")  # build a new model from scratch

model = YOLO("/Users/unswaccount/Documents/Studying/Year 2/VIP - Robo-Re-Cycle/Object Detection Data/pythonFiles.py/runs/detect/screwsAndHoles_7/weights/best.pt") # load an existing model

# Use the model
model.train(data="config.yaml", epochs=NUM_EPOCHS)  # train the model