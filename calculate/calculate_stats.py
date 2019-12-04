from utils.csv_utils import get_list_of_stats
from utils.csv_utils import get_average_of_field, get_sum_of_field, get_offers
from memory.mem_stats import get_mem_list
from shell.shell import get_cmd_output, run_cmd
from paths.paths import CSV_PATH, MEM_USAGE_PATH


def calculate_stats():
    stats_dict = dict()
    stats_list = get_list_of_stats()
    mem_list = get_mem_list()
    mem_avg = sum(mem_list) / len(mem_list)
    mem_max = float(max(mem_list)/1000.00)
    received_data_avg = get_average_of_field('recv', stats_list)
    sended_data_avg = get_average_of_field('send', stats_list)
    sum_sent_data = get_sum_of_field('send', stats_list)

    stats_dict["rec_avg"] = received_data_avg
    stats_dict["sent_sum"] = (((sum_sent_data/1024)/1024)/1024) * 43800
    stats_dict["mem_avg"] = mem_avg/1000

    if stats_dict["sent_sum"] < 1.0:
        network_cost = 0.0
    elif stats_dict["sent_sum"] > 1 and stats_dict["sent_sum"]/1000.00 <= 10.0:
        network_cost = stats_dict["sent_sum"] * 0.09
    elif 10 < stats_dict["sent_sum"]/1000.00 <= 40.0:
        network_cost = stats_dict["sent_sum"] * 0.085
    elif 40 < stats_dict["sent_sum"]/1000.00 <= 150.0:
        network_cost = stats_dict["sent_sum"] * 0.07
    elif stats_dict["sent_sum"]/1000.00 > 150.0:
        network_cost = stats_dict["sent_sum"] * 0.05

    if 4 < mem_max < 8:
        mem = 8
    elif 8 < mem_max < 16:
        mem = 16
    elif 16 < mem_max < 32:
        mem = 32
    elif 32 < mem_max < 64:
        mem = 64
    amount_of_cpu = get_cmd_output('nproc --all').strip()

    offers_list = get_offers(mem, amount_of_cpu)

    for offer in offers_list:
        price = float(offer[9]) * 730
        total = float(price) + float(network_cost)
        print "Instance type: " + offer[18] + ", Cost: " + str(total) + ", USD per month " + ", CPU: " + offer[22] + ", CPU cores: " + offer[21] + ", Memory: " + offer[24] + ", Storage: " + offer[25]

        # TODO: printar nome da maquina e custo total



    run_cmd('rm {}'.format(CSV_PATH))
    run_cmd('rm {}'.format(MEM_USAGE_PATH))

