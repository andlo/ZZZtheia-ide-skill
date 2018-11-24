# <img src='theia.png' card_color='#40DBB0' width='50' style='vertical-align:bottom'/> THEIA IDE
VS Code experience on your Mycroft device.

## About
Installs and setup THEIA IDE localy on your Mycroft device

## Description
This skill installs Theia IDE on your Mycroft device. This makes it easy to make and edit skills for Mycroft. Thiea IDE integrates whith Github, and you can use mycroft tools like mycroft-msm and mycroft-msk directly from the integrated shell in the IDE.
Theia provides the VS Code experience in the browser.
People familiar with Microsoft's VS Code editor will find many familiar features and concepts.

https://www.theia-ide.org/index.html

<img src='screenshot.png' card_color='#40DBB0' width=800 style='vertical-align:bottom'/>

## How to install
Install the skill by running this command
```
mycroft-msm install https://github.com/andlo/theia-ide-skill.git
```
Skill will then install THEIA IDE. Duing installation a precompiled package is downloaded and extracted.

When done, there should be a log info saying "Starting THEIA IDE" and Mycrot should tell you by voice that he has installed the skill.
You can then open a web-browser and gå to http://picroft:3000 if your Mycroft device is picroft. If on a Mark One go to http://mark_1:3000
You then get access to the THEIA IDE in a workplace located /opt/mycroft/skills.

Skillsettings on https://home.mycroft.ai/ have one checkboks for setting auto start or not.

## Mark 1
On Mark_ the firewall needs to be open. SSH to your mark_1 and run the follow command
```
sudo ufw allow from any to any port 3000 proto tcp
```

## Updating THEIA IDE
For now, to update the THEIA IDE remove and reinstall this skill.

## Examples
* "Start IDE"
* "Stop IDE"
* "Restart IDE"

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
