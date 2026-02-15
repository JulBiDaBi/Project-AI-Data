from Phase2.models.multitask_model import MultitaskYOLO

model = MultitaskYOLO(
    detection_model_name="yolov8m.pt",
    emotion_model_path="/kaggle/working/models/yolov8m_emotions_affectnet.pt",
    num_emotions=8
)
