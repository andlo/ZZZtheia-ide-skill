#!/bin/bash
# The requirements.sh is an advanced mechanism an should rarely be needed.
# Be aware that it won't run with root permissions and 'sudo' won't work
# in most cases.

#detect distribution using lsb_release (may be replaced parsing /etc/*release)
dist=$(lsb_release -ds)

#setting dependencies and package manager in relation to the distribution

if $(hash pkcon 2>/dev/null); then
    pm="pkcon"
else
    priv="sudo"
    if [ "$dist"  == "\"Arch Linux\""  ]; then
        pm="pacman -S"
        dependencies=()
    elif [[ "$dist" =~  "Ubuntu" ]] || [[ "$dist" =~ "Debian" ]] ||[[ "$dist" =~ "Raspbian" ]]; then
        pm="apt -y install"
        dependencies=()
    elif [[ "$dist" =~ "SUSE" ]]; then
        pm="zypper install"
        dependencies=()
    fi
fi


# installing dependencies
if [ ! -z "$pm" ]; then
    for dep in "${dependencies[@]}"
    do
        $priv $pm $dep
    done
fi

# Making swafile much bigger if there is enough free diskspace
freespace = $(df . | awk 'NR==2{print $4/1024/1024}')
if [ ${freespace%.*} >= 5 ]; then
    sed -i -e "s/CONF_SWAPSIZE=100/CONF_SWAPSIZE=2048/" /etc/dphys-swapfile
    /etc/init.d/dphys-swapfile stop
    /etc/init.d/dphys-swapfile start
fi
# On Mark_1 the firewall needs to be opend
if [ -f /usr/sbin/ufw ]; then
        ufw allow from any to any port 3000 proto tcp
fi

