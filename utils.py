from deepface import DeepFace
import json

def get_embedding(image):
    try:
        embedding = DeepFace.represent(image, model_name="SFace")[0]["embedding"]
        return embedding
    except:
        return None

def load_knowledge_base(path="knowledge_base.json"):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_knowledge_base(kb, path="knowledge_base.json"):
    with open(path, "w") as f:
        json.dump(kb, f, indent=2)
