# 🌀 Beyblade Battle Tracker with YOLOv8 and Telegram Integration 🚀

This Python script is designed to analyze Beyblade battles from a video using the YOLOv8 object detection model. It tracks the movements of the Beyblades, detects collisions, and determines the winner and loser based on their spinning status. Here’s how it works:

## 🛠️ How It Works:
1. Load the YOLOv8 Model 🧠:
   The trained model is used to identify Beyblades in the video, detecting their movements frame-by-frame.
2. Track Beyblades in Real-Time 📹:
   The script tracks multiple Beyblades, analyzing their position and calculating their spin status.
3. Collision Detection ⚡:
   The script detects Beyblade collisions using bounding box overlap and counts the number of times they collide.
4. Spin Status 🔄:
   The Beyblade's spinning status is determined by calculating the difference between consecutive video frames. When one Beyblade stops spinning, the script identifies it as the loser.
5. Battle Outcome 🏆:
   The battle ends when one Beyblade stops spinning. The script captures the moment, stores battle details (winner, loser, and duration), and saves images of the final result.
6. Telegram Bot Integration 🤖:
   After the battle, the results (including a CSV file, summary, and images of the winner and loser) are automatically sent via a Telegram bot to a specified chat.

# ✨ Key Features:
- Object Detection with YOLOv8: Automatically detects Beyblades in real-time 🎯.
- Collision Detection: Counts the number of collisions during the battle ⚔️.
- Spin Status Analysis: Detects the spinning and stopping of Beyblades by comparing video frames 🔍.
- Telegram Bot Notifications: Sends results, images, and CSV files directly to your Telegram 📩.
- Battle Outcome Detection: Determines the winner and saves all relevant information 🏅.

# 🚀 How to Access and Run the Beyblade Battle Tracker 🌀
🛠️ Prerequisites
Before diving in, make sure you have the following installed:
- Python 3.x (Get it here)
- Required libraries (install them via terminal) "pip install opencv-python ultralytics numpy pandas python-telegram-bot"

# 📥 Setup Guide
1. Upload Your Dataset to Roboflow 📤:
   Create a Roboflow account and log in.
2. Upload your Beyblade images or video frames to create a new project.
3. Annotate the Dataset Using Roboflow ✏️:
   - Use the annotation tools provided by Roboflow to label your Beyblade objects (e.g., "Beyblade").
   - Once done, save your annotations.
4. Download the Annotated Dataset 📥:
   - After annotation, download the dataset in the YOLO format.
   - This will typically include your images and a corresponding set of annotation files.
5. Train the Dataset 🏋️‍♂️:
   - Use the downloaded dataset to train your YOLOv8 model.
   - Follow the specific training instructions from the YOLO documentation or Roboflow to create your custom model.
6. Clone the Repository:
   Download the project files: 
