import cv2
import numpy
import numpy as np
import imutils

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
scaling_factor = 0.5
frame = cv2.imread("faces.png")
gray_filter = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

if frame.shape[0] > 0 and frame.shape[1] > 0:
    frame = cv2.resize(frame, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)

else:
    print("Empty image or invalid dimensions.")

face_rects = face_cascade.detectMultiScale(frame, scaleFactor=1.3, minNeighbors=5)

for (x, y, w, h) in face_rects:
    cv2.rectangle(frame, (x, y), (x + w, y + h), (250, 0, 0), 3)
    roi_gray = gray_filter[y:y + h, x:x + w]
    roi_color = frame[y:y + h, x:x + w]
    smile = smile_cascade.detectMultiScale(roi_gray)
    eye = eye_cascade.detectMultiScale(roi_gray)
    for (sx, sy, sw, sh) in smile:
        cv2.rectangle(roi_color, (sx, sy), (sx + sw, sy + sh), (0, 255, 0), 1)
    for (ex, ey, ew, eh) in eye:
        cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 0, 255), 1)

cv2.imshow("Picture", frame)
cv2.waitKey(0)
print(f'Found {len(face_rects)} faces!')

# Zliczanie osob na zdjeciu

scaling_factor = 0.5
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
image = cv2.imread("test2.png")

if image.shape[0] > 0 and image.shape[1] > 0:
    image = cv2.resize(image, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)

else:
    print("Empty image or invalid dimensions.")

people_rects = hog.detectMultiScale(image, winStride=(8, 8), padding=(30, 30), scale=1.06)

for (x, y, w, h) in people_rects[0]:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow("X--men", image)
cv2.waitKey(0)
print(f'Found {len(people_rects[0])} people!')

# Wideo

cv2.startWindowThread()
cap = cv2.VideoCapture("video2.mp4")

while True:
    ret, frame = cap.read()

    frame = cv2.resize(frame, (800, 560))
    gray_filter = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    boxes, weigts = hog.detectMultiScale(frame, winStride=(8, 8))
    boxes = numpy.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])

    for (xa, ya, xb, yb) in boxes:
        cv2.rectangle(frame, (xa, ya), (xb, yb), (0, 255, 0), 1)
    cv2.imshow("Video", frame)
    if (cv2.waitKey(1) & 0XFF == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()
