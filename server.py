from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    data = request.get_json()
    text_to_analyze = data.get('text')
    if not text_to_analyze:
        return jsonify({"error": "Invalid text!Please try again!"}), 400
    
    result = emotion_detector(text_to_analyze)
    if not result:
        return jsonify({"error": "Emotion detection failed"}), 500

    # Format the response as specified
    response_text = (f"For the given statement, the system response is 'anger': {result['anger']}, "
                     f"'disgust': {result['disgust']}, 'fear': {result['fear']}, "
                     f"'joy': {result['joy']} and 'sadness': {result['sadness']}. "
                     f"The dominant emotion is {result['dominant_emotion']}.")

    return jsonify({"message": response_text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
