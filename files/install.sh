#!/bin/bash

## install theia-ide as user pi
sudo -i -u pi \$HOME/theia-ide/theia_install.sh

## Setup service
cp -u theia-ide.service /lib/systemd/system
chmod 644 /lib/systemd/system/theia-ide.service
systemctl daemon-reload
systemctl enable theia-ide.service
systemctl start theia-ide.service
