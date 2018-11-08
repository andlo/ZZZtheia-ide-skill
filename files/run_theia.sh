#!/bin/bash

cd $1
export LOCAL_GIT_DIRECTORY="/usr"
export GIT_EXEC_PATH="/usr/lib/git-core"

export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion

pyls &
yarn theia start /opt/mycroft/skills  --startup-timeout -1 --hostname 0.0.0.0 --port 3000
