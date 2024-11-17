import cv2
import os

# Definisci la cartella contenente i video da unire
input_folder = 'video_frame/video_to_join'

# Definisci il percorso e il nome del video di output
output_video_path = 'video_frame/video/Rip Currents.mp4'

# Definisci il codec e il VideoWriter per MP4
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_video_path, fourcc, 25.0, (640, 640))

# Ciclo attraverso i file nella cartella di input
for filename in os.listdir(input_folder):
    if filename.endswith('.mp4'):
        video_path = os.path.join(input_folder, filename)
        video = cv2.VideoCapture(video_path)

        while True:
            ret, frame = video.read()

            if not ret:
                break

            # Scrivi il frame nel video di output
            out.write(frame)


        video.release()

# Rilascia le risorse e chiudi i video
out.release()
