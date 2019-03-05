#!/usr/bin/bash
#mpmsimo
#9/11/2016

HUGO_VER='0.16'
HUGO_DISTRO='linux-64bit'
HUGO_ARCH='amd64'
HUGO_DEB='hugo_'$HUGO_VER'-1_'$HUGO_ARCH'.deb'
HUGO_SRC='hugo_'$HUGO_VER'_'$HUGO_DISTRO'.tgz'
HUGO_TGZ='https://github.com/spf13/hugo/releases/download/v'$HUGO_VER'/'$HUGO_DEB
#HUGO_TGZ='https://github.com/spf13/hugo/releases/download/v'$HUGO_VER'/'$HUGO_SRC
echo $HUGO_TGZ

WEB_DIR='/var/www'
HUGO_DIR='/var/www/hugo'
HUGO_TITLE='mpmsimo.com'
DOMAIN='http://mpmsimo.com'

check_for_missing_packages(){
    PACKAGE_ARRAY=(wget python-pip virtualenv git nginx)

    sudo apt-get update
    # figure out if needed packages are installed
	for package in ${PACKAGE_ARRAY[@]};
	do
        PKG_SEARCH=$(dpkg-query -W -f='${Status}' $package 2> /dev/null | grep -c 'ok installed')
        if [[ $PKG_SEARCH -eq 0 ]];
            then
                echo "Installing $package"
                sudo apt-get install $package
            else
                echo "$package is already installed."
        fi
	done
}

hugo_install(){
    sudo mkdir -p $HUGO_DIR/themes
    cd $HUGO_DIR
    # From source
    #sudo wget $HUGO_TGZ
    #sudo tar -xvzf $HUGO_SRC

    # Debian package
    sudo wget $HUGO_TGZ
    sudo dpkg -i $HUGO_DEB

    echo ''
    hugo version

    sudo git clone --recursive https://github.com/spf13/hugoThemes $HUGO_DIR/themes

    # Not really needed? - App will be running as root so...
    #virtualenv henv
    #source $HOME/henv/bin/activate
    #pip install Pygments
    sudo pip install Pygments

    sudo hugo gen autocomplete 
}

hugo_configuration(){
    env HUGO_TITLE=$HUGO_TITLE
    #sudo sed -i -e "s;url\:.*;url\: '$DOMAIN,;" config.js
}

check_for_missing_packages
hugo_install
hugo_configuration
