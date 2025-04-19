import cv2
import torch
import functools
from io import BytesIO
from ultralytics import YOLO
import numpy as np
from PIL import Image

# Override torch.load to disable weights_only restriction
original_torch_load = torch.load
torch.load = functools.partial(original_torch_load, weights_only=False)

# Load models once globally
license_plate_model = YOLO("./custom_model/license_plate_detector.pt")

class UploadImageService:
    def blur_licence_plate(self, image_file) -> BytesIO:
        image_file.seek(0)
        file_bytes = np.frombuffer(image_file.read(), np.uint8)
        image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

        if image is None:
            raise ValueError("Failed to decode image. Ensure it's a valid format.")

        plate_results = license_plate_model(image)[0]

        for box in plate_results.boxes.data.tolist():
            x1, y1, x2, y2, _, _ = map(int, box[:6])
            roi = image[y1:y2, x1:x2]
            blurred = cv2.GaussianBlur(roi, (25, 25), 30)
            image[y1:y2, x1:x2] = blurred

        success, buffer = cv2.imencode('.jpg', image)
        if not success:
            raise ValueError("Failed to encode the processed image.")

        img_io = BytesIO(buffer.tobytes())
        img_io.seek(0)
        return img_io


    