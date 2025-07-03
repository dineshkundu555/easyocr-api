from flask import Flask, request, jsonify
import pytesseract
from PIL import Image
import io
import base64
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return 'Tesseract OCR API is running!'

@app.route('/ocr', methods=['POST'])
def ocr():
    try:
        data = request.get_json()

        if 'image_url' in data:
            response = requests.get(data['image_url'])
            image = Image.open(io.BytesIO(response.content))

        elif 'base64' in data:
            image_data = base64.b64decode(data['base64'])
            image = Image.open(io.BytesIO(image_data))

        else:
            return jsonify({'error': 'No image_url or base64 provided'}), 400

        text = pytesseract.image_to_string(image)
        return jsonify({'text': text})

    except Exception as e:
        return jsonify({'error': str(e)}), 500
