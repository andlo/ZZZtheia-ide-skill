from mycroft import MycroftSkill, intent_file_handler
from distutils.dir_util import copy_tree
from shutil import copyfile
from psutil import swap_memory
import os


class TheiaIde(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):
        self.log.info("Initialize...")
        SafePath = self.file_system.path
        AppPath = self._dir
        if self.settings.get('theia installed') is None:
            try:
                mem = swap_memory()
                if (int(mem.total/1024/1024)) > 2000:
                    self.speak_dialog('install_start')
                    copy_tree(AppPath + '/files/', SafePath)
                    copyfile(AppPath + '/files/.editorconfig',
                             '/opt/mycroft/skills/.editorconfig')
                    os.system(SafePath + '/install.sh ' + SafePath +
                              ' 2>/dev/null 1>/dev/null')
                    self.log.info("THEIA IDE is installed and configured")
                    self.settings['theia installed'] = 'True'
                    self.speak_dialog('installed_OK')
                else:
                    self.log.error("Not enough memmory. Encrease swap size!")
                    self.speak_dialog('not_enough_swap')
            except Exception:
                self.log.error("THEIA IDE is NOT installed")
                self.speak_dialog('installed_BAD')
        if self.settings.get('theia installed') == 'True':
                self.log.info("Starting THEIA IDE")
                os.system(SafePath + '/run_theia.sh ' +
                          SafePath + ' 2>/dev/null 1>/dev/null &')

    @intent_file_handler('ide.theia.intent')
    def handle_ide_theia(self, message):
        self.speak_dialog('ide.theia')


def create_skill():
    return TheiaIde()
