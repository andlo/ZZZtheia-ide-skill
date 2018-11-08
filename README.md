# <img src='theia.png' card_color='#40DBB0' width='50' style='vertical-align:bottom'/> THEIA IDE
VS Code experience on your Mycroft device

## About
Installs and setup THEIA IDE localy on your Mycroft device


## Description
This skill installs Theia IDE on your Mycroft device. This makes it easy to make and edit skills for Mycroft. Thiea IDE integrates whith Github, and you can use mycroft tools like mycroft-msm and mycroft-msk directly from the integrated shell in the IDE.
Theia provides the VS Code experience in the browser. Developers familiar with Microsoft's great editor will find many familiar features and concepts, to minimze the gap when switching between desktop and cloud environment.

https://www.theia-ide.org/index.html


# INITIAL WORK !
This skill isnt finish yet! But now it seems to work.

### What supposed to work
* Installing and setup
* Running and access to THEIA http://picroft:3000
* Therminal and use og mycroft specifik commands
* Git integration - Pull and push and monitor changes etc.
* Search throu all workspaceses
* Python Language server support - formatiing and highlight etc

### What maybe dosnt work
* CRLF and not LF at the end of line in new files made by THEIA. There is a editorconfig plugin in THEIA that can be configured to fix this. I am working on the right stuf for that.


### Overall experiance
I like this IDE, as it is vscode like. Having it on the picroft makes it easier for me to make and edit skills etc.
Performance seems OK - dosnt see or feel anything I wouldnt expect from a IDE in thebrowser.
The git integration is awsome.

## How to install
To get Theai IDE to comile it is needed to encrease the swapsize. This is none by editing the file /etc/dphys-seapfile and setting changing CONF_SWAPSIZE=100 to 2048

to do that ssh into your device and do:
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

When done, there should be a log info saying "Starting THEIA IDE"
You can then open a web-browser and gå to http://picroft:3000 if your Mycroft device is picroft. If on a Mark One go to http://mark_1:3000
You then get access to the THEIA IDE in a workplace located /opt/mycroft/skills.


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
