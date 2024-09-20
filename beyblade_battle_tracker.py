import cv2
from ultralytics import YOLO
import numpy as np
import pandas as pd
from telegram import Bot, InputFile
import asyncio

# Initialize YOLOv8 model
model = YOLO("best.pt")
names = model.names

# Open the video file
video_path = r"your video"
cap = cv2.VideoCapture(video_path)

# Get video properties
fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
total_video_time = total_frames / fps  # Total video time in seconds

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc('F', 'M', 'P', '4')
output_path = "output_video.avi"
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

battle_start = False
start_time = None
prev_frame_gray = None
winner_out_path = None
loser_out_path = None
reason = None
collision_count = 0  # To track the number of collisions
frame_diff_threshold = 1  # Threshold for frame difference to detect stopped spinning

# Define region size for movement detection
region_size = 1  # Size of the region around the Beyblade for movement detection

# Initialize detected classes dictionary
detected_classes = {}

def check_battle(results):
    global battle_start, start_time, detected_classes
    classes = {}
    for r in results:
        for c in r.boxes.cls:
            name = names[int(c)]
            if name in classes:
                classes[name] += 1
            else:
                classes[name] = 1
    detected_classes = classes  # Store detected classes
    print("Detected classes:", detected_classes)  # Debugging line
    if classes.get('Beyblade', 0) >= 2:
        if start_time is None:  # Ensure start_time is only set once
            start_time = cap.get(cv2.CAP_PROP_POS_MSEC)
            battle_start = True
            print('Battle started at:', start_time)

def check_spin_status_by_frame_diff(results, prev_frame, frame, min_movement=30):
    spin_status = {}
    beyblade_positions = []

    for r in results:
        for c in r.boxes.cls:
            name = names[int(c)]
            if name == 'Beyblade':
                box = r.boxes.xyxy
                for b in box:
                    x1, y1, x2, y2 = b.tolist()
                    xc = round((x1 + x2) / 2)
                    yc = round((y1 + y2) / 2)
                    beyblade_positions.append((xc, yc))  # Store positions for checking frame difference
                    spin_status[(xc, yc)] = {
                        'x1': x1,
                        'y1': y1,
                        'x2': x2,
                        'y2': y2,
                        'status': 'spinning'
                    }

    if prev_frame is not None:
        # Convert frames to grayscale
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        prev_frame_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)

        # Calculate absolute difference between the current frame and the previous frame
        frame_diff = cv2.absdiff(frame_gray, prev_frame_gray)

        for pos, beyblade_info in spin_status.items():
            # Get the Beyblade region in the frame difference image
            x_min = max(0, int(beyblade_info['x1']))
            x_max = min(frame_diff.shape[1], int(beyblade_info['x2']))
            y_min = max(0, int(beyblade_info['y1']))
            y_max = min(frame_diff.shape[0], int(beyblade_info['y2']))

            # Calculate the mean difference in the Beyblade region
            region_diff = np.mean(frame_diff[y_min:y_max, x_min:x_max])

            # If the difference is below the threshold, mark the Beyblade as stopped
            if region_diff < frame_diff_threshold:
                spin_status[pos]['status'] = 'stopped'

    return spin_status

def detect_collisions(bboxes, area_threshold=0.5):
    global collision_count
    num_boxes = len(bboxes)
    for i in range(num_boxes):
        for j in range(i + 1, num_boxes):
            bbox1 = bboxes[i]
            bbox2 = bboxes[j]
            if is_collision(bbox1, bbox2, area_threshold):
                collision_count += 1

def is_collision(bbox1, bbox2, area_threshold):
    # Unpack bounding boxes
    x1_min, y1_min, x1_max, y1_max = bbox1
    x2_min, y2_min, x2_max, y2_max = bbox2

    # Calculate overlap area
    x_overlap = max(0, min(x1_max, x2_max) - max(x1_min, x2_min))
    y_overlap = max(0, min(y1_max, y2_max) - max(y1_min, y2_min))
    overlap_area = x_overlap * y_overlap

    # Calculate the area of the bounding boxes
    area1 = (x1_max - x1_min) * (y1_max - y1_min)
    area2 = (x2_max - x2_min) * (y2_max - y2_min)

    # Calculate overlap ratio
    overlap_ratio = overlap_area / min(area1, area2)

    # Check if overlap ratio exceeds threshold
    return overlap_ratio > area_threshold

