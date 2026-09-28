import requests 
import json

URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

def emotion_detector(text_to_analyze):
    emotions_dict = {'anger': None, 'disgust': None, 'fear': None,
                    'joy': None, 'sadness': None, 'dominant_emotion': None }
    url = URL
    headers = HEADERS
    myObj = {"raw_document": { "text": text_to_analyze }}
    response = requests.post(url, json = myObj, headers=headers)
    if response.status_code == 400:
        return emotions_dict
    else:
        return extract_emotions(response, emotions_dict)

def extract_emotions(response, adict):
    result = json.loads(response.text)   
    emotions = result["emotionPredictions"][0]["emotion"]
    adict = emotions
    dominant_emotion = max(emotions.items(), key = lambda val: val[1])
    adict["dominant_emotion"] = dominant_emotion[0]
    return adict