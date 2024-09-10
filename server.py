"""My Emotion Dectector app"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/")
def render_index_page():
    """html renderer"""
    return render_template('index.html')

@app.route("/emotionDetector")
def emo_detection():
    """emo detector"""
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] == 'None':
        return  "Invalid text! Please try again!."

    # Return the emotion detected from given string
    return f'For the given statement, the system response is {response}'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    