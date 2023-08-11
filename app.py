from flask import Flask, jsonify, request
from sentimental import SentimentalProcessor

app= Flask(__name__)

@app.route('/sentimental', methods=['POST'])
def sentimental():
    data= request.get_json()
    if not data or 'text' not in data:
        return jsonify({'error': 'El payload debe tener la llave "texto".'}), 400
        
    processed_text= SentimentalProcessor.process(data['text'])
    return jsonify({'processed_text': processed_text}), 200

if __name__=='__main__':
    app.run(debug=True)
