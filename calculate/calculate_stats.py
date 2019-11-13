from utils.csv_utils import get_list_of_stats
from utils.csv_utils import get_average_of_field
from memory.mem_stats import get_mem_usage


def calculate_stats():
    total_stats = get_list_of_stats()
    received_data_avg = get_average_of_field('recv', total_stats)
    sended_data_avg = get_average_of_field('send', total_stats)

    #memory
    get_mem_usage()