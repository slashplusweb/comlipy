import os
import stat
import sys

from comlipy.hook_template import commit_msg_template
from comlipy.lib.color import Color


def detect_git_path(path: str) -> str:
    """
    Detect the git path by iterative traversing the `path` up until
    either the project path has been found or there is no parent path

    Returns:
        str: the verified .git path
    """
    while not is_git_path(path):
        parent_path = os.path.dirname(path)
        if parent_path == path:
            return ''
        path = parent_path

    return os.path.realpath(os.path.join(path, '.git'))


def is_git_path(path: str) -> bool:
    """
    Check if the given `path` can be verified as git path by checking it against the `.git` directory

    Returns:
        bool: whether `path` is the .git project path
    """
    detection_path = os.path.join(path, '.git')

    return os.path.exists(detection_path) and os.path.isdir(detection_path)


def render_commit_hook(git_path: str, config_file_path: str = None):
    """
    Render the commit-msg hook from template in 'hook_template.py'

    Args:
        git_path(str):
        config_file_path(str): config_file_path:
    """
    output_file = os.path.realpath(os.path.join(git_path, 'hooks', 'commit-msg'))

    if os.path.exists(output_file):
        yesno = None
        while yesno not in ('y', 'n', 'yes', 'no'):
            if yesno is not None:
                Color.print('Invalid input: {!r}'.format(yesno), color='yellow')
            yesno = input('commit-msg hook already exists, but is older than template, overwrite? [Yn] ')
            if yesno == '':
                yesno = 'y'
            yesno = yesno.lower()
        if yesno in ('n', 'no'):
            sys.exit(1)

    try:
        with open(output_file, 'wb') as file:
            config = '-c "{!s}" '.format(config_file_path) if config_file_path else ''
            file.write(commit_msg_template.format(config=config, ).encode())
            st = os.stat(output_file)
            os.chmod(output_file, st.st_mode | stat.S_IEXEC)
    except IOError as error:
        Color.print('commit-msg output could not be saved', color='red')
        Color.print(str(error), color='yellow')
        sys.exit(1)

    if config_file_path:
        print('commit-msg hook successfully created with comlipy-config path {!r}'.format(config_file_path))
    else:
        print('commit-msg hook successfully created'.format(config_file_path))
