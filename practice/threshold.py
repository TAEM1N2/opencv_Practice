import cv2
import numpy as np 

img = cv2.imread("paper.jpg")
ret, imthres = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)