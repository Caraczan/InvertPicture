#!python3
from os import listdir, system, mkdir, getcwd
from os.path import isfile, join

import argparse

from PIL import Image, ImageOps

def isDotExt(name,extensions):
	"""checks if it is one of corrects extensions, returns true if so if not returns false"""
	if isinstance(extensions, str):
		if extensions[1] != '.':
			extensions = '.' + extensions
		if extensions in name:
			return True
	else:
		for i in extensions:
			if i in name:
				return True
	return False

def checkDir(defaultLandingDirectory):
	if defaultLandingDirectory[-1] == '/':
		dLD = defaultLandingDirectory[:-1]
	ch = False
	for i in listdir():
		if i == dLD:
			ch = True
	if ch == False:
		mkdir(dLD)

def magickInvertCommand(pic, defaultLandingDirectory):
	defaultLandingDirectory = slashCheck(defaultLandingDirectory)
	system("magick "+pic+" -negate "+defaultLandingDirectory+pic)

def slashCheck(string):
	if string != None and string[-1] != '/':
		string += '/'
		return string
	else:
		return string

def invert(pic):
	pic = ImageOps.invert(pic)
	return pic

# parsing flags
parser = argparse.ArgumentParser()
helpDir = "Name for new or existing directory for inverted pictures to be put in"
helpExt = "Name of one extension by which script will filter puctures and convert only those with given extension"
helpPic = "You can choose to invert one picture, make sure you write picture name with extension"

parser.add_argument("-dn", "--directoryname", type = str, default = "inverted", help = helpDir)
parser.add_argument("-e", "--extension", type = str, default = ['.png','.jpg','.jpeg','gif'], help = helpExt)
parser.add_argument("-p", "--picture", type = str, default = None, help = helpPic)
args = parser.parse_args()

# list of extensions to filter files and pics in current dir
dotExtensions = args.extension
# name of directory where inverted pictures will be put
defaultLandingDirectory = args.directoryname
defaultLandingDirectory = slashCheck(defaultLandingDirectory)
# name of one picture if you want to invert just one
pic = args.picture
# we will not allow to pull pictures from other places
pic = slashCheck(pic)

if pic:
	if isDotExt(pic, dotExtensions):
		checkDir(defaultLandingDirectory)
		# print(pic.mode)
		pic = Image.open(i)
		if pic.mode == 'P':
			magickInvertCommand(i,defaultLandingDirectory)
		else:	
			invert(pic)
			pic.save(defaultLandingDirectory+i)	

	else:
		print('Picture name must be in current directory to exist,\nif you use pictures with strange/non-standard extension please use -e .ext with your extension in place of .ext')
else:
	pic = [file for file in listdir() if isfile(join(file)) and isDotExt(file,dotExtensions)]
	if pic:
		"""checks if file exist, it is only so there is no throw out error from mkdir that directory exist"""
		checkDir(defaultLandingDirectory)
		"""inverting pictures and putting them in directory"""
		for i in pic:
			pic = Image.open(i)
			# print(pic.mode)
			if pic.mode == 'P':
				magickInvertCommand(i,defaultLandingDirectory)
			else:	
				pic = invert(pic)
				pic.save(defaultLandingDirectory+i)	
			
	else:
		"""If it wont find any images it will put this message on screen"""
		print("No pictures given viable for inversion.")
		print("Eligable for inversion:")
		for i in dotExtensions:
			print(i)
