
# Import necessary libraries from Flask
from flask import Flask, redirect, request, render_template, url_for

# Instantiate Flask application
app = Flask(__name__)

text_to_analyze = 

URL: 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
Headers: {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
Input json: { "raw_document": { "text": text_to_analyse } }

@app.route("/")
def emotion_detector("text_to_analyse"):
    return "text"


