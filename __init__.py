from mycroft import MycroftSkill, intent_file_handler
from shutil import copyfile
import os
import tarfile
import wget
import subprocess
import signal


class TheiaIde(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):
        self.log.info("Initialize THEIA IDE...")
        self.SafePath = self.file_system.path
        self.theia_process = None
        if not self.settings.get("theia installed") is True or self.settings.get("theia installed") is None:
            self.install_theia()
        if self.settings.get("auto_start") is True:
            self.handle_ide_start()

    @intent_file_handler('ide.theia.intent')
    def handle_ide_theia(self, message):
        self.speak_dialog('ide.theia')

    @intent_file_handler('stop.intent')
    def handle_ide_stop(self, message):
        self.log.info("Stopping IDE")
        os.killpg(self.theia_process.pid, signal.SIGKILL)
        self.speak_dialog('IDE stopped')

    @intent_file_handler('start.intent')
    def handle_ide_start(self, message):
        if self.theia_process is None:
            self.log.info("Starting IDE")
            self.theia_process = subprocess.Popen(self.SafePath + '/theia_run.sh ' +
                                                  self.SafePath, preexec_fn=os.setsid, shell=True)
            self.speak_dialog('IDE started')
        else:
            self.speak_dialog('IDE alreddy running')

    def install_theia(self):
        platform = self.config_core.get('enclosure', {}).get('platform')
        if not os.path.isfile(self.SafePath + '/theia_run.sh'):
            self.speak_dialog('install_start')
            self.log.info(
                "Downloading precompiled package for the " + platform + " platform.")
            self.speak_dialog(
                "Downloading precompiled package for the " + platform + " platform.")
            # getting the precompiled package depending on platform
            if platform == "picroft":
                url = 'https://github.com/andlo/theia-for-mycroft/releases/download/THEIA-for-Mycroft/theiaide-picroft.tgz'
            if platform == "mycroft_mark_1":
                url = 'https://github.com/andlo/theia-for-mycroft/releases/download/THEIA-for-Mycroft/theiaide-mark1.tgz'
            try:
                filename = wget.download(url, self.SafePath + '/theiaide.tgz')
                self.speak_dialog('Unpacking theia IDE...')
                package = tarfile.open(filename)
                package.extractall(self.SafePath)
                package.close()
                os.remove(filename)
                copyfile(self._dir + '/files/.editorconfig',
                         '/opt/mycroft/skills/.editorconfig')
                self.log.info("Installed OK")
                self.settings['theia installed'] = 'True'
                self.speak_dialog('installed_OK')
            except Exception:
                self.log.info("Theia not installed-something went wrong!")
                self.speak_dialog('installed_BAD')


def create_skill():
    return TheiaIde()
