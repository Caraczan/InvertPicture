#!python3
from os import listdir, system, mkdir, getcwd
from os.path import isfile, join, realpath
import argparse

# way to getting absolute path to the script and its Name
abspath = realpath(__file__)
abspath, sname = abspath.rsplit('/',1)
abspath += '/'
# abspath - absolute path to the folder conatinging script(absoulute means from root folder / )
# sname - name of script (if it would be changed by someone)
#print('sname: ',sname)
#print('abspath: ', abspath)

def isDotExt(name,extensions):
	for i in extensions:
		if i in str(name):
			return True
	return False

def findmany(string,find):
	many = 0
	for i in string:
		if i == find:
			many += 1
	return many

# activating args parser
parser = argparse.ArgumentParser()
# help text for flag parser
helpDir = "Name for new or existing directory for inverted pictures to be put in"
helpExt = "Name of one extension by which script will filter puctures and convert only those with given extension"
helpPic = "You can choose to invert one picture, make sure you write picture name with extension"
# parsing flags
parser.add_argument("-dn", "--directoryname", type = str, default = "inverted/", help = helpDir)
parser.add_argument("-e", "--extension", type = str, default = ['.png','.jpg','.jpeg','.gif','.tiff'], help = helpExt)
parser.add_argument("-p", "--picture", type = str, nargs='+', default = None, help = helpPic)
args = parser.parse_args()
#

#extension checking module, trust the user
if type(args.extension) == str:
	dotExtension = [args.extension]
else:
	dotExtension = args.extension
#print(type(dotExtension))
#print(dotExtension)

#checking if user given picture as argument and parsing it if not downloading it from listdir
if args.picture:
	pic = list()
	#pic = [picture.replace('/','') for picture in args.picture]
	for picture in args.picture:
		if '/' in picture:
			tpic = picture.rsplit('/',1)[1]
			if tpic != '' and findmany(tpic,'.') == 1 and isDotExt(tpic,dotExtension):
				pic.append(tpic)
else:
	pic = [file for file in listdir(abspath) if isfile(join(file)) and isDotExt(file,dotExtension)]	
#print(type(pic))
#print(pic)

#checking landing directory name
if args.directoryname == 'inverted/':
	dn = args.directoryname
else:
	dn = args.directoryname.replace('/','')
	dn += '/'
#print(dn)

#checking directory existance
if dn.split('/')[0] in listdir(abspath):
	print('Directory '+dn+' of that name exist in this folder.')
else:
	mkdir(abspath+dn)

#conversion itself, and saving, as we call magick command
for i in pic:
	system('magick '+i+' -negate '+dn+i)