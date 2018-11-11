# <img src='theia.png' card_color='#40DBB0' width='50' style='vertical-align:bottom'/> THEIA IDE
VS Code experience on your Mycroft device

## About
Installs and setup THEIA IDE localy on your Mycroft device

## Description
This skill installs Theia IDE on your Mycroft device. This makes it easy to make and edit skills for Mycroft. Thiea IDE integrates whith Github, and you can use mycroft tools like mycroft-msm and mycroft-msk directly from the integrated shell in the IDE.
Theia provides the VS Code experience in the browser. Developers familiar with Microsoft's VS code editor will find many familiar features and concepts, to minimze the gap when switching between desktop and webbased environment.

https://www.theia-ide.org/index.html

### When running this skill on Mark_1 there are some features of THEIA IDE that are missing.
This is - I think - due to the version of python3 is 3.4, and some of the features requere version >= 3.5

## How to install
To get Theai IDE to comile it is needed to encrease the swapsize. This is none by editing the file /etc/dphys-seapfile and setting changing CONF_SWAPSIZE=100 to 2048.

Be aware that stoch mark_1 only has a 4 GB ssd card. My experiance is that it isnt enough for this skill.

To encrease the swapsize log into your device with ssh and do the following:
```
sudo nano /etc/dphys-swapfile
```
exit by Ctrl+X and save
And restart swarpfile
```
sudo /etc/init.d/dphys-swapfile stop
sudo /etc/init.d/dphys-swapfile start
```

Install the skill by
```
mycroft-msm install https://github.com/andlo/theia-ide-skill.git
```
Skill wil then install THEIA IDE. This takes more than 15 minutes, and will slow your Mycroft device down when compiling node-modules.

When done, there should be a log info saying "Starting THEIA IDE" and Mycrot should tell you by voice that he has installed the skill.
You can then open a web-browser and gå to http://picroft:3000 if your Mycroft device is picroft. If on a Mark One go to http://mark_1:3000
You then get access to the THEIA IDE in a workplace located /opt/mycroft/skills.

On mark_1 the firewall needs to be opend. This is done by
```
sudo ufw allow from any to any port 3000 proto tcp
```

## Credits
Andreas Lorensen (@andlo)

## Supported Devices
platform_mark1 platform_picroft

## Category
**Configuration**

## Tags
#theia
#IDE
#editor
#dev
