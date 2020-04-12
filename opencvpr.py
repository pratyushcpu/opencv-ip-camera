import numpy as np 
import cv2

lowerBound = np.array([33,80,40])
upperBound = np.array([255,90,178])

camera = cv2.VideoCapture(0)

while True:
	ret, img = camera.read()
	img = cv2.resize(img,(500,500))

	imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

	cv2.imshow("camera", img)

	cv2.waitKey(1)