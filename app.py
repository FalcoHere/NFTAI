from flask import Flask, jsonify, send_file, request
from flask_cors import CORS
from PIL import Image, ImageDraw, ImageFont
import random
import io
import os

app = Flask(__name__)
CORS(app)

# Create directories for storing images
os.makedirs('backgrounds', exist_ok=True)
os.makedirs('characters', exist_ok=True)

def generate_background():
    img = Image.new('RGB', (300, 300), color=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    buf = io.BytesIO()
    img.save(buf, format='PNG')
    buf.seek(0)
    return buf

def generate_character():
    img = Image.new('RGB', (300, 300), color=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    d = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 100)
    character = random.choice(['😀', '😎', '🤖', '👽', '🦄'])
    d.text((100, 100), character, fill=(255, 255, 255), font=font)
    buf = io.BytesIO()
    img.save(buf, format='PNG')
    buf.seek(0)
    return buf

@app.route('/generate_background', methods=['GET'])
def get_background():
    img_buf = generate_background()
    img_path = 'backgrounds/background_{}.png'.format(random.randint(1, 1000))
    with open(img_path, 'wb') as f:
        f.write(img_buf.getvalue())
    return send_file(img_buf, mimetype='image/png')

@app.route('/generate_character', methods=['GET'])
def get_character():
    img_buf = generate_character()
    img_path = 'characters/character_{}.png'.format(random.randint(1, 1000))
    with open(img_path, 'wb') as f:
        f.write(img_buf.getvalue())
    return send_file(img_buf, mimetype='image/png')

@app.route('/save_metadata', methods=['POST'])
def save_metadata():
    data = request.json
    with open('metadata.txt', 'a') as f:
        f.write(f"Name: {data['name']}, Description: {data['description']}\n")
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(debug=True)
