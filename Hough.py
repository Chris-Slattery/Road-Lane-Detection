import cv2
import numpy as np


def hough_transform(frame):
    video = cv2.VideoCapture('StayingInLane.avi')
 
    while True:
        ret, orig_frame = video.read()
        if not ret:
            video = cv2.VideoCapture("StayingInLane.avi")
            continue

        hsv = cv2.cvtColor(orig_frame, cv2.COLOR_BGR2HSV)
        hsv = cv2.Canny(hsv, 25, 50)
        hsv = cv2.GaussianBlur(hsv, (3, 3), 0)
        vertices = np.array([[50,40],[30,60], [60,255], [50,70], [220,240], [40,50]], np.int32)
        #low_yellow = np.array([0, 0, 229], np.uint32)
        #up_yellow = np.array([180, 38, 255], np.uint32)
        #hsv = cv2.inRange(hasv, [vertices])
        #print(mask)
        #edges = cv2.Canny(mask, 25, 50)
        #print(edges)
        hsv = roi(hsv, [vertices])
 
        lines = cv2.HoughLinesP(hsv, 1, np.pi/180, 30, maxLineGap=50)
        if lines is not None:
            for line in lines:
                x1, y1, x2, y2 = line[0]
                cv2.line(hsv, (x1, y1), (x2, y2), (0, 255, 0), 5)
        cv2.imshow("frame", orig_frame)
        cv2.imshow("edges", hsv)

        key = cv2.waitKey(25)
        if key == 27:
            break
    video.release()
    cv2.destroyAllWindows()
 



def roi(img, vertices):
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, vertices, 255)
    masked = cv2.bitwise_and(img, mask)
    return masked



edge = cv2.VideoCapture('StayingInLane.avi')
#edge_detection(edge)
#clip = cv2.VideoCapture('StayingInLane.avi')
hough_transform(edge)