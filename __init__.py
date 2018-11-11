from mycroft import MycroftSkill, intent_file_handler
from distutils.dir_util import copy_tree
from shutil import copyfile
import os


class TheiaIde(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):
        self.log.info("Initialize...")
        SafePath = self.file_system.path
        AppPath = self._dir
        if self.settings.get('theia installed') is None:
            copy_tree(AppPath + '/files/', SafePath)
            copyfile(AppPath + '/files/.editorconfig', '/opt/mycroft/skills/.editorconfig')
            os.system(SafePath + '/install.sh ' + SafePath +
                      ' >' + SafePath + '/install.log')
            # Some error checking would be fine here ;)
            self.log.info("THEIA IDE is installed and configured")
            self.settings['theia installed'] = 'True'
        self.log.info("Starting THEIA IDE")
        os.system(SafePath + '/run_theia.sh ' + SafePath + ' &')

    @intent_file_handler('ide.theia.intent')
    def handle_ide_theia(self, message):
        self.speak_dialog('ide.theia')


def create_skill():
    return TheiaIde()
