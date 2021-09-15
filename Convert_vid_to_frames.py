import numpy as np
import cv2
import os
import time


def video_to_frames(input_loc, output_loc):
	try:
		os.mkdir(output_loc)
	except OSError:
		pass
	#Log the time
	time_start = time.time()
	#Start capturing feed
	cap = cv2.VideoCapture(input_loc)
	#Find the number of frames
	video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
	print("Number of Frames: ", video_length)
	count = 0
	print("Converting Video...\n")
	#Start converting video
	while cap.isOpened():
		ret, frame = cap.read()
		cv2.imwrite(output_loc + "/%#05d.jpg" % (count+1), frame)
		count = count + 1
		#If there are no frames left
		if (count > (video_length-1)):
			time_end = time.time()
			cap.release()
			print("Done extracting frames")
			break




if __name__=="__main__":

	input_loc = "C:\\Users\\chris\\Desktop\\College Backup\\Semester 2\\Computer Vision\\Assignment2\\StayingInLane.avi"
	output_loc = "C:\\Users\\chris\\Desktop\\College Backup\\Semester 2\\Computer Vision\\Assignment2\\Images"
	video_to_frames(input_loc, output_loc)