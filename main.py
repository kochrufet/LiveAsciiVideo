"""
	Script for live ascii video

	Explanation:
		This script gives a palette choice for user and registers the palette for camera.
		After that, convertation process starts.

	Author: kochrufet
"""

import os
from live_process import LiveAsciiVideo

palette_container = {
	"normal1" : "@%#*+=-:.",
	"normal2" : "@#?;:,. ",
	"normalplus" : "ME$sj1|-^`",
	"number" : "8960452317",
	"letter" : "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
	"silver" : "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'.",
	"symbol" : "!\"#$%&'()*+,-./:;<=>?@[\\]^_{|}~"
}

palette_name = None
values = palette_container.keys()

while not palette_name:
	os.system("clear || cls")
	print("Choose a palette !",*values, sep = '\n')

	palette_name = input(">>>")

	if palette_name not in values:
		palette_name = None
		print("Invalid palette name !")
		time.sleep(0.5)

LiveAsciiVideo(palette = palette_container[palette_name]).start()