async def send_telegram_results():
    # Telegram bot setup
    TELEGRAM_API_TOKEN = 'your telegram api'
    CHAT_ID = 'your chat id'
    bot = Bot(token=TELEGRAM_API_TOKEN)

    # Prepare the results message
    message_text = "Beyblade Battle Results:\n"


    message_text += f"Total Video Time: {total_video_time:.2f} seconds\n"

    if reason:
        message_text += f"Reason for outcome: {reason}\n"

    message_text += f"Total Collisions: {collision_count}\n"

    if detected_classes:
        message_text += f"Detected Classes: {detected_classes}\n"

    # Send results message via Telegram
    await bot.send_message(chat_id=CHAT_ID, text=message_text)

    # Send images
    if winner_out_path:
        message_text += f"The Winner"
        with open(winner_out_path, 'rb') as f:
            await bot.send_photo(chat_id=CHAT_ID, photo=InputFile(f, filename=winner_out_path))
            

    if loser_out_path:
        message_text += f"The Loser"
        with open(loser_out_path, 'rb') as f:
            await bot.send_photo(chat_id=CHAT_ID, photo=InputFile(f, filename=loser_out_path))
            

    if 'kondisi_terakhir.jpg':
        message_text += f"Last Condition"
        with open('kondisi_terakhir.jpg', 'rb') as f:
            await bot.send_photo(chat_id=CHAT_ID, photo=InputFile(f, filename='kondisi_terakhir.jpg'))
            

    # Send CSV file
    with open('battle_result.csv', 'rb') as f:
        await bot.send_document(chat_id=CHAT_ID, document=InputFile(f, filename='battle_result.csv'))

    await bot.close()

while cap.isOpened():
    success, frame = cap.read()

    if success:
        results = model.track(frame, verbose=False, tracker='botsort.yaml')
        annotated_frame = results[0].plot()

        # Extract bounding boxes for collision detection
        bboxes = []
        for r in results:
            for c in r.boxes.cls:
                name = names[int(c)]
                if name == 'Beyblade':
                    box = r.boxes.xyxy
                    for b in box:
                        x1, y1, x2, y2 = b.tolist()
                        bboxes.append([x1, y1, x2, y2])

        # Detect collisions
        detect_collisions(bboxes)

        if not battle_start:
            check_battle(results)
        else:
            spin_status = check_spin_status_by_frame_diff(results, prev_frame_gray, frame)

            beyblades_spinning = [status for status in spin_status.values() if status['status'] == 'spinning']
            beyblades_stopped = [status for status in spin_status.values() if status['status'] == 'stopped']

            if len(beyblades_stopped) > 0 and len(beyblades_spinning) == 1:
                winner = beyblades_spinning[0]
                loser = beyblades_stopped[0]
                winner_out_path = 'the winner.jpg'
                loser_out_path = 'the loser.jpg'
                frame_win = frame[int(winner['y1']):int(winner['y2']), int(winner['x1']):int(winner['x2'])]
                frame_lose = frame[int(loser['y1']):int(loser['y2']), int(loser['x1']):int(loser['x2'])]
                cv2.imwrite(winner_out_path, frame_win)
                cv2.imwrite(loser_out_path, frame_lose)
                reason = 'Opponent stopped spinning'
                cv2.imwrite('last condition.jpg', frame)
                break

        prev_frame_gray = frame  # Update previous frame for next iteration
        cv2.imshow("YOLOv8 Tracking", annotated_frame)
        out.write(annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

# Store results in a DataFrame
data = {
    'battle_time': (cap.get(cv2.CAP_PROP_POS_MSEC) - start_time) / 1000 if start_time else 0,
    'total_video_time': total_video_time,  # Added total video time
    'winner': winner_out_path,
    'loser': loser_out_path,
    'reason': reason,
    'collisions': collision_count,  # Store the number of collisions in the CSV
    'detected_classes': str(detected_classes)  # Store the detected classes in the CSV
}

index = ['Battle Data']
df = pd.DataFrame(data, index=index)

cap.release()
cv2.destroyAllWindows()
df.to_csv('battle_result.csv', index=False)

# Run the asynchronous Telegram function
loop = asyncio.get_event_loop()
if loop.is_running():
    loop.create_task(send_telegram_results())
else:
    asyncio.run(send_telegram_results())
