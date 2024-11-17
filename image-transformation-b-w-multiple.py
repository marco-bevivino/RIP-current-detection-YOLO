import os
import cv2

# Definisci la funzione per la conversione e il ridimensionamento delle immagini
def convert_resize_image(input_path, output_path):
    image = cv2.imread(input_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    resized_image = cv2.resize(gray_image, (640, 640))
    cv2.imwrite(output_path, resized_image)




# Percorso della cartella principale contenente le sottocartelle con le immagini
main_folder = 'C:/Users/VG User/Desktop/UNI/TESI/script modelli/Yolov8 custom/images/'

# Scorrere tutte le sottocartelle e le immagini al loro interno
for root, dirs, files in os.walk(main_folder):
    for file in files:
        if file.endswith('.JPG') or file.endswith('.jpeg') or file.endswith('.jpg') or file.endswith('.png'):
            input_path = os.path.join(root, file)
            print(input_path)
            output_path = os.path.join('C:/Users/VG User/Desktop/UNI/TESI/script modelli/Yolov8 custom/converted-images/', file)  # Definisci la cartella di output
            convert_resize_image(input_path, output_path)



