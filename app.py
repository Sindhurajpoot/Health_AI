from flask import Flask, request, jsonify, send_from_directory
from textblob import TextBlob
from flask_cors import CORS

app = Flask(__name__, static_folder=".", static_url_path="")
CORS(app)

# -----------------------------------
# Disease Prediction
# -----------------------------------
def predict_disease(text):
    text = text.lower()

    if "chest pain" in text:
        return "Heart-related Issue", 90

    elif "fever" in text and "cough" in text:
        return "Flu", 70

    elif "headache" in text:
        return "Migraine", 60

    elif "stress" in text or "anxiety" in text:
        return "Stress-related Health Issue", 65

    else:
        return "General Health Checkup Recommended", 40


# -----------------------------------
# Emotion Detection
# -----------------------------------
def detect_emotion(text):
    text = text.lower()

    if "stress" in text or "stressed" in text or "anxiety" in text:
        return "😟 Stressed"

    polarity = TextBlob(text).sentiment.polarity

    if polarity < -0.2:
        return "😟 Stressed"
    elif polarity > 0.2:
        return "😊 Positive"
    else:
        return "😐 Neutral"


# -----------------------------------
# Serve Frontend
# -----------------------------------
@app.route("/")
def home():
    return send_from_directory(".", "index.html")


# -----------------------------------
# Main Analysis Route
# -----------------------------------
@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    user_input = data.get("text", "")

    disease, risk = predict_disease(user_input)
    emotion = detect_emotion(user_input)

    # Alert Level
    if risk >= 85:
        alert = "HIGH"
    elif risk >= 60:
        alert = "MEDIUM"
    else:
        alert = "LOW"

    # Future Risk Prediction
    future_risk = min(risk + 10, 95)

    # Confidence Score
    confidence = min(risk + 5, 95)

    # Personalized AI Insight
    insight = f"Based on your symptoms and emotional state, you may be at risk of {disease}."

    # Advice
    if alert == "HIGH":
        advice = "Immediate medical attention is recommended."
    elif alert == "MEDIUM":
        advice = "Consult a doctor soon and monitor symptoms carefully."
    else:
        advice = "Home care, hydration, and rest are sufficient."

    return jsonify({
        "disease": disease,
        "emotion": emotion,
        "risk": risk,
        "future_risk": future_risk,
        "confidence": confidence,
        "insight": insight,
        "advice": advice,
        "alert": alert
    })


if __name__ == "__main__":
    app.run(debug=True)
