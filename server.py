from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Instantiate the emotion analyzer app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sentiment_analyzer():
    text_to_analyze = request.args.get("textToAnalyze")
    print("Input text", text_to_analyze)
    result = emotion_detector(text_to_analyze)
    return f"""For the given statement, the system response is 'anger': {result["anger"]}, 
    'disgust': {result["disgust"]}, 'fear': {result["fear"]}, 'joy': {result["joy"]} and 
    'sadness': {result["sadness"]}. The dominant emotion is {result["dominant_emotion"]}."""

@app.route("/")
def render_index_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
