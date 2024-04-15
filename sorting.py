import csv
import os


def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    with open (file_path, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        data = {}
        for row in reader:
            for header, value, in row.items():
                if header not in data:
                    data[header] = [int(value)]
                else:
                    data[header].append(int(value))
    return data

def selection_sort(cisla):
    idx = 0
    for i in range(len(cisla)):
        cislo = cisla[i]
        for j in range(i, len(cisla)):
            if cisla[j] <= cislo:
                cislo = cisla[j]
                idx = j
        cisla[i], cisla[idx] = cislo, cisla[i]
    return cisla

def main():
    pass


if __name__ == '__main__':
    main()
