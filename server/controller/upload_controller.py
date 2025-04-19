# controller/item_controller.py
# from flask import jsonify, request
# import app
# from werkzeug.utils import secure_filename
# import os
    
# @app.route('/upload-car-image', methods=['POST'])
# async def upload_car_image():
#     try:
#         if 'image' not in request.files:
#             return jsonify({"error": "No image file provided"}), 400
    
#     except Exception as e:
#         print(f"Error: {str(e)}")
#         return jsonify({"error": str(e)}), 500