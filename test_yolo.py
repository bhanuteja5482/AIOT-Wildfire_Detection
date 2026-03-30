from ultralytics import YOLO
import os

# load trained YOLO model
model = YOLO("yolov8n.pt")

# folder that contains wildfire images
folder = "images"

# loop through each image in the folder
for img in os.listdir(folder):
    path = os.path.join(folder, img)
    print("Processing:", path)

    # run detection and save results
    results = model(path, save=True)

print("🔥 Fire detection completed!")