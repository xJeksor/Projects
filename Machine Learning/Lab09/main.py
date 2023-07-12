import cv2
import numpy as np

img = cv2.imread("img.jpg")

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray image", gray_img)
cv2.imwrite("gray_img.jpg", gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

blur_kernel_size = (15, 15)
gray_img = cv2.imread("gray_img.jpg")
blur_img = cv2.GaussianBlur(gray_img, blur_kernel_size, 0)
cv2.imshow("blur image", blur_img)
cv2.imwrite("blur_img.jpg", blur_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

canny_low_threshold = 20
canny_high_threshold = 100
blur_img = cv2.imread("blur_img.jpg")
canny_img = cv2.Canny(blur_img, canny_low_threshold, canny_high_threshold)
cv2.imshow("canny image", canny_img)
cv2.imwrite("canny_img.jpg", canny_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

img = cv2.imread("canny_img.jpg", 0)
height, width = canny_img.shape[:2]
print(height, width)
h = height // 2
w = width
x = height // 2
y = 0
img1 = img[x : x + h, y : y + w]
img2 = np.zeros_like(img)
img2[x : x + h, y : y + w] = img1


cv2.imshow("img2", img2)
cv2.imwrite("img2.jpg", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()


src = cv2.imread("img2.jpg")

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
        pt1 = (
            int(x0 + 1000 * (-b)),
            int(y0 + 1000 * (a)),
        )
        pt2 = (
            int(x0 - 1000 * (-b)),
            int(y0 - 1000 * (a)),
        )
        cv2.line(cdst, pt1, pt2, (0, 0, 255), 3, cv2.LINE_AA)
linesP = cv2.HoughLinesP(dst, 1, np.pi / 180, 50, None, 50, 10)
if linesP is not None:
    for i in range(0, len(linesP)):
        l = linesP[i][0]
        cv2.line(cdstP, (l[0], l[1]), (l[2], l[3]), (0, 0, 255), 3, cv2.LINE_AA)
# cv2.imshow("Detected Lines (in red) - Standard Hough Line Transform", cdst)
cv2.imshow("Detected Lines (in red) - Probabilistic Line Transform", cdstP)
cv2.imwrite("detected.jpg", cdstP)
cv2.waitKey()
cv2.destroyAllWindows()

img = cv2.imread("img.jpg")
img1 = cv2.imread("detected.jpg")
img2 = cv2.addWeighted(img, 0.8, img1, 1, 0)
cv2.imshow("sum", img2)
cv2.imwrite("sum.jpg", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
