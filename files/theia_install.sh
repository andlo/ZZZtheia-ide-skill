#!/bin/bash
mkdir $HOME/theia-ide
cd $HOME/theia-ide
curl -o- https://raw.githubusercontent.com/creationix/nvm/master/install.sh | bash

export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion

nvm install 8
npm install -g yarn

yarn
yarn theia build

pip3 install python-language-server

cp -u .editorconfig /opt/mycroft/skills
