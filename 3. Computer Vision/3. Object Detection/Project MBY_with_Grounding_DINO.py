# Purpose 

"""
This project aims to implement an object detection and tracking tasks on Bel's products using YOLOv5.
"""

# ISSUES
"""
Before we start, here are some potential issues:

Issue 1:  The YOLO model is not fine-tune on Bel's products datasets. Therefore,
    - The model will not detect these objects because it does not recognize them.
    - It may confuse these objects with similar classes that it does recognize.
  ==> You may consider retraining (fine-tuning) the model with your own classes.

Issue 2: I do not have neither data nor time to annotate the Bel's products images. Therefore,
  ==> I'll implement an 'open-world' or 'zero-shot' model such as CLIP or Grounding DINO.
    GO TO KNOW: open-world model can detect objects based on a textual description, even if they have not been trained on these classes.
"""

# My approach
"""
To create a pipeline for detecting cheese in a video with Grounding DINO, here's what we'll do:
    - Pipeline steps
    - Load the video and extract the frames.
    - Load the pre-trained Grounding DINO model.
    - Define a text query such as ‘cheese’, “camembert”, ‘soft cheese’, etc.
    - Apply the model to each frame to detect cheese.
    - Draw detection boxes on the frames.venv
    - Reassemble the annotated video.
"""

# 0. Setup Configuration

# 0.1. Install packages
# a. Download packages
!pip install -q -U groundingdino-py supervision ipywidgets timm

# b. External packages requested
# --> Clone 'Groundingdino' Repository
!git clone https://www.github.com/IDEA-Research/GroundingDINO.git

# --> Build the custom C++ operators
!python setup.py build_ext --inplace

# --> Download the pre-trained model weights
!curl -L -o groundingdino_swint_ogc.pth https://github.com/IDEA-Research/GroundingDINO/releases/download/v0.1.0-alpha/groundingdino_swint_ogc.pth

# c. Load requested libraries
import os 
import supervision as sv
import torch
import cv2
import matplotlib.pyplot as plt


from groundingdino.util.inference import Model

# 0.2. Parameters Configuration and Loading Video
# a. Parameters configuration
# --> Parameters
HOME = os.getcwd()

model_config_path = os.path.join(HOME, 'GroundingDINO/groundingdino/config/GroundingDINO_SwinT_OGC.py')
model_checkpoint_path = os.path.join(HOME, 'GroundingDINO/groundingdino_swint_ogc.pth')

# --> Load the Grounding DINO model
DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = Model(model_config_path=model_config_path, model_checkpoint_path=model_checkpoint_path, device=DEVICE)

# --> Quick checking
print(
    f'{model_config_path}\n'
    f'{model_checkpoint_path}\n'
    f'Loading the Grounding DINO model ............\n'
)

# b. Load video and extract frames to stock in a folder

## Create a directory to store the frames
if not os.path.exists('frames'):
    os.makedirs('frames')

## Open the video file
video_path = './Data/IMG_0121.MP4'
cap = cv2.VideoCapture(video_path)

## Check if the video opened successfully
if not cap.isOpened():
    print("Error: Could not open video.")
else:
    # Get the frame rate of the video
    fps = cap.get(cv2.CAP_PROP_FPS)
    print(f"Video FPS: {fps}")

    # Loop through the video and save each frame
    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break  # Break the loop if there are no more frames

        # Save the frame as a JPEG image
        frame_filename = os.path.join('frames', f'frame_{frame_count:04d}.jpg')
        cv2.imwrite(frame_filename, frame)
        frame_count += 1

    # Release the video capture object
    cap.release()
    print(f"Successfully extracted {frame_count} frames from the video.")
    
# 1. Processing

# a. Labeling and display the first  framme
# --> Define the text prompt
TEXT_PROMPT = "cheese"

# --> Load the first frame
image = cv2.imread('frames/frame_0000.jpg')

# --> Perform the detection
detections, labels = model.predict_with_caption(
    image=image,
    caption=TEXT_PROMPT,
    box_threshold=0.35,
    text_threshold=0.25
)

# --> Annotate the image with the detections
box_annotator = sv.BoxAnnotator()
annotated_image = box_annotator.annotate(scene=image.copy(), detections=detections, labels=labels)

# --> Display the annotated image
sv.plot_image(annotated_image)

# b. Extract frames  from the video + Automatical frames' annotation + Reconstruct an annotated video

# --> Extract frames
## Create a directory to store the annotated frames
if not os.path.exists('annotated_frames'):
    os.makedirs('annotated_frames')

## Get the list of frame files
frame_files = sorted([f for f in os.listdir('frames') if f.endswith('.jpg')])

## Process each frame
for frame_file in frame_files:
    # Load the frame
    image = cv2.imread(os.path.join('frames', frame_file))

    # Perform the detection
    detections, labels = model.predict_with_caption(
        image=image,
        caption=TEXT_PROMPT,
        box_threshold=0.35,
        text_threshold=0.25
    )

# --> Automatical frame annotation
    # Annotate the image with the detections
    box_annotator = sv.BoxAnnotator()
    annotated_image = box_annotator.annotate(scene=image.copy(), detections=detections, labels=labels)

    # Save the annotated frame
    annotated_frame_filename = os.path.join('annotated_frames', frame_file)
    cv2.imwrite(annotated_frame_filename, annotated_image)

print(f"Successfully annotated {len(frame_files)} frames.")

# --> Reassemble the annotated frames into a video
output_video_path = 'annotated_video.mp4'
frame_size = (image.shape[1], image.shape[0])
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_video_path, fourcc, fps, frame_size)

for frame_file in frame_files:
    annotated_frame_path = os.path.join('annotated_frames', frame_file)
    out.write(cv2.imread(annotated_frame_path))

