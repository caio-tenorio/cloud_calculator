from subprocess import CalledProcessError

from paths.paths import CSV_PATH
from shell.shell import run_cmd


def get_stats():
    try:
        run_cmd('timeout 60s dstat --output {}'.format(CSV_PATH))
    except CalledProcessError:
        pass