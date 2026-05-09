import requests
import json

def emotion_detector(text_to_analyze):

    # URL of Watson NLP EmotionPredict function
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    # Header required by the API
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    # Input JSON format
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    # Send POST request
    response = requests.post(url, json=input_json, headers=headers)

    # Convert response text into dictionary
    formatted_response = json.loads(response.text)

    # Extract emotion scores
    emotions = formatted_response["emotionPredictions"][0]["emotion"]

    anger = emotions["anger"]
    disgust = emotions["disgust"]
    fear = emotions["fear"]
    joy = emotions["joy"]
    sadness = emotions["sadness"]

    # Find dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)

    # Return required output format
    return {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
    }



