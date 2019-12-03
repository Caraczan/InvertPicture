#!python3
from os import listdir, system, mkdir
from os.path import isfile, join
import argparse

#parsing flags
parser = argparse.ArgumentParser()
helpDir = "Name for new or existing directory for inverted pictures to be put in"
helpExt = "Name of one extension by which script will filter puctures and convert only those with given extension"
parser.add_argument("-d", "--directory", type = str, default = "inverted", help = helpDir)
parser.add_argument("-e", "--extension", type = str, default = ['.png','.jpg','.jpeg'], help = helpExt)
args = parser.parse_args()

# list of extensions to be checked by to filter files and pics in current dir
dotExtensions = args.extension
# name of directory where inverted pictures will be put
defaultLandingDirectory = args.directory

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

"""downloads pictures from current directory"""
onlypictures = [file for file in listdir() if isfile(join(file)) and isDotExt(file,dotExtensions)]
if onlypictures:
	"""checks if file exist, it is only so there is no throw out error from mkdir that directory exist"""
	ch = False
	for i in listdir():
		if i == defaultLandingDirectory:
			ch = True
	if ch == False:
		mkdir(defaultLandingDirectory)

	"""inverting pictures and putting them in directory"""
	for pic in onlypictures:
		system("magick "+pic+" -negate "+defaultLandingDirectory+'/'+pic)

else:
	"""If it wont find any images it will put this message on screen"""
	print("No pictures given viable for inversion.")
	print("Eligable for converion:")
	for i in dotExtensions:
		print(i)
