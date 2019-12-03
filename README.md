# InvertPicture
invert.py is a simply script that inverts colors pictures. <br />
Script uses magick from ImageMagick in this script. <br />

Tested for Mac only, pretty sure it would work on linux distros too. <br />

---

**Dependencies:**
1. [Python3](https://www.python.org)
2. [ImageMagick](https://imagemagick.org/index.php)

**How does it work?**<br />
1. First make sure you have installed python3 and ImageMagick (links above),
2. Now put script with pictures you want to invert,
3. Run it,
4. Check new pics in newly created folder.

**Flags**
* ```-e .ext``` - takes ```.extensionName``` (e.g. .png .tiff ..), it replaces standard list of extension with one given after flag. Useful with -p options if file given there has non-standard extension.
* ```-dn directoryName``` - name of directory that script will make and put or put inverted pictures.
* ```-p picture.ext``` - name of the picture to invert, it will invert just this picture. If you want to invert picture with non-standard extension use -e flag.

**Standard extensions**
- .png
- .jpg, .jpeg
- .gif
