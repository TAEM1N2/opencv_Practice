import cv2
import numpy as np

img = cv2.imread("paper.jpg")

blur = cv2.GaussianBlur(img, (3,3), 0)
cv2.imshow('gaussian blur', blur)
cv2.waitKey(0)
cv2.destroyAllWindows()