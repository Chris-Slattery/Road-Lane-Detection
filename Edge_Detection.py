import numpy as np
import cv2
import os
import time



def edge_detection(edge):
	cap = cv2.VideoCapture('StayingInLane.avi')

	while(1):
		ret, frame = cap.read()

		if not ret:
			break

		#Convert BGR to HSV
		hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

		#Define the raneg fo the red color in HSV
		lower_red = np.array([30,150,50])
		upper_red = np.array([255,255,180])

		#Create a red HSV olor boundary and threshold HSV image
		mask = cv2.inRange(hsv, lower_red, upper_red)

		#Bitwise and mask the original image
		res = cv2.bitwise_and(frame,frame, mask=mask)

		#Convert to grayscale
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		#Display original image
		cv2.imshow('Original', gray)

		#Find edges in the input image and mark them in ouput map edges
		edges = cv2.Canny(frame, 100,200)

		#Display images in a frame
		cv2.imshow('Edges', edges)

		#Wait for ESc key to stop
		k = cv2.waitKey(40) & 0xFF
		if k == 27:
			break
	#Close the window		
	cap.release()

	#De-allocate any associated memory usage
	cv2.destroyAllWindows()


edge = cv2.VideoCapture('StayingInLane.avi')
edge_detection(edge)
