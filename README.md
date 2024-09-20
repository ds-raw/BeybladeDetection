# Beyblade Battle Detection
This Python script utilizes the YOLOv8 object detection model to track Beyblade battles from a video, analyze collisions, and determine the winner and loser based on spin detection. The process begins by loading the trained YOLOv8 model and a video file, where Beyblade movements are detected frame-by-frame. The model identifies the Beyblade objects, calculates spin status by comparing frame differences, and tracks collisions using bounding box overlap. Once one Beyblade stops spinning, the script identifies the winner, stores relevant information (such as battle duration, detected collisions, and detected object classes), and saves the final frames of the winner and loser. Results are logged in a CSV file for further analysis.

Additionally, the script integrates with a Telegram bot, sending battle results, including a summary, images of the winner, loser, and the last condition, as well as the CSV file. The script employs asynchronous communication with Telegram, ensuring that all results are sent after the battle analysis completes.

Key features include:

Object detection with YOLOv8: Identifies Beyblades and tracks their status (spinning or stopped).
Collision detection: Tracks the number of Beyblade collisions during the battle using bounding box overlap.
Spin status analysis: Detects the stopping of Beyblades by calculating frame differences between consecutive video frames.
Telegram integration: Automatically sends battle results, images, and CSV files via a Telegram bot.
Battle outcome detection: Determines the winner when one Beyblade stops spinning.
The script effectively combines object detection, video processing, and asynchronous messaging for a comprehensive Beyblade battle tracking system.

How to Access and Run the Code
Prerequisites
Before running the code, ensure you have the following dependencies installed:

Python 3.x
OpenCV (pip install opencv-python)
Ultralytics YOLOv8 library (pip install ultralytics)
NumPy (pip install numpy)
Pandas (pip install pandas)
Python Telegram Bot (pip install python-telegram-bot)
asyncio (comes built-in with Python 3.x)
