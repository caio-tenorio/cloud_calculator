from shell.shell import get_cmd_output
from constants.constants import MEM_USAGE_CMD
import time


def get_mem_usage():
    mem_usage_list = list()
    t_end = time.time() + 60 * 5
    while time.time() < t_end:
        mem_usage_list.append(get_cmd_output(MEM_USAGE_CMD))

    return mem_usage_list
