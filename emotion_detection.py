
# Import necessary libraries from Flask
import requests, json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    e_obj = { "raw_document": { "text": text_to_analyse } }  # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Set the headers required for the API request
    response = requests.post(url, json = e_obj, headers=header)  # Send a POST request to the API with the text and headers
    
    #return response.text  # Return the response text from the API
    
    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)
 
     # Extracting requred set of emotions and score from the response
    emotions = formatted_response['documentSentiment']['emotion']

    anger_score = formatted_response['documentSentiment']['anger']
    disgust_score = formatted_response['documentSentiment']['disgust']
    fear_score = formatted_response['documentSentiment']['fear']
    joy_score = formatted_response['documentSentiment']['joy']
    sadness_score = formatted_response['documentSentiment']['sadness']
    

    # Returning a dictionary containing sentiment analysis results
    return {'anger': anger_score,'disgust': disgust_score, \
            'fear': fear_score,'joy': joy_score, \
            'sadness': sadness_score, \ 
            'dominant_emotion': 'anger'}