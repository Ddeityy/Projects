#Track a purple blob and output the center of the contour as x, y for After Effects tracking.

import numpy as np
import cv2 as cv

#HSV colors
lower = np.array([130, 150, 20])
higher = np.array([150, 255, 255])

frames = open(r"C:\Users\ddeit\Desktop\pythonProject\PurpleTracker\frames.txt", "w")
video = cv.VideoCapture(r"C:\Users\ddeit\Desktop\pythonProject\PurpleTracker\track.mp4")

counter = -1
frames.write("txt = [];\n")
while True:
    counter += 1
    success, img = video.read()
    frame = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    mask = cv.inRange(frame, lower, higher)
    conts, hier = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    if len(conts) != 0:
        for cont in conts:
            M = cv.moments(cont)
            if M['m00'] != 0:
                cx = int(M['m10']/M['m00'])
                cy = int(M['m01']/M['m00'])
                frames.write(f"txt[{counter}] = [{cx}, {cy}];\n")
                frames.flush()
    else:
        frames.write(f"txt[{counter}] = [3000, 3000];\n")
        frames.flush()
        
    cv.waitKey(1)
    