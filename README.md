# InvertPicture
invert.py is a simply script that inverts pictures colors.
Script now uses one of two possible methods to invert picture. Depending on the mode of picture.
Main reason for change was to make it independent from magick command(which didn't work) and to make it faster(which worked).

Tested on Mac only, pretty sure it would work on linux distributions and Windows with few tweaks.

---

**Dependencies:**
1. [Python3](https://www.python.org)
2. [Pillow](https://pillow.readthedocs.io/en/3.1.x/index.html)
3. [ImageMagick](https://imagemagick.org/index.php)

This script is directed at users of macOS.<br />
This simple POSIX script with three lines of code actual code, installs Homebrew repository, python3 and ImageMagick.
```
#!/bin/bash

# installing homebrew
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
# installing python3 from homebrew
brew install python3
# installing imagegick from homebrew
brew install imagemagick
pip3 install Pillow

# pip3 should be installed with python3 automatically.
# if not install using this command:
# sudo easy_install pip
# and rerun last command in Terminal.
```
If you want to install everything separately just put those commands into Terminal from top to bottom (omit lines with hashes).

---

**How does it work?**
1. First make sure you have installed python3 and ImageMagick (instruction above),
2. Now put script with pictures you want to invert,
3. Run it,
4. Check new pics in newly created folder.

**Flags**
* ```-e .ext``` - takes *.extensionName* (e.g. .png .tiff ..), it replaces standard list of extension with one given after flag. Useful with -p options if file given there has non-standard extension.
* ```-dn directoryName``` - name of directory that script will make and put or put inverted pictures.
* ```-p picture.ext``` - name of the picture to invert, it will invert just this picture. If you want to invert picture with non-standard extension use -e flag.

**Standard extensions**
- .png
- .jpg, .jpeg
- .gif
