# InvertPicture
invert.py is a simply script that inverts pictures colors.

Script has been flattened and simpliefied for sake of clarity and overall speed. Now there is only one way script invert, ImageMagick. Magick is marginally slower than Pillow/PIL but impact is marginal. Script no longer needlesly check things constantly.

---

Small but significant change, now ```-p``` flag will take more then one argument. Also handling input is slghtly different, now it will also filter from more than ```.``` in string, those will not be added to list and in effect processed.

Now user should be aware of changes/warnings:
* scirpt will take anything to the -e and then proceed to check based on it. So be aware and put correct extension with dot.
* -p flag will check if it comply with extensions, if you have different than standard it omit this input from futher processing. You should use -e flag to this in this case.
* -p flag won't take path and work on picture in different directory, it will take last string (last after ```/```).
* -dn flag takes anything but it will sterilize input from ```/```

Tested on Mac only, pretty sure it would work on linux distributions and Windows with few tweaks on the host.

# Instalation

**Dependencies:**
1. [Python3](https://www.python.org)
2. [ImageMagick](https://imagemagick.org/index.php)

This simple bash script with three lines of code actual code, installs Homebrew repository, python3 and ImageMagick.
Open with Terminal or ```bash install_required.sh``` from terminal in folder containing this script.
```
#!/bin/bash

# installing homebrew
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
# installing python3 from homebrew
brew install python3
# installing imagegick from homebrew
brew install imagemagick
```
If you want to install everything separately just put those commands into Terminal from top to bottom (omit lines with hashes) or jus go to the respectevie websites and install based on their guides.

## How does it work?
0. First make sure you have installed python3 and ImageMagick (links below),
1. Now put script with pictures you want to invert,
2. Run it,
3. Check new pics in newly created folder.

## Flags
* ```-e .extension``` - takes *.extensionName* (e.g. .png .tiff ..), it replaces standard list of extension with one given after flag. Useful with -p options if file given there has non-standard extension.
* ```-dn directory_name``` - name of directory that script will make and put or put inverted pictures.
* ```-p picture.ext``` - name of the picture to invert, it will invert just this picture. If you want to invert picture with non-standard extension use -e flag.

## Standard extensions
- .png
- .jpg/jpeg
- .gif
- .tiff

---

