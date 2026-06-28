import requests
import json

def emotion_detector(text_to_analyze):
    # URL de la función Emotion Predict de Watson NLP
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Header con el ID del modelo de emociones requerido
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Payload o JSON de entrada utilizando la variable solicitada
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    # Envío de la petición POST a la API
    response = requests.post(url, json=myobj, headers=headers)
    
    # --- MANEJO DE ERRORES: STATUS CODE 400 ---
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    # Si la petición es exitosa (status_code 200), procesamos el JSON normalmente
    formatted_response = json.loads(response.text)
    
    # Extracción del diccionario de emociones específico
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    # Extracción individual de los puntajes
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']
    
    # Diccionario intermedio para evaluar cuál tiene la puntuación más alta
    emotion_list = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    
    # Lógica para encontrar la emoción dominante
    dominant_emotion = max(emotion_list, key=emotion_list.get)
    
    # Construcción del diccionario final
    result = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
    
    return result