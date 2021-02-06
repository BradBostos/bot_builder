#!/usr/bin/python3
import pyautogui
import time

def cord_tracker():
	while True:
		print (pyautogui.position());
		time.sleep(1);

if __name__ == '__main__':
    cord_tracker()
