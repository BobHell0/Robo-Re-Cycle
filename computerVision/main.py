# The primary file used for training and re-training computer vision models

from ultralytics import YOLO

NUM_EPOCHS = 300
# Load a model
model = YOLO("yolov8n.yaml")  # build a new model from scratch

# Use the model
model.train(data="config.yaml", epochs=NUM_EPOCHS)  # train the model