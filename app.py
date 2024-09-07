from flask import Flask, jsonify, send_file
from flask_cors import CORS
from PIL import Image, ImageDraw, ImageFont
import random
import io

app = Flask(__name__)
CORS(app)

def generate_nft():
    # Create a blank image
    img = Image.new('RGB', (300, 300), color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    
    # Add text
    d = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 100)
    characters = ['😀', '😎', '🤖', '👽', '🦄']
    character = random.choice(characters)
    d.text((100, 100), character, fill=(255, 255, 255), font=font)
    
    # Save to a bytes buffer
    buf = io.BytesIO()
    img.save(buf, format='PNG')
    buf.seek(0)
    return buf

@app.route('/generate_nft', methods=['GET'])
def get_nft():
    img_buf = generate_nft()
    return send_file(img_buf, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
