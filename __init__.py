from mycroft import MycroftSkill, intent_file_handler
from distutils.dir_util import copy_tree
from shutil import copyfile
from psutil import swap_memory
import os
import tarfile
import wget


class TheiaIde(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):
        self.log.info("Initialize...")
        SafePath = self.file_system.path
        AppPath = self._dir
        platform = self.config_core.get('enclosure', {}).get('platform')
        if self.settings.get('theia installed') is None:
            self.log.info(
                "Downloading precompiled package for the " + platform + " platform.")
            # getting the precompiled package depending on platform
            if platform is 'picroft':
                url = 'http://url o the install'
            elif platform is 'mark_1':
                url = 'http://url o the install'
            else:
                self.log.info(
                    "No precompiled package for your platform " + platform)
                self.speak('Platform not usefull')
                return
            try:
                filename = wget.download(url, SafePath)
            except Exception:
                self.log.error('Coundnt download precompiled package!')
            # copyfile('/home/pi/theiaide-picroft.tgz', SafePath + 'theiaide-picroft.tgz')
            try:
                package = tarfile.open(filename)
                package.extractall(SafePath)
                package.close()
                self.log.info("Installed OK")
                self.settings['theia installed'] = 'True'
                self.speak_dialog('installed_OK')
            except Exception:
                self.log.info("Theia not installed-something went wrong!")
                self.speak('Theia not installed-something went wrong!')
        if self.settings.get('theia installed') == 'True':
            self.log.info("Starting THEIA IDE")
            self.speak("theia IDE is now running")
            os.system(SafePath + '/theia_run.sh ' + SafePath)

    @intent_file_handler('ide.theia.intent')
    def handle_ide_theia(self, message):
        self.speak_dialog('ide.theia')


def create_skill():
    return TheiaIde()
