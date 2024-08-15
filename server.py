"""
This is the Emotion Detector Server
"""

# Import Flask, render_template, request from the flask framework package
from flask import Flask, request, render_template

# Import the emotion_detector function from the package created
from EmotionDetection.emotion_detection import emotion_detector

# Initiate the flask app
app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def emo_detector():
    """
    Endpoint to analyze emotions in the given statement.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Check if the dominant emotion is None and handle such an error
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again."

    return f"For the given statement, the system response is: {response}"


@app.route("/")
def render_index_page():
    """
    Render the index page to deploy.
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5050)
    