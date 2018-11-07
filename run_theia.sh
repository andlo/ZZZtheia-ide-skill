#!/bin/bash

export LOCAL_GIT_DIRECTORY="/usr"
export GIT_EXEC_PATH="/usr/lib/git-core"

export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion

yarn theia start /opt/mycroft/skills --hostname 0.0.0.0 --port 3000