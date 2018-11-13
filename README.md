# <img src='theia.png' card_color='#40DBB0' width='50' style='vertical-align:bottom'/> THEIA IDE
VS Code experience on your Mycroft device

## About
Installs and setup THEIA IDE localy on your Mycroft device

## Description
This skill installs Theia IDE on your Mycroft device. This makes it easy to make and edit skills for Mycroft. Thiea IDE integrates whith Github, and you can use mycroft tools like mycroft-msm and mycroft-msk directly from the integrated shell in the IDE.
Theia provides the VS Code experience in the browser. Developers familiar with Microsoft's VS code editor will find many familiar features and concepts.

https://www.theia-ide.org/index.html

## Warning
This skill will not install if there isnt enough free diskspace. This is mainly because the skill needs Gb swapfile to compile and run.
The instal will try to encrease swapfilesize if there is enough (more than 5 Gb) free space on the ssd card.

Be aware that mark_1 came with only  a 4 GB ssd card. So if you hassnt changed that, the skill will not install or run.

## How to install
Install the skill by ssh to your device and run this command
```
mycroft-msm install https://github.com/andlo/theia-ide-skill.git
```
Skill will then install THEIA IDE. This takes more than 15 minutes, and will slow your Mycroft device during install and when compiling node-modules.

When done, there should be a log info saying "Starting THEIA IDE" and Mycrot should tell you by voice that he has installed the skill.
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
