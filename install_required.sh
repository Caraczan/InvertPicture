#!/bin/bash

# installing homebrew
if [[ $(brew | grep '\w: command not found: brew') == "" ]]; then
	/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
fi
# installing python3 from homebrew
if [[ $(python -V) < 2.8 && $(python3 -V) < 3 ]]; then
	brew install python3
fi
# installing imagegick from homebrew
if [[ $(magick | grep '\w: command not found: magick') == "" ]]; then
	brew install imagemagick
fi
