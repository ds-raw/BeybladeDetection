# 🌀 Beyblade Battle Tracker with YOLOv8 and Telegram Integration 🚀

This Python script is designed to analyze Beyblade battles from a video using the YOLOv8 object detection model. It tracks the movements of the Beyblades, detects collisions, and determines the winner and loser based on their spinning status. Here’s how it works:

🛠️ How It Works:
Load the YOLOv8 Model 🧠:

The trained model is used to identify Beyblades in the video, detecting their movements frame-by-frame.
Track Beyblades in Real-Time 📹:

The script tracks multiple Beyblades, analyzing their position and calculating their spin status.
Collision Detection ⚡:

The script detects Beyblade collisions using bounding box overlap and counts the number of times they collide.
Spin Status 🔄:

The Beyblade's spinning status is determined by calculating the difference between consecutive video frames. When one Beyblade stops spinning, the script identifies it as the loser.
Battle Outcome 🏆:

The battle ends when one Beyblade stops spinning. The script captures the moment, stores battle details (winner, loser, and duration), and saves images of the final result.
Telegram Bot Integration 🤖:

After the battle, the results (including a CSV file, summary, and images of the winner and loser) are automatically sent via a Telegram bot to a specified chat.
Ultralytics YOLOv8 library (pip install ultralytics)
NumPy (pip install numpy)
Pandas (pip install pandas)
Python Telegram Bot (pip install python-telegram-bot)
asyncio (comes built-in with Python 3.x)
