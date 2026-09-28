import requests 
import json

URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

def emotion_detector(text_to_analyze):
    url = URL
    headers = HEADERS
    myObj = {"raw_document": { "text": text_to_analyze }}
    response = requests.post(url, json = myObj, headers=headers)
    return extract_emotions(response)

def extract_emotions(response):
    result = json.loads(response.text)   
    emotions = result["emotionPredictions"][0]["emotion"]
    dominant_emotion = max(emotions.items(), key = lambda val: val[1])
    emotions["dominant_emotion"] = dominant_emotion[0]
    return emotions