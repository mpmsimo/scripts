#!/usr/bin/bash
#mpmsimo
#9/9/2016

GHOST_ZIP='https://ghost.org/zip/ghost-latest.zip'
WEB_DIR='/var/www'
GHOST_DIR='/var/www/ghost'

sudo mkdir -p $GHOST_DIR
cd $WEB_DIR
sudo wget $GHOST_ZIP
cd $GHOST_DIR

sudo npm install --production
