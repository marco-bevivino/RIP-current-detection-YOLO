import cv2
from ultralytics import YOLO

# Load the YOLOv8 model
model = YOLO('Custom_models\Yolov8s_datasetV1_noAug.pt')

# Open the video file
video_path = "video/IMG_1976.mp4"
cap = cv2.VideoCapture(video_path)

# Get video properties (frame width, frame height, and frame rate)
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame_rate = int(cap.get(cv2.CAP_PROP_FPS))

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_video_path = "output/video_result.mp4"
out = cv2.VideoWriter(output_video_path, fourcc, frame_rate, (frame_width, frame_height))

# Loop through the video frames
while cap.isOpened():
    success, frame = cap.read()

    if success:
        # Run YOLOv8 inference on the frame, conf=0.25
        results = model(frame, conf=0.25)

        # Get the annotated frame
        annotated_frame = results[0].plot()

        # Write the annotated frame to the output video
        out.write(annotated_frame)

        # Display the annotated frame
        cv2.imshow("YOLOv8 Inference", annotated_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

# Release the video capture and writer objects
cap.release()
out.release()
cv2.destroyAllWindows()
