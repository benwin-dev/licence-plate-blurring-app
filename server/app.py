from bson import ObjectId
from flask import Flask,jsonify,request, send_file

from flask_pymongo import PyMongo
from flask_socketio import SocketIO
from dotenv import load_dotenv

from services.upload_image_service import UploadImageService

import json
from flask_cors import CORS  # Import CORS
load_dotenv()


app = Flask(__name__)


CORS(app)  # Enable CORS for all routes

socketio = SocketIO(app)

upload_service = UploadImageService()

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({
        "ping": "pong"        
    })

    
@app.route('/upload-car-image', methods=['POST'])
def upload_car_image():
    try:
        if 'image' not in request.files:
            return jsonify({"error": "No image file provided"}), 400
        
        image_file = request.files['image']
        # username = request.form.get('username')

        # if not username:
        #     return jsonify({"error": "Username is required"}), 400
        
        if image_file.filename == '':
            return jsonify({"error": "No selected file"}), 400
        
        processed_img_io = upload_service.blur_licence_plate(image_file)

        return send_file(
            processed_img_io,
            mimetype='image/jpeg',
            as_attachment=False,
            download_name='processed.jpg'
        )
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
