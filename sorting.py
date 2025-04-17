import os
import csv

def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, "r") as f:
        reader = csv.DictReader(f) ## jednotlive hodnoty z radku se priradi pod klic ktery je v hlavicce
        data = {"series_1":[], "series_2":[], "series_3":[]}
        for row in reader:
            # print(row)
            for key, value in row.items():
                # print(key)
                # print(value)
                data[key].append(int(value))
    return data


print(read_data("V:/BPC - PRG2/lecture_sorting/numbers.csv"))

def selection_sort(numbers, direction):
    for i in range(len(numbers)):
        min_index = i
        if direction == "up":
            for j in range(i + 1, len(numbers)):
                if numbers[j] < numbers[min_index]:
                    min_index = j
            numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
        if direction == "down":
            for j in range(i + 1, len(numbers)):
                if numbers[j] > numbers[min_index]:
                    min_index = j
            numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
    return numbers


numbers = [1,9,5,12,36,29,96,85,2,0,87]
print(selection_sort(numbers, "down"))

def main():
    pass


if __name__ == '__main__':
    main()
