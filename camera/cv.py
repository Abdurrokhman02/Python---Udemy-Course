import cv2

img = cv2.imread('image.jpg')

cv2.imshow('Gambar', img)
cv2.waitKey(0) 
cv2.destroyAllWindows()