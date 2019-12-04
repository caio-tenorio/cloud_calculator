import threading
import time
from utils.csv_utils import get_list_of_stats
from memory.mem_stats import get_mem_usage
from stats.stats import get_stats
from calculate.calculate_stats import calculate_stats


def start_stats_get():
    get_stats_thread = threading.Thread(target=get_stats)
    get_stats_thread.start()
    get_mem_stats_thread = threading.Thread(target=get_mem_usage)
    get_mem_stats_thread.start()

    while get_stats_thread.isAlive() and get_mem_stats_thread.isAlive():
        print "Waiting for stats gathering!!!"
        time.sleep(10)

    print "threads are dead"


def run():
    start_stats_get()
    calculate_stats()


if __name__ == '__main__':
    run()
