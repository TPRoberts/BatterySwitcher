#!/usr/bin/python
from PIL import Image, ImageDraw, ImageFont
import math, re
import os, sys
import subprocess

from time import sleep
hex = ['0', '1', '2', '3', '4', '5', '6', '7', '9', 'A', 'a', 'B', 'b', 'c', 'C', 'D', 'd', 'e', 'E', 'f', 'F']
number = ['1', '2', '3', '4', '5', '6', '7', '9']


# Clean command Promt Screen
def cls():
    os.system(['clear','cls'][os.name == 'nt'])

# Function that choice list
def menu(question, list):
	invalid = False
	promt = True
	while promt:
		pass

		print question
		for i in range (0, len(list),1):
			string = "%d: %s" % (i+1, list[i])
			print string
		reponse = raw_input("-> Plese Choose a option: ")
		if reponse in number:
			if int(reponse) >0 and int(reponse) <=len(list):
				invalid = False
			else:
				invalid = True
		else:
			invalid = True

		if invalid:
			print "Choice entered is invalid!"
		else:
			print "-> You chose %d\n" % (int(reponse))
			promt = False
	print "\n"
	return int(reponse)-1

def colourMenu(question):
	invalid = False
	promt = True
	while promt:
		print question
		hexColour = raw_input("-> Input your RGBA colour -> ").split(' ')

		if len(hexColour) > 4:
			print "Hex Number entered is too long!"
		if len(hexColour) < 4:
			print "Hex Number entered is too short!"

		if len(hexColour) == 4:
			for i in range (0, len(hexColour),1):
				hexString = hexColour[i]
				firstHexString = hexString[0]
				secondHexString = hexString[1]
				if firstHexString in hex:
					if secondHexString in hex:
						invalid = False
					else:
						invalid = True
				else:
					invalid = True

			if invalid:
				print "Hex Number entered is invalid!"
			else:
				promt = False

	print "\n"
	colour = (int(hexColour[0], 16), int(hexColour[1], 16), int(hexColour[2], 16), int(hexColour[3], 16))
	return colour



styleQ = "Please choose the style of the icon you would like to make"
styles = ["Sense7","Sense6", "Medium", "Large", "Circle", "Text"]
fontQ = "Please choose the font for your percent indicator font (if any)"
paddingQ = "Please choose the space size (in pixels) between the outline and the battery colour"
padding = ["0 pixels","1 pixels", "2 pixels", "3 pixels"]




cls() # Clear shell

# Style Choice
styleRes = menu(styleQ, styles)

## Only Promt the user to indicator for caertain styles
if styles[styleRes] == "Text":
	fonts = ["Aerial", "Roboto", "AndroidLogo", "LCD"]
else:
	fonts = ["Aerial", "Roboto", "AndroidLogo", "LCD", "NoIndicator"]

if (styles[styleRes] != "Sense7"):
	fontRes = menu(fontQ, fonts)
else:
	fontRes = False

print "\nNOTE: Colours should be typed in Hex with spaces as follows (AA BB CC FF).\n It is in RGBA format (Red(AA), Green(BB), Blue(CC) and Alpha(FF is Opaque, 00 is transparent)).\n"

mainColour = colourMenu ("Enter your main colour (the colour from 100% to 31%)")

warningColour = colourMenu ("Enter your warning colour (the colour from 30% to 11%)")

unhealthyColour = colourMenu ("Enter your unhealthy colour (the colour from 10% to 0%)")

if styles[styleRes] != "Sense7" and styles[styleRes] != "Text":
	fontColour = colourMenu ("Enter the colour of your font")
else:
	fontColour = False

if styles[styleRes] != "Circle" and styles[styleRes] != "Text":
	outlineColour = colourMenu ("Enter the colour of your battery outlineColour")
	paddingRes = menu (paddingQ, padding)
else:
	paddingRes = False
	outlineColour = False

print "\n The summary of your choice\n"
print "Style: %s" % styles[styleRes]
if fontRes != False:
	print "Font: %s" % fonts[fontRes]
print "Main colour: %s" % mainColour
print "Warning colour: %s" % warningColour
print "Unhealthy colour: %s" % unhealthyColour

if fontColour != False:
	print "Font colour: %s" % fontColour
if paddingRes != False:
	print "Space size: %s" % padding[paddingRes]
if outlineColour != False:
	print "Outline colour: %s" % outlineColour
	

