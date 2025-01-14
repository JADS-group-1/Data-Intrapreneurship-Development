import os
from ultralytics import YOLO

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.getenv("MODEL_PATH", os.path.join(BASE_DIR, "model/finaL_yolov8_freeze_10_14_epochs.pt"))
MIN_CONFIDENCE = os.getenv("MIN_CONFIDENCE", 0.25)

class Predictor:
    def __init__(self):
        self.model = YOLO(MODEL_PATH)

    def predict(self, image_path):
        result = self.model.predict(image_path)
        return result[0]

    def get_classes(self):
        return self.model.names

