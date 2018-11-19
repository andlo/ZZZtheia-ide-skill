#!/bin/bash
<<<<<<< HEAD
cd $(dirname "$0")
=======

## if on mycroft venv is started different than on picroft
## this check dosnt work yet...need to find a better way.....
if [ "$(whoami)" == "mycroft" ]; then
     source /opt/venvs/mycroft-core/bin/activate
fi

## enter venv
#source /home/pi/mycroft-core/venv-activate.sh -q
cd $HOME/theia-ide
>>>>>>> 23f9797fe18ee65dee9249238790a0897139a8be

## make sure git is working
#export LOCAL_GIT_DIRECTORY="/usr"
#export GIT_EXEC_PATH="/usr/lib/git-core"

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

## setup and load nvm
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion

## run theia-ide
yarn theia start /opt/mycroft/skills  --startup-timeout -1 --hostname 0.0.0.0 --port 3001
