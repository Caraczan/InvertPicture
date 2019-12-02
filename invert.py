#!python3
from os import listdir, system
from os.path import isfile, join

# important variables
dotExtensions = ['.png','.jpg','.jpeg']
defaultLandingDirectory = 'invertedPics'

def isDotExt(name,extensions):
	"""checks if it is one of corrects extensions, returns true if so if not returns false"""
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
		system("mkdir "+defaultLandingDirectory)

	"""inverting pictures and putting them in directory"""
	for pic in onlyfiles:
		system("magick "+pic+" -negate "+defaultLandingDirectory+'/'+pic)

else:
	"""If it wont find any images it will put this message on screen"""
	print("No pictures given viable for inversion.")
	print("Pictures with ")
	for i in Dot:
		print(i)
	print("extensions can be inverted.")