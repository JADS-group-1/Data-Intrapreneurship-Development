from flask import Flask, request, jsonify, send_file
from flask_cors import CORS, cross_origin
import os
from numpy import ndarray
from ultralytics.engine.results import Results

from backend.predictor import Predictor

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", os.path.join(BASE_DIR, "uploads"))
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

predictor = Predictor()

def count(list_of_boxes):
    res = {}
    for box in list_of_boxes:
        class_name = box["class"]
        if class_name not in res:
            res[class_name] = 0
        res[class_name] += 1

    return res

def construct_results(prediction: Results, file_name: str):
    class_names = predictor.get_classes()

    zipped = zip(prediction.boxes.cls.numpy(), prediction.boxes.xywhn.numpy())
    list_of_boxes = [{"class": class_names[int(x[0])], "xywh": x[1].tolist()} for x in zipped]
    res = {"image_path": "/api/uploads/" + file_name, "boxes": list_of_boxes, "counts": count(list_of_boxes)}
    print(res)
    return res

@app.route('/api/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({"error": "No image part in the request"}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file:
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)
    else:
        return jsonify({"error": "Unknown exception"}), 500

    prediction = predictor.predict(file_path)
    return jsonify(construct_results(prediction, file.filename))

@app.route('/api/uploads/<file_name>', methods=["GET"])
def get_image(file_name):
    print(file_name)
    file_path = os.path.join(UPLOAD_FOLDER, file_name)
    if not os.path.isfile(file_path):
        return jsonify({"error": "File not found"}), 404

    return send_file(file_path, mimetype="image/" + file_name.split(".")[-1])

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)