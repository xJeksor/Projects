import cv2
import numpy as np

cap = cv2.VideoCapture("video.mp4")

if cap.isOpened() == False:
    print("Error opening video stream or file")

frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
print(frames)
frames = 0

cv2.namedWindow("sum", cv2.WINDOW_NORMAL)
cv2.resizeWindow("sum", 800, 600)

while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
        frames += 1

        gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blur_kernel_size = (5, 5)
        blur_img = cv2.GaussianBlur(gray_img, blur_kernel_size, 0)
        canny_low_threshold = 20
        canny_high_threshold = 100
        canny_img = cv2.Canny(blur_img, canny_low_threshold, canny_high_threshold)
        height, width = canny_img.shape[:2]
        h = height // 2
        w = width
        x = height // 2
        y = 0

        img1 = canny_img[x: x + h, y: y + w]
        # cv2.imshow("img1", canny_img)
        img2 = np.zeros_like(canny_img)
        img2[x: x + h, y: y + w] = img1

        src = img2

        dst = cv2.Canny(src, 50, 200, None, 3)
        cdst = cv2.cvtColor(dst, cv2.COLOR_GRAY2BGR)
        cdstP = np.copy(cdst)
        lines = cv2.HoughLines(dst, 1, np.pi / 180, 150, None, 0, 0)
        if lines is not None:
            for i in range(0, len(lines)):
                rho = lines[i][0][0]
                theta = lines[i][0][1]
                a = np.cos(theta)
                b = np.sin(theta)
                x0 = a * rho
                y0 = b * rho
                pt1 = (int(x0 + 1000 * (-b)), int(y0 + 1000 * (a)))
                pt2 = (int(x0 - 1000 * (-b)), int(y0 - 1000 * (a)))
                cv2.line(cdst, pt1, pt2, (0, 0, 255), 3, cv2.LINE_AA)
        linesP = cv2.HoughLinesP(dst, 1, np.pi / 180, 50, None, 50, 10)
        if linesP is not None:
            for i in range(0, len(linesP)):
                l = linesP[i][0]
                cv2.line(cdstP, (l[0], l[1]), (l[2], l[3]), (0, 0, 255), 3, cv2.LINE_AA)
        img2 = cv2.addWeighted(frame, 0.8, cdstP, 1, 0)

        font = cv2.FONT_HERSHEY_SIMPLEX
        bottomLeftCornerOfText = (width - 300, height - 10)
        fontScale = 1
        fontColor = (255, 255, 255)
        lineType = 2
        cv2.putText(
            img2,
            "Filip Urban",
            bottomLeftCornerOfText,
            font,
            fontScale,
            fontColor,
            lineType,
        )
        cv2.imshow("sum", img2)

        if cv2.waitKey(25) & 0xFF == ord("q"):
            break
    else:
        break

print(frames)
cap.release()
cv2.destroyAllWindows()
