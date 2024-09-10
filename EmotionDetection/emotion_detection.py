
# Import necessary libraries from Flask
import requests, json

def emotion_detector(text_to_analyse):
    
    """analyze emotions from text with ML library"""

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    e_obj = { "raw_document": { "text": text_to_analyse } }  # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Set the headers required for the API request
    response = requests.post(url, json = e_obj, headers=header)  # Send a POST request to the API with the text and headers
    
    #return response.text  # Return the response text from the API
    
    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)
   
    # If the response status code is 400, assign all dict keys to None
    if response.status_code == 400:
       return {'anger': 'None','disgust': 'None', \
            'fear': 'None','joy': 'None', \
            'sadness': 'None', \
            'dominant_emotion': 'None'}
     
     # Extracting requred set of emotions and score from the response
    extracted_emotions = formatted_response['emotionPredictions'][0]['emotion']
    print(f'Extracted Emotions and scores : {extracted_emotions}') 

    anger_score = extracted_emotions['anger']
    print(f'This is the anger score : {anger_score}')

    disgust_score = extracted_emotions['disgust']
    fear_score = extracted_emotions['fear']
    joy_score = extracted_emotions['joy']
    sadness_score = extracted_emotions['sadness']
    
    score_list = [anger_score,disgust_score,fear_score,joy_score,sadness_score]
    #print(score_list)
    max_score = max(score_list)
    print(f'This is the max score: {max_score}')

    # match the emotion key with the max_score
    for e in extracted_emotions:
        if extracted_emotions[e] == max_score:
            max_emotion = e
    
    if e == None:
        return  "Invalid text! Please try again!."

    # Returning a dictionary containing sentiment analysis results
    return {'anger': anger_score,'disgust': disgust_score, \
            'fear': fear_score,'joy': joy_score, \
            'sadness': sadness_score, \
            'dominant_emotion': max_emotion}