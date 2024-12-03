import os
from ultralytics import YOLO

MODEL_PATH = os.getenv("MODEL_PATH", "model/turkey_trained_v8_platinum.pt")
MIN_CONFIDENCE = os.getenv("MIN_CONFIDENCE", 0.25)

class Predictor:
    def __init__(self):
        self.model = YOLO(MODEL_PATH)

    def predict(self, image_path):
        result = self.model.predict(image_path)
        return result[0]

    def get_classes(self):
        return self.model.names

