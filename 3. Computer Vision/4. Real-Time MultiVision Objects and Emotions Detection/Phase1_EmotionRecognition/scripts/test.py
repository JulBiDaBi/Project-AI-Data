# Load resquested libraries
import os 

from ultralytics import YOLO
from IPython import display

# Set working directory
HOME = os.getcwd()
# HOME

# Load model 'yolov8.pt'
path_model = os.path.join(HOME, 'Phase1_EmotionRecognition', 'models', 'yolov8m_emotions_affectnet.pt')
model = YOLO(path_model)

# Predict on images
images_path = os.path.join(HOME, 'Phase1_EmotionRecognition', 'data', 'check_model_images')
image_files = [os.path.join(images_path, f"img{i}.jpeg") for i in range(1, 5)]

check_results = [model.predict(source=image, save=True, conf=0.5) for image in image_files]

# Print results
for i, result in enumerate(check_results):
    print(f"Results for {image_files[i]}:")
    display(result[i].plot())