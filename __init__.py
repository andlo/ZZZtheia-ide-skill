"""
skill THEIA-IDE
Copyright (C) 2018  Andreas Lorensen

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

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
        if self.settings.get("theia installed") is not True or self.settings.get("theia installed") is None:
            self.install_theia()
        if not self.pid_exists(self.settings.get("theia_pid")):
            self.settings["theia_pid"] = None
        if self.settings.get("auto_start") and self.settings.get("theia_pid") is None:
            self.run_theia()

    @intent_file_handler('stop.intent')
    def handle_ide_stop(self, message):
        if self.stop_theia():
            self.speak_dialog('ide_stopped')
        else:
            self.speak_dialog('ide_is_not_running')

    @intent_file_handler('start.intent')
    def handle_ide_start(self, message):
        url = os.uname().nodename + " kolon 3000"
        if self.run_theia():
            self.speak_dialog('ide_started', data={"url": url})
        else:
            self.speak_dialog('ide_already_running', data={"url": url})

    @intent_file_handler('restart.intent')
    def handle_ide_restart(self, message):
        url = os.uname().nodename + " kolon 3000"
        self.stop_theia()
        if self.run_theia():
            self.speak_dialog('ide_started', data={"url": url})

    def stop_theia(self):
        self.log.info("Stopping IDE")
        if self.settings.get("theia_pid") is not None:
            os.killpg(self.settings.get("theia_pid"), signal.SIGTERM)
            self.settings["theia_pid"] = None
            return True
        else:
            return False

    def run_theia(self):
        if self.settings.get("theia_pid)") is None:
            self.log.info("Starting IDE")
            theia_proc = subprocess.Popen(self.SafePath + '/theia_run.sh ' +
                                          self.SafePath, preexec_fn=os.setsid, shell=True)
            self.settings["theia_pid"] = theia_proc.pid
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
                if int(open("/etc/debian_version").read(1)) is 8:
                    url = 'https://github.com/andlo/theia-for-mycroft/releases/download/THEIA-for-Mycroft/theiaide-mark1.tgz'
            if platform == "mycroft_mark_1":
                url = 'https://github.com/andlo/theia-for-mycroft/releases/download/THEIA-for-Mycroft/theiaide-mark1.tgz'
            if platform == "mycroft_mark_2":
                url = 'https://github.com/domcross/theia-for-mycroft/releases/download/THEIA-for-Mycroft/theiaide-mark2.tgz'
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
                if self.settings.get("auto_start"):
                    url = os.uname().nodename + " kolon 3000"
                    self.speak_dialog('ide_started', data={"url": url})
                return True
            except Exception:
                self.log.info("Theia not installed - something went wrong!")
                self.speak_dialog('installed_BAD')
                return False

    def pid_exists(self, pid):
        try:
            os.kill(pid, 0)
            return True
        except Exception:
            return False


def create_skill():
    return TheiaIde()
