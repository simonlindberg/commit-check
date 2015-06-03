"""
This is a help script to centralize the management of saving,
retriving and deleting commit messages between commits.

Will be used by the 'prepare-commit-msg', 'commit-msg' and 'post-commit' git hooks.
"""

import subprocess
import os

def get_msg_file():
    git_dir = subprocess.Popen(["git rev-parse --git-dir"], stdout = subprocess.PIPE, stderr = subprocess.STDOUT, shell = True).communicate()[0].split("\n")[0]
    msg_file = git_dir + "/last_commit_msg"

    return msg_file

def delete():
    filename = get_msg_file()
    if os.path.exists(filename):
        os.remove(filename)

def save(message):
    file = open(get_msg_file(), 'w')
    file.write(message)
    file.close()

def get():
    filename = get_msg_file()

    if os.path.exists(filename):
        file = open(filename, 'r')
        msg = file.read()
        file.close()
        return msg
    else:
        return None
