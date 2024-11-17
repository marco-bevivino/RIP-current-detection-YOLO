import cv2
import os

# Definisci il percorso del video
video_name = 'RIPOFF11'
video_path = f'video_frame/video/{video_name}.mkv'

# Definisci la cartella in cui salvare i frame estratti
output_folder = 'video_frame/frame/'
os.makedirs(output_folder, exist_ok=True)

# Apri il video
cap = cv2.VideoCapture(video_path)
frame_rate = cap.get(cv2.CAP_PROP_FPS)

# Inizializza variabili
frame_count = 0
success = True

while success:
    # Leggi il frame corrente
    success, frame = cap.read()

    # Calcola il tempo corrente in secondi
    current_time = cap.get(cv2.CAP_PROP_POS_MSEC) / 1000

    # Estrai un frame ogni 10 secondi
    if frame_count % (frame_rate * 5) == 0:
        # Salva il frame estratto nella cartella specificata
        frame_name = f'{output_folder}/{video_name}{int(current_time)}.jpg'
        cv2.imwrite(frame_name, frame)
        print(f'Frame salvato: {frame_name}')

    frame_count += 1

# Rilascia le risorse e chiudi il video
cap.release()
cv2.destroyAllWindows()