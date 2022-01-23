import cv2
import numpy as np 

img = cv2.imread("shapes.png")
img2 = img.copy()

# 그레이 스케일 변환 / 스레시홀드로 바이너리이미지, 검은색 배경에 흰색 전경 변환 
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, imthres = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY_INV)

# 가장 바깥쪽 컨투어에 대한 꼭짓점 좌표만 변환 
contour, hierarchy = cv2.findContours(imthres, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#외각선 검출 
cv2.drawContours(img2, contour, -1, (0,255,0), 4)

#꼭짓점 검출 
for i in contour:
    for j in i:
        cv2.circle(img2, tuple(j[0]), 1, (255,0,0), -1)

cv2.imshow("contour", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
