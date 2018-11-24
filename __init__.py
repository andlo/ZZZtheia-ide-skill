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
        if not self.process_exists("theia_run.sh"):
            self.theia_process = None
        if self.settings.get("theia installed") is not True or self.settings.get("theia installed") is None:
            self.install_theia()
        if self.settings.get("auto_start") is True:
            self.run_theia()

    @intent_file_handler('stop.intent')
    def handle_ide_stop(self, message):
        if self.stop_theia():
            self.speak_dialog('ide_stopped')
        else:
            self.speak_dialog('ide_is_not_running')

    @intent_file_handler('start.intent')
    def handle_ide_start(self, message):
        url = "http://" + os.getenv('HOSTNAME') + ":3000"
        if self.run_theia():
            self.speak_dialog('ide_started', data={"url": url})
        else:
            self.speak_dialog('ide_alreddy_running', data={"url": url})

    @intent_file_handler('restart.intent')
    def handle_ide_restart(self, message):
        url = "http://" + os.getenv('HOSTNAME') + ":3000"
        self.stop_theia()
        if self.run_theia():
            self.speak_dialog('ide_started', data={"url": url})

    def stop_theia(self):
        self.log.info("Stopping IDE")
        if self.theia_process is not None and self.process_exists("theia_run.sh"):
            os.killpg(self.theia_process.pid, signal.SIGKILL)
            if self.theia_process is not None:
                self.theia_process = None
            return True
        else:
            return False

    def run_theia(self):
        if self.theia_process is None and not self.process_exists("theia_run.sh"):
            self.log.info("Starting IDE")
            self.theia_process = subprocess.Popen(self.SafePath + '/theia_run.sh ' +
                                                  self.SafePath, preexec_fn=os.setsid, shell=True)
            return True
        else:
            return False

    def install_theia(self):
        platform = self.config_core.get('enclosure', {}).get('platform')
        if not os.path.isfile(self.SafePath + '/theia_run.sh'):
            self.speak_dialog('install_start')
            self.log.info(
                "Downloading precompiled package for the " + platform + " platform.")
            self.speak_dialog('downloading', data={"platform": platform})
            if platform == "picroft":
                url = 'https://github.com/andlo/theia-for-mycroft/releases/download/THEIA-for-Mycroft/theiaide-picroft.tgz'
            if platform == "mycroft_mark_1":
                url = 'https://github.com/andlo/theia-for-mycroft/releases/download/THEIA-for-Mycroft/theiaide-mark1.tgz'
            try:
                filename = wget.download(url, self.SafePath + '/theiaide.tgz')
                self.log.info("Unpacking....")
                package = tarfile.open(filename)
                package.extractall(self.SafePath)
                package.close()
                os.remove(filename)
                copyfile(self._dir + '/files/.editorconfig',
                         '/opt/mycroft/skills/.editorconfig')
                self.log.info("Installed OK")
                self.settings['theia installed'] = 'True'
                self.speak_dialog('installed_OK')
                return True
            except Exception:
                self.log.info("Theia not installed - something went wrong!")
                self.speak_dialog('installed_BAD')
                return False

    def process_exists(self, proc_name):
        tmp = os.popen("ps -ax | grep " + proc_name).read()
        proccount = tmp.count(proc_name)
        if proccount > 2:
            return True
        else:
            return False


def create_skill():
    return TheiaIde()
