import csv
from paths.paths import CSV_PATH, OFFERS_CSV_PATH


def get_list_of_stats():
    stats_list = list()
    header_list = list()
    with open(CSV_PATH, "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        count = 0
        for line in csv_reader:
            if count == 5:
                header_list = line
            if count > 5:
                temp_dict = dict()
                for key in header_list:
                    for value in line:
                        if "." in value:
                            temp_dict[key] = float(value.strip())
                        else:
                            temp_dict[key] = int(value.strip())
                stats_list.append(temp_dict)
            count = count + 1

    return stats_list


def get_offers(mem, amount_of_cpu):
    rows_list = list()
    with open(OFFERS_CSV_PATH, "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        count = 0
        for line in csv_reader:
            if count > 6:
                if line[3].strip() == "OnDemand" and line[24].strip().split(" ")[0] == str(mem) \
                        and line[37] == "Linux" and line[21] == amount_of_cpu and "SQL" not in line[4] and "Unused" not in line[4] \
                        and "On Demand" in line[4] and line[8].strip() == "Hrs":
                    rows_list.append(line)
                    count += 1
            else:
                count += 1
    return rows_list


def get_average_of_field(field, stats_list):
    field_values = __get_list_of_all_values_of_a_field(field, stats_list)
    avg_of_field = sum(field_values) / len(field_values)

    return avg_of_field


def get_sum_of_field(field, stats_list):
    field_values = __get_list_of_all_values_of_a_field(field, stats_list)
    _sum = sum(field_values)
    return _sum


def __get_list_of_all_values_of_a_field(field, stats_list):
    field_values = list()
    for row in stats_list:
        field_values.append(row[field])

    return field_values
