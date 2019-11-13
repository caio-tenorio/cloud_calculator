import csv
from paths.paths import CSV_PATH


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
                        temp_dict[key] = value
                stats_list.append(temp_dict)
            count = count + 1

    return stats_list


def get_average_of_field(field, stats_list):
    field_values = __get_list_of_all_values_of_a_field(field, stats_list)
    avg_of_field = sum(field_values) / len(field_values)

    return avg_of_field


def __get_list_of_all_values_of_a_field(field, stats_list):
    field_values = list()
    for row in stats_list:
        field_values.append(row[field])

    return field_values
