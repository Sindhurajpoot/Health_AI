from flask import Flask, request, jsonify, send_from_directory
from textblob import TextBlob
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# -------------------------------
# Disease Prediction
# -------------------------------
def predict_disease(text):
    text = text.lower()

    if "fever" in text and "cough" in text:
        return "Flu", 70
    elif "chest pain" in text:
        return "Heart-related Issue", 90
    elif "headache" in text:
        return "Migraine", 60
    else:
        return "General Checkup Recommended", 40

# -------------------------------
# Emotion Detection
# -------------------------------
def detect_emotion(text):
    polarity = TextBlob(text).sentiment.polarity

    if polarity < -0.2:
        return "😟 Stressed"
    elif polarity > 0.2:
        return "😊 Positive"
    else:
        return "😐 Neutral"

# -------------------------------
# API Route
# -------------------------------
@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    user_input = data.get("text", "")

    disease, risk = predict_disease(user_input)
    emotion = detect_emotion(user_input)

    # Advice logic
    if "Stressed" in emotion:
        advice = f"You may have {disease}. Your stress level is high. Please take rest, hydrate, and relax."
    else:
        advice = f"You may have {disease}. Monitor symptoms and maintain a healthy lifestyle."

    # 🔥 ALERT LEVEL (IMPORTANT FOR BUTTONS)
    if risk > 80:
        alert = "HIGH"
    elif risk > 60:
        alert = "MEDIUM"
    else:
        alert = "LOW"

    return jsonify({
        "disease": disease,
        "emotion": emotion,
        "advice": advice,
        "risk": risk,
        "alert": alert   # 🔥 NEW FIELD (VERY IMPORTANT)
    })

# -------------------------------
# Serve Frontend Files
# -------------------------------
@app.route("/")
def home():
    return send_from_directory(".", "index.html")

@app.route("/style.css")
def style():
    return send_from_directory(".", "style.css")

# -------------------------------
# Run Server
# -------------------------------
if __name__ == "__main__":
    app.run(debug=True)