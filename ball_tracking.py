import numpy as np
import cv2
import imutils
from collections import deque

from imutils.video import VideoStream
import time


class BallTracker:
	def __init__(self):
		self.greenLower = (45//2, 45, 10)
		self.greenUpper = (65//2, 255, 255)
		self.positions = deque(maxlen=2)

	def add_frame(self, frame):
		found, center, radius = False, None, None
		if frame is None:
			return found, center, radius

		# blur the frame, and convert it to the HSVcolor space
		blurred = cv2.GaussianBlur(frame, (11, 11), 0)
		hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

		# construct a mask for the color "green", then perform
		# a series of dilations and erosions to remove any small
		# blobs left in the mask
		mask = cv2.inRange(hsv, self.greenLower, self.greenUpper)
		mask = cv2.erode(mask, None, iterations=2)
		mask = cv2.dilate(mask, None, iterations=2)

		

		# find contours in the mask and initialize the current
		# (x, y) center of the ball
		cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
		cnts = imutils.grab_contours(cnts)
		
		# only proceed if at least one contour was found
		if len(cnts) > 0:

			# find the largest contour in the mask, then use
			# it to compute the minimum enclosing circle and
			# centroid
			c = max(cnts, key=cv2.contourArea)
			((x, y), radius) = cv2.minEnclosingCircle(c)
			M = cv2.moments(c)

			found, center = True, (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

			# only proceed if the radius meets a minimum size
			# if radius > 10:
			# 	self.positions.appendleft(center)
			# 	return True, center
		
		return found, center, radius

if __name__ == "__main__":
	bt = BallTracker()

	# Start the videostream
	vs = VideoStream(src=0).start()
	time.sleep(2.0)

	while True:
		# grab the current frame
		frame = vs.read()
		b, center, radius = bt.add_frame(frame)
		print(b, center, radius)