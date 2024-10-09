# The primary file that is used to train new computer vision models or retrain
# existing ones

# More information can be found on the ultralytics documentation.

# The tutorial I followed to carry out the process of training a Computer Vision
# model: https://www.youtube.com/watch?v=m9fH9OWn8YM

from ultralytics import YOLO

NUM_EPOCHS = 300    # An Epoch refers to a layers or cycle of training – 300 epochs 
                    # means you want show your model in training your data set 300 times

# build a new model from scratch
model = YOLO("yolov8n.yaml")  

# Alternatively you can retrain a model you have previously trained:

# currentModel = <Path to model you want to retrian>
# model = YOLO(currentModel) # load an existing model

# Use the model – see config.yaml for more information on WHERE to get the 
model.train(data="config.yaml", epochs=NUM_EPOCHS)  # train the model