from shell.shell import get_cmd_output
from constants.constants import MEM_USAGE_CMD
from paths.paths import MEM_USAGE_PATH
import time


def get_mem_usage():
    mem_usage_list = list()
    t_end = time.time() + 20 * 5
    while time.time() < t_end:
        mem_usage_list.append(get_cmd_output(MEM_USAGE_CMD))
        time.sleep(5)


def get_mem_list():
    mem_list = list()
    with open(MEM_USAGE_PATH, "r") as f:
        lines = f.readlines()
        for line in lines:
            mem_list.append(int(line.strip()))

    return mem_list
