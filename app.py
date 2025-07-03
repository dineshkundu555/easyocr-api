from flask import Flask, request, jsonify
import pytesseract
from PIL import Image
import io
import base64

app = Flask(__name__)

@app.route("/ocr", methods=["POST"])
def ocr():
    data = request.json
    image_data = base64.b64decode(data["image_base64"])
    image = Image.open(io.BytesIO(image_data))
    text = pytesseract.image_to_string(image)
    return jsonify({"text": text})
