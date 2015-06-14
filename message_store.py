"""
This is a help script to centralize the management of saving,
retriving and deleting commit messages between commits.

Will be used by the 'prepare-commit-msg', 'commit-msg' and 'post-commit' git hooks.
"""

import subprocess
import os

import config

def run_cmd_output_lines(cmd):
    """
    Runs the given command in a new subprocess and returns the output as a list of lines.
    """
    process = subprocess.Popen([cmd], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    return process.communicate()[0].split("\n")

def get_msg_file():
    """
    Returns the path to the file where the commit message is stored.
    The file is located in `$GIT_DIR/last_commit_msg`
    """
    git_dir = run_cmd_output_lines("git rev-parse --git-dir")[0]
    msg_file = git_dir + "/last_commit_msg"

    return msg_file

def delete():
    """
    Deletes the saved commit message.
    """
    filename = get_msg_file()
    if os.path.exists(filename):
        os.remove(filename)

def save(message):
    """
    Stores the message to disk.
    """
    if config.STORE_BAD_MESSAGE:
        msg_file = open(get_msg_file(), 'w')
        msg_file.write(message)
        msg_file.close()

def get():
    """
    Returns the stored commit message.
    """
    filename = get_msg_file()

    if os.path.exists(filename):
        msg_file = open(filename, 'r')
        msg = msg_file.read()
        msg_file.close()
        return msg
    else:
        return None
