# 🚗🔍 Number Plate Blurring App

A privacy-focused AI web app that automatically detects and blurs vehicle number plates in images — perfect for sharing car photos on social media or marketplaces without revealing sensitive information.

## 🔧 Features
- 🧠 **AI Detection**: Trained YOLOv11n model to detect number plates with high accuracy.
- 🎯 **Automatic Blurring**: Detected plates are blurred instantly — no manual editing needed.
- 🌐 **Web Interface**: Built with Next.js for a clean, minimal frontend experience.
- ⚙️ **Flask API**: Serves the trained model and handles image processing in real-time.

## 🛠️ Tech Stack
- **Frontend**: Next.js
- **Backend**: Flask (Python)
- **Model Training**: YOLOv11n via Ultralytics + Google Colab
- **Dataset**: Custom-labeled using Roboflow

## 📦 Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/benwin-dev/licence-plate-blurring-app.git
cd number-plate-blur-app