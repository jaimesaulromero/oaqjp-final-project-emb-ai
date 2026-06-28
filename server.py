"""
Server module for the Emotion Detection application.
Defines the Flask routing and endpoints to interact with the Watson NLP API.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Inicializar la aplicación Flask
app = Flask(__name__)


@app.route("/")
def render_index_page():
    """
    Renders the main user interface page (index.html).
    """
    return render_template('index.html')


@app.route("/emotionDetector")
def emot_detector():
    """
    Retrieves text from the request arguments, runs emotion detection,
    and returns a formatted string with the scores and dominant emotion.
    Handles invalid or blank text by returning an error message.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']

    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    