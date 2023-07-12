import cv2
import imutils
import numpy as np

# Wczytanie
img = cv2.imread("Lab7.png")

# Wyswietlenie i zapis
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.imwrite('Zapisany_obraz.png', img)

# Wycinek obrazu
roi = img[40:200, 250:420]
cv2.imshow("ROI", roi)
cv2.waitKey(0)

# Zmiana rozmiaru
resized = cv2.resize(img, (200, 200))
cv2.imshow("Fixed Resizing", resized)
cv2.waitKey(0)

# Obrot o 45 stopni
rotated = imutils.rotate(img, -45)
cv2.imshow("Imutils Rotation", rotated)
cv2.waitKey(0)

# Rozmycie i sklejenie
blurred = cv2.GaussianBlur(img, (11, 11), 0)
resized = imutils.resize(img, width=460)
bresized = imutils.resize(blurred, width=resized.shape[1])
suming = np.hstack((resized, bresized))
cv2.imshow("Blur", suming)
cv2.waitKey(0)

# Rysowanie prostokąta
output = img.copy()
cv2.rectangle(output, (270, 50), (420, 260), (0, 0, 255), 2)
cv2.imshow("Rectangle", output)
cv2.waitKey(0)

# Rysowanie linii
img = np.zeros((200, 200, 3), np.uint8)
cv2.line(img, (0, 0), (200, 200), (255, 0, 0), 5)
cv2.imshow("Line", img)
cv2.waitKey(0)

# Rysowanie linii łamanych przez kilka punktów
img = np.zeros((1000, 1000, 3), np.uint8)
points = np.array([[600, 200], [910, 641], [300, 300], [0, 0]])
cv2.polylines(img, np.int32([points]), 1, (255, 255, 255))
cv2.imshow("Line2", img)
cv2.waitKey(0)

# Rysowanie koła
img = np.zeros((200, 200, 3), np.uint8)
output = img.copy()
cv2.circle(output, (100, 100), 50, (0, 0, 255), 2)
cv2.imshow("Circle", output)
cv2.waitKey(0)

# Umieszczanie tekstu na obrazie
img = cv2.imread("Lab7.png")
font = cv2.FONT_HERSHEY_SIMPLEX
font1 = cv2.FONT_HERSHEY_COMPLEX
font2 = cv2.FONT_HERSHEY_SCRIPT_COMPLEX

cv2.putText(img, "Filip Urban", (1, 500), font, 4, (255, 255, 255), 2, cv2.LINE_4)
cv2.putText(img, "Filip Urban", (1, 300), font1, 4, (255, 255, 255), 2, cv2.LINE_4)
cv2.putText(img, "Filip Urban", (1, 100), font2, 4, (255, 255, 255), 2, cv2.LINE_4)
cv2.imshow("Text", img)
cv2.waitKey(0)
