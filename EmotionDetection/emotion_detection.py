import requests
import json

def emotion_detector(text_to_analyse):
    # Define the IBM Watson URL for the emotion detection API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Create the payload with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } }
    # Set the headers with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=myobj, headers=header)
    
    # Check for blank entries and handle status code 400
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    # Parse the response from the API
    formatted_response = json.loads(response.text)
    
    # Extract emotions and their scores
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    extracted_emotions = {emotion: score for emotion, score in emotions.items()}
    
    # Find the dominant emotion
    dominant_emotion = max(extracted_emotions, key=extracted_emotions.get)
    extracted_emotions['dominant_emotion'] = dominant_emotion
    
    return extracted_emotions
