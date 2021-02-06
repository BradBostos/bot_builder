import pyautogui
import random
import time

class clicker:
	move_time = 0;
	hover_time = 0;
	delay = None;

	def __init__(self, move_time=.15, hover_time=.05):
		self.move_time = move_time;
		self.hover_time = hover_time;

	def left_click(self, position, delay_time, event=True):
		pyautogui.moveTo(position[0], position[1], duration=self.move_time);
		time.sleep(self.hover_time);
		pyautogui.click(position[0], position[1]);

	def right_click(self, position, delay_time, event=True):
		pyautogui.moveTo(position[0], position[1], duration=self.move_time);
		time.sleep(self.hover_time);
		pyautogui.rightClick(position[0], position[1]);
