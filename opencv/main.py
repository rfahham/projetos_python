# pip3 install opencv-python

import cv2 as cv
img = cv.imread("spacex-768x512.jpg")

cv.imshow("Display window", img)
# Wait for a keystroke in the window
k = cv.waitKey(0) 