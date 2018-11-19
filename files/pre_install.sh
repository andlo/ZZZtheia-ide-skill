#!/bin/bash
freespace=$(df . | awk 'NR==2{print $4/1024/1024}')
if [ ${freespace%.*}>=4 ]; then
    sed -i -e "s/CONF_SWAPSIZE=100/CONF_SWAPSIZE=1024/" /etc/dphys-swapfile
    /etc/init.d/dphys-swapfile stop >/dev/null 2>/dev/null
    /etc/init.d/dphys-swapfile start >/dev/null 2>/dev/null
else
    echo "Not enough free doskspace!"
    exit
fi

# On Mark_1 the firewall needs to be opend
if [ -f /usr/sbin/ufw ]; then
        echo "Opening port 3000 in firewall... "
        sudo ufw allow from any to any port 3000 proto tcp  >/dev/null 2>/dev/null
fi

