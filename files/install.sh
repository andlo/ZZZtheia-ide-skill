#!/bin/bash

cd $1
curl -o- https://raw.githubusercontent.com/creationix/nvm/master/install.sh | bash
#chmod +x install.sh

export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion

nvm install 8
npm install -g yarn

yarn
yarn theia build

#
