#!python3
from os import listdir, system, mkdir
from os.path import isfile, join
import argparse

def isDotExt(name,extensions):
	"""checks if it is one of corrects extensions, returns true if so if not returns false"""
	if isinstance(extensions, str):
		if extensions in name:
			return True
	else:
		for i in extensions:
			if i in name:
				return True
	return False

def checkDir(defaultLandingDirectory):
	ch = False
	for i in listdir():
		if i == defaultLandingDirectory:
			ch = True
	if ch == False:
		mkdir(defaultLandingDirectory)

def magickNegateSysCommand(pic, defaultLandingDirectory):
	system("magick "+pic+" -negate "+defaultLandingDirectory+'/'+pic)

#parsing flags
parser = argparse.ArgumentParser()
helpDir = "Name for new or existing directory for inverted pictures to be put in"
helpExt = "Name of one extension by which script will filter puctures and convert only those with given extension"
helpPic = "You can choose to invert one picture, make sure you write pic name with extension"
parser.add_argument("-d", "--directory", type = str, default = "inverted", help = helpDir)
parser.add_argument("-e", "--extension", type = str, default = ['.png','.jpg','.jpeg','gif'], help = helpExt)
parser.add_argument("-p", "--picture", type = str, default = None, help = helpPic)
args = parser.parse_args()

# list of extensions to filter files and pics in current dir
dotExtensions = args.extension
# name of directory where inverted pictures will be put
defaultLandingDirectory = args.directory
# name of one picture if you want to invert just one
pic = args.picture

if pic:
	if isDotExt(pic, dotExtensions):
		checkDir(defaultLandingDirectory)
		magickNegateSysCommand(pic,defaultLandingDirectory)
	else:
		print('Picture name must be in current directory to exist,\nif you use pictures with strange/non-standard extension please use -e .ext with your extension in place of .ext')
else:
	onlypictures = [file for file in listdir() if isfile(join(file)) and isDotExt(file,dotExtensions)]
	if onlypictures:
		"""checks if file exist, it is only so there is no throw out error from mkdir that directory exist"""
		checkDir(defaultLandingDirectory)
		"""inverting pictures and putting them in directory"""
		for pic in onlypictures:
			magickNegateSysCommand(pic,defaultLandingDirectory)
	else:
		"""If it wont find any images it will put this message on screen"""
		print("No pictures given viable for inversion.")
		print("Eligable for converion:")
		for i in dotExtensions:
			print(i)
