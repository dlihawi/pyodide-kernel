import requests
import json


def emotion_detector(text_to_analyze):
    # Define the URL and headers
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Construct input JSON payload
    input_json = {"raw_document": {"text": text_to_analyze }}

    try:
        # Make the API request
        response = requests.post(url, headers=headers, json=input_json)
        
        # Convert response text to dictionary
        formatted_response = json.loads(response.text)
        
        # Extract emotion predictions
        emotion_predictions = formatted_response['emotionPredictions'][0]['emotion']
        
        # Extract scores for each emotion
        anger_score = emotion_predictions.get('anger', 0)
        disgust_score = emotion_predictions.get('disgust', 0)
        fear_score = emotion_predictions.get('fear', 0)
        joy_score = emotion_predictions.get('joy', 0)
        sadness_score = emotion_predictions.get('sadness', 0)
        
        # Determine dominant emotion
        emotion_scores = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score
        }
        
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)
        
        # Prepare output dictionary
        output = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }
        
        return output
    
    except Exception as e:
        print(f"Error in emotion detection: {e}")
        return None
