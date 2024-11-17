import cv2
import os 

# Apre il video
video = cv2.VideoCapture('video/IMG_1976.mp4')

# Definisci il percorso della cartella in cui desideri salvare il video in scala di grigi
output_folder = 'converted-videos/'

# Assicurati che la cartella esista, altrimenti creala
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Controlla se il video è stato aperto correttamente
if not video.isOpened():
    print("Errore nell'apertura del video.")
    exit()

# Crea un video writer per salvare il video in scala di grigi
fps = int(video.get(cv2.CAP_PROP_FPS))
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(os.path.join(output_folder, 'video_in_grigio.avi'), fourcc, fps, (width, height), isColor=False)

while True:
    ret, frame = video.read()

    if not ret:
        break

    # Converte il frame in scala di grigi
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Scrive il frame in scala di grigi nel video di output
    out.write(gray_frame)

    cv2.imshow('Video in Scala di Grigi', gray_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
out.release()
cv2.destroyAllWindows()