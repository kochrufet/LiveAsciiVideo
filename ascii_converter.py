"""
	Script for live ascii video

	Explanation:
		This script implements convertation process for our program.
		It accepts opencv image ( cv Mat ) and converts it to PIL image.
		After that we read our image and calculating char index for each
		pixel.

	Tip:
		"Negative" parameter can be useful for negatote the video ( frames )

	Author: kochrufet
"""

import os
import sys
import cv2
import time

from PIL import Image

class AsciiConverter:

	def __init__(self, size = 40, palette = "@%#*+=-:.", cvMat = None, negative = False):
		if not negative:
			palette = palette[::-1]

		self.width = int(os.get_terminal_size()[0] * size/100)
		self.palette = palette
		self.color_ratio = float(255/len(palette))+1

		self.configure(cvMat)
		w,h = self.image.size
		self.height = int((h/w)*self.width)

		self.pixels = self.image = None

	def configure(self, cvMat):
		self.image = Image.fromarray(cv2.cvtColor(cvMat, cv2.COLOR_BGR2RGB)).convert("L")

	def feed(self, cvMat):
		self.image = Image.fromarray(cv2.cvtColor(cvMat, cv2.COLOR_BGR2RGB)).convert("L").resize((self.width,self.height))

		self.pixels = self.image.getdata()

	def convert(self):
		data = ""
		index = 0

		for i in range(len(self.pixels)):
			if i%self.width==0 and i:data += '\n'

			data += self.palette[ int(self.pixels[i] / self.color_ratio) ]

		return data
