"""
This is a Flask app for analyzing the emotions expressed in a given text.
"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

# Initiating the Flask app
app = Flask(__name__)

# Defining the '/emotionDetector' route for analyzing the emotions
@app.route("/emotionDetector")
def send_emotion():
    """
    This is the logic that gets run when accessing the '/emotionDetector' endpoint
    """
    text_to_analyze = request.args["textToAnalyze"]
    emotion_dict = emotion_detector(text_to_analyze)
    anger_score = emotion_dict["anger"]
    disgust_score = emotion_dict["disgust"]
    fear_score = emotion_dict["fear"]
    joy_score = emotion_dict["joy"]
    sadness_score = emotion_dict["sadness"]
    dominant_emotion = emotion_dict["dominant_emotion"]

    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    return f"For the given statement, the system response is 'anger': {anger_score}, \
            'disgust': {disgust_score}, 'fear': {fear_score}, 'joy': {joy_score}, \
            and 'sadness': {sadness_score}. The dominant emotion is {dominant_emotion}."

# Defining the rout route
@app.route("/")
def main_page():
    """
    This function renders the index.html file when accessing the '/' route
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run("0.0.0.0", port=5000)
