#!/bin/bash

## install theia-ide as user pi
sudo -i -u pi ./theia_install.sh

## Setup service
cp -u theia-ide.service /lib/systemd/system
chmod 644 /lib/systemd/system/theia-ide.service
systemctl daemon-reload
systemctl enable hello.service
systemctl start hello.service
