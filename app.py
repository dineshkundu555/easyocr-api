from flask import Flask, request, jsonify
import easyocr
from PIL import Image
import io

app = Flask(__name__)
reader = easyocr.Reader(['en'], gpu=False)

@app.route('/ocr', methods=['POST'])
def ocr():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    image_file = request.files['image']
    image = Image.open(image_file.stream).convert('RGB')
    image_bytes = io.BytesIO()
    image.save(image_bytes, format='PNG')
    image_bytes = image_bytes.getvalue()

    result = reader.readtext(image_bytes, detail=0)
    return jsonify({'text': result})

@app.route('/', methods=['GET'])
def home():
    return "EasyOCR API is running."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
