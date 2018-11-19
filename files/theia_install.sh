#!/bin/bash
cd $(dirname "$0")
mkdir theia-ideAAA
cd theia-ideAAA
#cd $(pwd)

## enter .venv
## If picroft
#if [ -f /home/pi/mycroft-core/.venv/bin/activate ]; then
#    source /home/pi/mycroft-core/.venv/bin/activate
#    export PATH="$HOME/bin:$HOME/mycroft-core/bin:$PATH"
#fi
## if mark_1
#if [ -f /opt/venvs/mycroft-core/bin/activate ]; then
#    source /opt/venvs/mycroft-core/bin/activate
#fi

echo "Installing nvm..."
#curl -o nvm_install.sh https://raw.githubusercontent.com/creationix/nvm/master/install.sh | bash >/dev/null 2>/dev/null
curl -o nvm_install.sh https://raw.githubusercontent.com/creationix/nvm/master/install.sh >/dev/null 2>/dev/null
chmod +x nvm_install.sh
nvm_install.sh >/dev/null 2>/dev/null

export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  >/dev/null 2>/dev/null # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  >/dev/null 2>/dev/null # This loads nvm bash_completion

echo "Intsalling node..."
nvm install 8 >/dev/null 2>/dev/null
echo "Installling yarn..."
npm install -g yarn >/dev/null 2>/dev/null

echo "Building theia..."
yarn >/dev/null 2>/dev/null
yarn theia build >/dev/null 2>/dev/null

echo "Installing Python Language Server"
mycroft-pip install python-language-server >/dev/null 2>/dev/null

<<<<<<< HEAD
cp -u $(pwd)/editorconfig $HOME/.editorconfig
=======
pip3 install python-language-server
>>>>>>> 23f9797fe18ee65dee9249238790a0897139a8be

