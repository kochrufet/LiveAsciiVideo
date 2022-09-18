"""
	Script for live ascii video

	Explanation:
		This script contains LiveCamera and LiveAsciiVideo classes.
		Those classes are for getting frame from webcam, processing frame,
		and generatin ascii context as result.

	Tip:
		You can change fps when calling LiveAsciiVideo builder, normal fps is about 60.

	Author: kochrufet
"""

import cv2
import sys
import time

from ascii_converter import AsciiConverter

class LiveCamera:

	def __init__(self, camera_index = 0):
		self.video = cv2.VideoCapture(camera_index)

		self.timeout = 3 # sec
		self.failure = False

		self.state = False
		self.mat = None

	def update(self):
		self.state, self.mat = self.video.read()

	def startCamera(self):
		self.update()
		i = 0
		while not self.state:

			if i > self.timeout:
				self.failure = True
				break

			time.sleep(1)
			self.update()
			i += 1

	def __del__(self):
		self.video.release()
		print("Camera released")

class LiveAsciiVideo:

	def __init__(self, fps = 60, palette = None):
		self.camera = LiveCamera()
		self.camera.startCamera()

		if palette:
			self.converter = AsciiConverter(cvMat = self.camera.mat, palette = palette)
		else:
			self.converter = AsciiConverter(cvMat = self.camera.mat)


		self.ms = 1 / fps

	def __start(self):

		while True:
			self.camera.update()
			self.converter.feed(self.camera.mat)

			sys.stdout.write( self.converter.convert() + '\r')
			sys.stdout.flush()

			time.sleep(self.ms)

	def start(self):

		try:
			self.__start()
		except KeyboardInterrupt:
			print("Program finished")
		except Exception as e:
			raise e
