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
   
### Video Link
- Original Video: https://www.youtube.com/watch?v=CIfr5618vy4&list=LL&index=4
- Input and Output: https://drive.google.com/drive/folders/1zOgJol-a_ubczUyk778LkNgznrWZ601m
  
## ✨ Key Features:
- Object Detection with YOLOv8: Automatically detects Beyblades in real-time 🎯.
- Collision Detection: Counts the number of collisions during the battle ⚔️.
- Spin Status Analysis: Detects the spinning and stopping of Beyblades by comparing video frames 🔍.
- Multi-Object Tracking with BoT-SORT: Tracks each Beyblade's movement throughout the battle and maintains their unique identities using BoT-SORT, a tracker combining bounding box overlap with ReID (Re Identification) features for consistent tracking across frames 🔄.
- Telegram Bot Notifications: Sends results, images, and CSV files directly to your Telegram 📩.
- Battle Outcome Detection: Determines the winner and saves all relevant information 🏅.

## 🛠️ Logic Behind Detecting a Stopped Beyblade 🔍
To determine whether a Beyblade has stopped spinning, the script employs a technique that involves comparing consecutive frames from the video (Motion Detection using Frame Differencing) and uses BoT-SORT to track individual Beyblades. Here’s how it works step by step:
1. Multi-Object Tracking with BoT-SORT: The script uses BoT-SORT to track each detected Beyblade across frames, leveraging both bounding box overlap and Re-Identification (ReID) features to maintain consistent identities, even in cases of occlusion or fast movement.
2. Capture Video Frames 🎥:
   The video is processed frame by frame, allowing the model to analyze the position and status of the Beyblades in real-time.
3. Convert Frames to Grayscale ⚪:
   - For each frame, the script converts the image from color to grayscale.
   - This simplifies the comparison process by reducing the amount of information that needs to be analyzed.
4. Calculate Frame Differences ➖:
   - The script calculates the absolute difference between the current frame and the previous frame using the OpenCV function cv2.absdiff().
   - This highlights areas where changes occur, such as movement or lack of movement.
5. Analyze the Beyblade Regions 📏:
   - For each detected Beyblade, the script identifies its bounding box (the area surrounding it). It focuses on this region in the difference image to assess movement.
   - The bounding box coordinates are used to extract the relevant area from the difference image.
6. Compute the Mean Difference 📊:
   - The script calculates the mean pixel intensity difference within the Beyblade’s bounding box in the difference image. A low mean difference indicates that there has been little to no movement in that region.
7. Set a Threshold for Movement ⚖️:
   A predefined threshold (e.g., frame_diff_threshold) is set to determine what constitutes significant movement. If the mean difference is below this threshold, the Beyblade is considered to have stopped spinning.
8. Update Spin Status 🔄:
   Based on the analysis, the Beyblade's status is updated to either "spinning" or "stopped." This status is maintained throughout the video processing loop.
9. Trigger Outcome Logic 🏁:
   Once a Beyblade is detected as "stopped" and there is only one other Beyblade still "spinning," the script concludes the battle and identifies the winner and loser.


## 🚀 How to Access and Run the Beyblade Battle Tracker 🌀
🛠️ Prerequisites
Before diving in, make sure you have the following installed:
- Python 3.x (Get it here)
- Required libraries (install them via terminal) "pip install opencv-python ultralytics numpy pandas python-telegram-bot"

## 📥 Setup Guide
1. Upload Your Dataset to Roboflow 📤:
   - Create a Roboflow account and log in.
   - Upload your Beyblade images or video frames to create a new project.
2. Annotate the Dataset Using Roboflow ✏️:
   - Use the annotation tools provided by Roboflow to label your Beyblade objects (e.g., "Beyblade").
   - Once done, save your annotations.
3. Download the Annotated Dataset 📥:
   - After annotation, download the dataset in the YOLO format.
   - This will typically include your images and a corresponding set of annotation files.
4. Train the Dataset 🏋️‍♂️:
   - Use the downloaded dataset to train your YOLOv8 model.
   - Follow the specific training instructions from the YOLO documentation or Roboflow to create your custom model.
5. Clone the Repository:
   - Download the project files:
   - git clone https://github.com/your-username/your-repository-name.git
   - cd your-repository-name
6. Place Your Trained YOLO Model:
   - Save your trained YOLOv8 model (e.g., best.pt) in the project folder, or update the path in the code:
   - model = YOLO(r"C:\path\to\your\best.pt")
7. Prepare Your Battle Video:
   - Add your Beyblade battle video. Ensure the path is correct
   - video_path = r"C:\path\to\your\beyblade_battle.mp4"
8. Set Up Your Telegram Bot:
   - Create a Telegram bot using BotFather and get your API token.
   - Update the script with your token and chat ID:
   - TELEGRAM_API_TOKEN = 'your-telegram-bot-token'
   - CHAT_ID = 'your-chat-id'
   - *using env to secure your API
## ▶️ Running the Script
Once everything is set up:
1. Open Terminal:
   Open your terminal (or command prompt) in the project folder.
2. Run the Script:
   Start the Beyblade battle analysis:
   python beyblade_battle_tracker.py
3. Enjoy the Show! 🎉
   - The script will process the video, track Beyblades, detect collisions, and determine the winner and loser.
   - Results, including a summary, images, and a CSV file, will be sent to your Telegram chat automatically.
## 📊 What You Get
- Results in Telegram: You'll receive:
  - A battle summary message 📜
  - Images of the winner 🏆 and loser ❌
  - The battle data in a CSV file 📈
- Local Files: A CSV file (battle_result.csv) and images will be saved in the project folder.
## 📊 Model Summary Results:
- Model Architecture:
  - Layers: 168
  - Parameters: 11,126,358
  - Gradients: 0
  - GFLOPs: 28.4
- Overall Performance:
  - Total Images: 39
  - Total Instances: 78
  - Box Precision (P): 0.944
  - Recall (R): 0.864
  - Mean Average Precision at IoU=0.50 (mAP50): 0.936
  - Mean Average Precision at IoU=0.50 to 0.95 (mAP50-95): 0.69
- Class-Specific Performance:
  - Beyblade:
    - Images: 35
    - Instances: 67
    - Precision: 1.000
    - Recall: 1.000
    - mAP50: 0.995
    - mAP50-95: 0.879
   - Hand:
     - Images: 7
     - Instances: 11
     - Precision: 0.888
     - Recall: 0.727
     - mAP50: 0.876
     - mAP50-95: 0.500


