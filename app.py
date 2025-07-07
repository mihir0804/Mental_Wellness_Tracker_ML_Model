import gradio as gr
from model import predict_emotion
from db import init_db, log_prediction
from log_config import logging

init_db()

def analyze_text(text):
    try:
        emotion, scores, confidence = predict_emotion(text)
        log_prediction(text, emotion, confidence)
        logging.info(f"Predicted: {emotion} with confidence {confidence:.2f}")
        return emotion, {score["label"]: round(score["score"], 2) for score in scores}, "How accurate is this?"
    except Exception as e:
        logging.error("Error during prediction", exc_info=True)
        return "Error", {}, "Something went wrong."

iface = gr.Interface(
    fn=analyze_text,
    inputs=gr.Textbox(label="Enter your journal entry", lines=4, placeholder="How are you feeling today?"),
    outputs=[
        gr.Text(label="Predicted Emotion"),
        gr.Label(label="Emotion Confidence Scores"),
        gr.Text(label="Feedback Prompt")
    ],
    title="🧠 Mental Wellness Tracker",
    description="This tool uses a transformer model to detect emotions in daily journal entries."
)

iface.launch()
