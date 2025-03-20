import os
from flask import Flask, request, jsonify
from transformers import pipeline
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/analyze": {"origins": "*"}})  # Allow all origins for /analyze

#label mapping
label_mapping = {
    "LABEL_0": "Human-Written",
    "LABEL_1": "AI-Generated"
}

# Load AI text detection model
classifier = pipeline("text-classification", model="openai-community/roberta-large-openai-detector")

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "No text provided"}), 400


    result = classifier(text)[0]
    readable_label = label_mapping.get(result["label"], "Unknown")

    return jsonify({
        "label": readable_label,
        "confidence": result["score"] * 100
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)

