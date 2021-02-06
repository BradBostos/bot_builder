import numpy as np
import time
import cv2
import pyautogui

class screen_matcher:
	top_left = [(0,0)]
	bottom_right = [(0,0)]
	template_path = ""
	thresh = 1
	img = []

	def __init__(self, template_path, thresh=0.8):
		self.top_left = []
		self.bottom_right = []
		self.template_path = template_path
		self.thresh = thresh
		self.rematch()

	def rematch(self):
		self.img = cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_BGR2RGB)
		# cv2.imshow('Screen', img_rgb);
		# cv2.waitKey(0);
		temp = cv2.imread(self.template_path)
		h, w, _ = temp.shape
		res = cv2.matchTemplate(self.img, temp, cv2.TM_CCOEFF_NORMED)
		matches = np.where(res >= self.thresh)
		self.top_left= []
		self.bottom_right = []
		for pt in zip(*matches[::-1]):
			self.top_left.append(pt)
			self.bottom_right.append((pt[0] + w, pt[1] + h))

	def set_template(self, template_path):
		self.template_path = template_path
		self.rematch()
		for i in range(2):
			if self.top_left == []:
				time.sleep(i+1)
				self.rematch()
		if self.top_left == []:
			print("Could not find template: " + template_path)


	def set_thresh(self, thresh):
		self.thresh = thresh
		self.rematch();

	def get_positions(self):
		return (self.top_left, self.bottom_right)

	def show_matches(self):
		img_loc = self.img;
		for i in range(len(self.top_left)):
			cv2.rectangle(img_loc, self.top_left[i], self.bottom_right[i], (0, 255, 255), 2)
		cv2.imshow("Matches", img_loc)
		cv2.waitKey(0)
