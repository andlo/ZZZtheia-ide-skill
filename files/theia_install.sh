#!/bin/bash

export NVM_DIR="$(pwd)/nvm"

echo "Installing nvm..."
curl -o nvm_install.sh https://raw.githubusercontent.com/creationix/nvm/master/install.sh | bash

[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  >/dev/null 2>/dev/null # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  >/dev/null 2>/dev/null # This loads nvm bash_completion


echo "Intsalling node..."
nvm install 8
echo "Installling yarn..."
npm install -g yarn

echo "Building theia..."
yarn
yarn theia build

echo "Building thiea OK"

## on mark_1 the version of git is to old, so need to compile and install newer one
## if mark_1
#if [ $(git --version |cut -d" " -f3 | cut -d"." -f1) \< 3 ]; then
#    if [ $(git --version |cut -d" " -f3 | cut -d"." -f2) \< 11 ]; then
#        echo "A newer version og git is requered!"
#        echo "Installing depencies..."
#        apt-get -y install dh-autoreconf libcurl4-gnutls-dev libexpat1-dev gettext libz-dev libssl-dev >/dev/null 2>/dev/null
#        echo "Cloning git..."
#        git clone git://git.kernel.org/pub/scm/git/git.git >/dev/null 2>/dev/null
#        cd git
#        echo "Compiling git..."
#        make configure >/dev/null 2>/dev/null
#        #./configure --prefix=$(pwd)/git >/dev/null 2>/dev/null
#        ./configure >/dev/null 2>/dev/null
#        make >/dev/null 2>/dev/null
#        # echo "Installing git..."
#        # make install >/dev/null 2>/dev/null
#        cd ..
#    fi
#fi

