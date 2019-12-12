#!/bin/bash

# installing homebrew
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
# installing python3 from homebrew
brew install python3
# installing imagegick from homebrew
brew install imagemagick
pip3 install Pillow

# pip3 should be installed with python3.
# if not download use this command
# sudo easy_install pip
# and rerun last command in Terminal

