from __future__ import unicode_literals
#
# gitmodules.py - A module for willie, to update additional modules on a git repository
#
# Copyright 2014 Niko Usai - mogui.it
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#   http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#
# this module requires sh package installed
#
import willie
import subprocess
import os

@willie.module.commands('gitmodules')
@willie.module.rate(5)
def gitmodules(bot, trigger):
    try:
        # asd
        repository = bot.config.gitmodules.repo
        path       = bot.config.gitmodules.path
    except:
        bot.say("No repository is configured in the settings")
    else:
        print(repository, path)
        if not os.path.exists(path):
            # clone repository
            failed = subprocess.check_call(['git', 'clone', repository, path])
            if failed:
                bot.say("ERROR: repository not cloned")
            else:
                bot.say("Cloned repository")
        res = subprocess.check_output([ 'git','--work-tree', path,'--git-dir',path+'/.git', 'pull'])
        bot.say(res)
