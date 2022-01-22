import cv2
import numpy as np

img = cv2.imread("paper.jpg")

blur = cv2.GaussianBlur(img, (3,3), 0)
edge = cv2.Laplacian(blur, -1)

merged = np.hstack((img, blur, edge))

cv2.imshow('Laplacian', merged)
cv2.waitKey(0)
cv2.destroyAllWindows()