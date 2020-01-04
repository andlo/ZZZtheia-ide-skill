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

from mycroft import MycroftSkill, intent_file_handler, MYCROFT_ROOT_PATH
import os
import tarfile
import subprocess
import signal
import shutil
from psutil import virtual_memory


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
            try:
                os.killpg(self.settings.get("theia_pid"), signal.SIGTERM)
            except Exception:
                proc = subprocess.Popen('pkill -f "yarn theia start"',
                                        cwd = self.SafePath, preexec_fn=os.setsid, shell=True)
                proc.wait()
            self.settings["theia_pid"] = None
            return True
        else:
            return False

    def run_theia(self):
        if self.settings.get("theia_pid)") is None:
            self.log.info("Starting IDE")
            theia_proc = subprocess.Popen(self.SafePath + '/theia_run.sh ' + MYCROFT_ROOT_PATH,
                                          cwd = self.SafePath, preexec_fn=os.setsid, shell=True)
            self.settings["theia_pid"] = theia_proc.pid
            return True
        else:
            return False

    def install_theia(self):
        platform = 'Unknown'
        if self.config_core.get('enclosure', {}).get('platform'):
            platform = self.config_core.get('enclosure', {}).get('platform')
        if not os.path.isfile(self.SafePath + '/theia_run.sh'):
            self.speak_dialog('install_start')
            GitRepo = 'https://api.github.com/repos/andlo/theia-for-mycroft/releases/latest'
            if platform is "mycroft_mark_1":
                self.log.info('Platform Mark_1 - ThiaIDE cant run on a this device')
                self.speak_dialog('platform_not_supported')
                self.settings['theia installed'] = 'False'
                return
            elif platform == "picroft":
                self.log.info("Downloading precompiled package for the " + platform + " platform.")
                self.speak_dialog('downloading', data={"platform": platform})
                proc = subprocess.Popen('curl -s ' + GitRepo + ' | jq -r ".assets[] ' + 
                                        ' | select(.name | contains(\\"picroft\\")) ' +
                                        ' | .browser_download_url" | wget -O theiaide.tgz -i - ' +
                                        ' >/dev/null 2>/dev/null',
                                        cwd=self.SafePath, preexec_fn=os.setsid, shell=True)
                proc.wait()
                precompiled = True

            else:
                self.log.info('Platform ' + platform + ' - no precompiled package')
                self.speak_dialog('cloning', data={"platform": platform})
                mem = int(virtual_memory().total/(1024**2))
                if mem < 4000:
                    self.log.info('Memmory on device is ' + memmory + ' that is not enough.')
                    self.log.info('Sorry.')
                    self.speak_dialog('cant.install.low.memmory')
                else:
                    self.log.info('Downloading and compiling')
                    self.log.info("Cloning and build package for the " + platform + " platform.")
                    proc = subprocess.Popen('git clone https://github.com/andlo/theia-for-mycroft.git .',
                                            cwd=self.SafePath, preexec_fn=os.setsid, shell=True)
                    proc.wait
                    precompiled = False
            try:
                if precompiled is True:
                    filename = self.SafePath + '/theiaide.tgz'
                    self.log.info("Unpacking....")
                    package = tarfile.open(filename)
                    package.extractall(self.SafePath)
                    package.close()
                    os.remove(filename)
                if precompiled is False:
                    self.log.info("Compiling THEIA IDE  - This can take a while....")
                    proc = subprocess.Popen(self.SafePath + "/build_release.sh >/dev/null 2>/dev/null",
                                          cwd=self.SafePath, preexec_fn=os.setsid, shell=True)
                    proc.wait()
                self.log.info("Installed OK")
                self.settings['theia installed'] = 'True'
                self.speak_dialog('installed_OK')
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
