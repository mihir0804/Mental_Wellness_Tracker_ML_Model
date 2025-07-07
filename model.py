from transformers import pipeline

emotion_classifier = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    return_all_scores=True
)

def predict_emotion(text):
    results = emotion_classifier(text)[0]
    results = sorted(results, key=lambda x: x['score'], reverse=True)
    top_emotion = results[0]['label']
    top_score = results[0]['score']
    return top_emotion, results, top_score

