#!/usr/bin/bash
# xmonad_install.sh - Installs xmonad window manage 
# Author: mpmsimo
# Created: 8/26/15

# Installs xmonad and other helpful packages
sudo apt-get install xmonad suckless-tools xscreensaver

# If not using Ubuntu you may need to install the dmenu package
# Install xmobar, a commonly used xmonad status bar
sudo apt-get install xmobar
touch ~/.xmobarrc

# Installing Stalonetray (stand-alone tray)
sudo apt-get install stalonetray
