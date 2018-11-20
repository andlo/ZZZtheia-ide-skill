from mycroft import MycroftSkill, intent_file_handler
from shutil import copyfile
import os
import tarfile
import wget


class TheiaIde(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):
        self.log.info("Initialize...")
        SafePath = self.file_system.path
        platform = self.config_core.get('enclosure', {}).get('platform')
        self.log.info(platform)
        self.speak_dialog(platform)
        if self.settings.get('theia installed') is None:
            self.speak_dialog('install_start')
            self.log.info(
                "Downloading precompiled package for the " + platform + " platform.")
            # getting the precompiled package depending on platform
            if platform == 'picroft':
                url = 'https://github.com/andlo/theia-for-mycroft/releases/download/THEIA-for-Mycroft/theiaide-picroft.tgz'
            elif platform == "mycroft_mark_1":
                url = 'https://github.com/andlo/theia-for-mycroft/releases/download/THEIA-for-Mycroft/theiaide-picroft.tgz'
            else:
                self.log.info(
                    "No precompiled package for your platform " + platform)
                self.speak_dialog('Platform not usefull')
                return
            try:
                filename = wget.download(url, SafePath)
            except Exception:
                self.log.error('Coundnt download precompiled package!')
            try:
                package = tarfile.open(filename)
                package.extractall(SafePath)
                package.close()
                copyfile(self._dir + '/files/.editorconfig',
                         '/opt/mycroft/skills/.editorconfig')
                self.log.info("Installed OK")
                self.settings['theia installed'] = 'True'
                self.speak_dialog('installed_OK')
            except Exception:
                self.log.info("Theia not installed-something went wrong!")
                self.speak_dialog('installed_BAD')
        if self.settings.get('theia installed') == 'True':
            self.log.info("Starting THEIA IDE")
            os.system(SafePath + '/theia_run.sh ' + SafePath)

    @intent_file_handler('ide.theia.intent')
    def handle_ide_theia(self, message):
        self.speak_dialog('ide.theia')


def create_skill():
    return TheiaIde()
