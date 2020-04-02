# 安装包的方法：https://pypi.org/project/opencv-python/
import cv2

img = cv2.imread("luoyonghao.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 3)
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 7, 7)

cv2.imwrite("./output_luoyonghao.jpg", edges)
