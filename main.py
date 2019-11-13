from subprocess import CalledProcessError

from utils.csv_utils import get_list_of_stats
from shell.shell import run_cmd
from paths.paths import CSV_PATH


def run():
    try:
        run_cmd('timeout 60s dstat --output {}'.format(CSV_PATH))
    except CalledProcessError:
        pass
    stats_list = get_list_of_stats()


if __name__ == '__main__':
    run()
