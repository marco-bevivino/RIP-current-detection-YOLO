# import opencv 
import cv2 

# Load the input image 
image = cv2.imread('images\IMG_1985.JPG') 

# Ridimensiona l'immagine in 640x640
resized_image = cv2.resize(image, (640, 640))


cv2.imshow('Original', resized_image) 
cv2.waitKey(0) 

# Use the cvtColor() function to grayscale the image 
gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY) 

cv2.imshow('Grayscale', gray_image) 
cv2.waitKey(0) 


(thresh, binary) = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)


cv2.imshow('Black and white', binary) 
cv2.waitKey(0)


# Window shown waits for any key pressing event 
cv2.destroyAllWindows()




