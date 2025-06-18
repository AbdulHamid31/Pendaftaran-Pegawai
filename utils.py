import face_recognition
import numpy as np
import json

def get_embedding(image):
    rgb_img = image[:, :, ::-1]  # BGR to RGB
    encodings = face_recognition.face_encodings(rgb_img)
    return encodings[0] if encodings else None

def load_knowledge_base(path="knowledge_base.json"):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_knowledge_base(kb, path="knowledge_base.json"):
    with open(path, "w") as f:
        json.dump(kb, f, indent=2)