out.release()

print(f"Successfully created the annotated video: {output_video_path}")

# Approach 1  
# Définir la zone d’intérêt (ROI)
x, y, w, h = 700, 200, 200, 300

# Créer un dossier pour stocker les frames annotées avec ROI
if not os.path.exists('annotated_frames_roi'):
    os.makedirs('annotated_frames_roi')

cheese_counts = []

for frame_file in frame_files:
    # Charger la frame
    image = cv2.imread(os.path.join('frames', frame_file))
    roi = image[y:y+h, x:x+w]

    # Appliquer le modèle sur la ROI
    detections, labels = model.predict_with_caption(
        image=roi,
        caption="cheese",
        box_threshold=0.35,
        text_threshold=0.25
    )

    # Ajuster les coordonnées des boîtes détectées
    adjusted_boxes = detections.xyxy + [x, y, x, y]
    adjusted_detections = sv.Detections(
        xyxy=adjusted_boxes,
        confidence=detections.confidence,
        class_id=detections.class_id
    )

    # Compter les fromages détectés dans la ROI
    cheese_count = sum(1 for label in labels if 'cheese' in label.lower())
    cheese_counts.append(cheese_count)

    # Annoter l’image complète avec les détections
    box_annotator = sv.BoxAnnotator()
    annotated_image = box_annotator.annotate(scene=image.copy(), detections=adjusted_detections, labels=labels)

    # Dessiner la ROI en rouge
    cv2.rectangle(annotated_image, (x, y), (x+w, y+h), (0, 0, 255), 2)

    # Sauvegarder la frame annotée
    annotated_frame_filename = os.path.join('annotated_frames_roi', frame_file)
    cv2.imwrite(annotated_frame_filename, annotated_image)

print(f"Nombre moyen de fromages détectés dans la ROI par frame : {sum(cheese_counts)/len(cheese_counts):.2f}")

# --> Reassemble the annotated ROI frames into a video
output_video_path = 'annotated_roi_video.mp4'
# Get sorted list of annotated ROI frames
frame_files = sorted([f for f in os.listdir('annotated_frames_roi') if f.endswith('.jpg')])
# Load the first frame to get the frame size
first_frame = cv2.imread(os.path.join('annotated_frames_roi', frame_files[0]))
frame_size = (first_frame.shape[1], first_frame.shape[0])

# Set the codec and initialize the video writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
fps = 30  # Set the correct fps if you know the original video's fps
out = cv2.VideoWriter(output_video_path, fourcc, fps, frame_size)

# Write each annotated frame to the video
for frame_file in frame_files:
    annotated_frame_path = os.path.join('annotated_frames_roi', frame_file)
    frame = cv2.imread(annotated_frame_path)
    if frame is not None:
        out.write(frame)

out.release()

print(f"Successfully created the annotated video: {output_video_path}")

# --> Reassemble the annotated frames into a video
output_video_path = 'annotated_roi_video.mp4'
frame_size = (image.shape[1], image.shape[0])
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_video_path, fourcc, fps, frame_size)

for frame_file in frame_files:
    annotated_frame_path = os.path.join('annotated_frames_roi', frame_file)
    out.write(cv2.imread(annotated_frame_path))

out.release()

print(f"Successfully created the annotated video: {output_video_path}")

# Approach 2

# Define a region of interest (ROI) as a rectangle: (x1, y1, x2, y2)
ROI = (700, 200, 200, 300)

def is_box_in_roi(box, roi):
    """Check if the center of the detection box is inside the ROI."""
    x1, y1, x2, y2 = box
    roi_x1, roi_y1, roi_x2, roi_y2 = roi
    cx = (x1 + x2) / 2
    cy = (y1 + y2) / 2
    return roi_x1 <= cx <= roi_x2 and roi_y1 <= cy <= roi_y2

# Filter detections to only those inside the ROI
boxes = detections.xyxy
cheese_count = 0
for i, box in enumerate(boxes):
    if is_box_in_roi(box, ROI):
        cheese_count += 1

print(f"Number of cheese detected in ROI: {cheese_count}")

# Optionally, draw the ROI on the annotated image for visualization
annotated_with_roi = annotated_image.copy()
cv2.rectangle(annotated_with_roi, (ROI[0], ROI[1]), (ROI[2], ROI[3]), (0, 255, 0), 2)
sv.plot_image(annotated_with_roi)



# Approach 3
# Définir la zone d’intérêt (ROI)
x, y, w, h = 700, 200, 200, 300  # coin supérieur gauche (x, y), largeur (w), hauteur (h)
roi = image[y:y+h, x:x+w]

# Appliquer le modèle de détection sur la ROI
detections, labels = model.predict_with_caption(
    image=roi,
    caption="region",
    box_threshold=0.35,
    text_threshold=0.25
)

# Recaler les coordonnées des boîtes détectées
adjusted_boxes = detections.xyxy + [x, y, x, y]

# Créer un nouvel objet Detections avec les coordonnées ajustées
adjusted_detections = sv.Detections(
    xyxy=adjusted_boxes,
    confidence=detections.confidence,
    class_id=detections.class_id
)

# Compter les fromages détectés
cheese_count = sum(1 for label in labels if 'cheese' in label.lower())
print(f"Nombre de fromages détectés dans la zone : {cheese_count}")

# Annoter l’image complète avec les détections
box_annotator = sv.BoxAnnotator()
annotated_image = box_annotator.annotate(scene=image.copy(), detections=adjusted_detections, labels=labels)

# Afficher l’image annotée (option 1 : Jupyter / Notebook)
sv.plot_image(annotated_image)


