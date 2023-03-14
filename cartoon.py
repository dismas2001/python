#program to turn picture into a cartoon
import cv2
import numpy as np
image = cv2.imread("barrack.jpeg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

gray = cv2.median8lur(gray, 5)
edges = cv2.adaptiveThreshold(gray, 255,
                              cv2.ADAPTIVE_THRESH_MEAN_C,
                              cv2.THRESH_BINARY, 9, 9)

color = cv2.bilateralFilter(image, 9, 250, 250)
cartoon = cv2.bitwise_and(color, mask=edges)

cv2.imshow("image", image)
cv2.imshow("edges", edges)
cv2.imshow("cartoon", cartoon)
cv2.waitKey(0)
cv2.destroyALLWindows()
