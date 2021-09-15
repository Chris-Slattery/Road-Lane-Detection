import numpy as np
import cv2
import os
import time



#Function to find the Region of Interest.
#The Region of Interest function is used to focus on a particular area of the video in order to
#perform the hough transform algorithm and find the lines of the lanes in the road
def roi(img, vertices):
	mask = np.zeros_like(img)
	cv2.fillPoly(mask, vertices, 255)
	masked = cv2.bitwise_and(img, mask)
	return masked

#Function to process the video.
#This function reads in a video, converts the video to grayscale and performs canny edge detection
#The function also performs a gaussian blur. The Gaussian Blur is used to blur the lines which helps
#With reducing noise in the video.
#The function also performs the Hough Transform Algorithm after acquiring the vertices(Pixels)
#And the Region of Interest.
def process_video(frame):

	#Read in video and make it keep showing frames while its open
	video = cv2.VideoCapture('StayingInLane.avi')

	while True:
		ret, orig_frame = video.read()
		if not ret:
			video = cv2.VideoCapture('StayingInLane.avi')
			continue

		#Convert clip to grayscale
		frame = cv2.cvtColor(orig_frame, cv2.COLOR_BGR2GRAY)

		#Perform Canny on clip to find the edges
		edges = cv2.Canny(frame, 80, 180)

		#Perform a gaussian blur on clip to reduce noise
		edges = cv2.GaussianBlur(edges, (5, 5), 0)
		#Insert specified pixels into a numpy array
		vertices = np.array([[80,160],[300,40], [320,50], [360,50], [500,80], [600,150]], np.int32)

		#Get region of interest by calling function and passing edges and vertices
		position = roi(edges, [vertices])

		#Perform hough transform on clip to follow lines of the lanes in the road
		lines = cv2.HoughLinesP(position, 1, np.pi/180, 80, maxLineGap=5)
		#Loop through pixels and make pixels of road lane lines green.
		#The colour of the HSV values which are currently set to (0, 255, 0) can be changed 
		#To make the lanes a different colour. 
		if lines is not None:
			for line in lines:
				x1, y1, x2, y2 = line[0]
				cv2.line(orig_frame, (x1, y1), (x2, y2), (0, 255, 0), 5)
		#Show frames 
		cv2.imshow("Hough Transform/Annotated", orig_frame)
		cv2.imshow("Edge Detection", edges)
		cv2.imshow("Grayscale", frame)

		key = cv2.waitKey(25)
		if key == 27:
			break
	video.release()
	cv2.destroyAllWindows()

#Send the video to the prcoess video function to run program
edge = cv2.VideoCapture('StayingInLane.avi')
process_video(edge)