# inference_example.py
import torch
import cv2
import numpy as np

from Phase2.models.multitask_model import MultitaskYOLO
from ultralytics.yolo.utils.ops import non_max_suppression  # selon version

device = "cuda:0" if torch.cuda.is_available() else "cpu"
model = MultitaskYOLO("/kaggle/working/pretrained/yolov8m.pt",
                      "/kaggle/working/models/yolov8m_emotions_affectnet.pt",
                      device=device)
model.eval()

img_bgr = cv2.imread("/kaggle/working/some_image.jpg")
img, _, _ = ...  # use the same letterbox preprocessing from dataset code
img_tensor = torch.tensor(img).unsqueeze(0).to(device)  # [1,3,H,W]

with torch.no_grad():
    out = model(img_tensor, task=None)  # returns dict with 'object' and 'emotion' raw outputs

# Apply NMS separately
obj_raw = out["object"]
emo_raw = out["emotion"]

# If using Ultralytics' nms:
# from ultralytics.yolo.utils.ops import non_max_suppression
obj_preds = non_max_suppression(obj_raw, conf_thres=0.25, iou_thres=0.45)
emo_preds = non_max_suppression(emo_raw, conf_thres=0.25, iou_thres=0.45)

# obj_preds and emo_preds are lists (per batch) of detections [x1,y1,x2,y2,conf,cls]
