# 🌀 Beyblade Battle Tracker with YOLOv8 and Telegram Integration 🚀

This Python script is designed to analyze Beyblade battles from a video using the YOLOv8 object detection model. It tracks the movements of the Beyblades, detects collisions, and determines the winner and loser based on their spinning status. Here’s how it works:

🛠️ How It Works:
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

✨ Key Features:
- Object Detection with YOLOv8: Automatically detects Beyblades in real-time 🎯.
- Collision Detection: Counts the number of collisions during the battle ⚔️.
- Spin Status Analysis: Detects the spinning and stopping of Beyblades by comparing video frames 🔍.
- Telegram Bot Notifications: Sends results, images, and CSV files directly to your Telegram 📩.
- Battle Outcome Detection: Determines the winner and saves all relevant information 🏅.
