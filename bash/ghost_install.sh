#!/usr/bin/bash
#mpmsimo
#9/9/2016

PACKAGE_ARRAY=(curl wget zip nodejs npm build-essential)
GHOST_ZIP='https://ghost.org/zip/ghost-latest.zip'
WEB_DIR='/var/www'
GHOST_DIR='/var/www/ghost'
DOMAIN='http://blog.mpmsimo.com'

check_for_missing_packages(){
    # Node.js repo
    curl -sL https://deb.nodesource.com/setup_4.x | sudo -E bash -

    # figure out if needed packages are installed
	for package in ${PACKAGE_ARRAY[@]};
	do
        #PKG_SEARCH=$(dpkg -s $package > /dev/null 2>&1)
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

ghost_install(){
    #Node js version
    #NPM version
    ls -s $(which nodejs) /usr/bin/node
    sudo mkdir -p $GHOST_DIR
    cd $WEB_DIR
    sudo wget $GHOST_ZIP
    sudo unzip -d ghost ghost-latest.zip
    cd $GHOST_DIR

    # Install node production dependencies
    sudo npm install --production

    # Install example config
    sudo cp config.example.js config.js

    #TODO: Only replace first occurences
    # Use sed to change url, use ; instead / as delimeter because urls...
    # Not global since we do not want to change development url
    echo "Changing blog URL to: $DOMAIN"
    #sudo sed -i -e "s;url\:.*;url\: '$DOMAIN,;" config.js

    # Use sed to change host entry.
    echo "Changing host entry to: 0.0.0.0"
    #sudo sed -i -e "s;host\:.*;host\: 0.0.0.0,;" config.js
}

check_for_missing_packages
ghost_install
