import os
import json
from typing import Union

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name: str, field: str) -> Union[list[int], str, None]:
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data[field] if field in data else None


def main():
    sequential_data = read_data('sequential.json', 'unordered_numbers')
    print(sequential_data)


if __name__ == '__main__':
    main()