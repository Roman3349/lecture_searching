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


def linear_search(sequence: list[int], target: int) -> dict:
    """
    Linear search algorithm.
    :param sequence: (list), list of integers
    :param target: (int), target value to search
    :return: (dict), dictionary with search results information
    """
    result = {
        'positions': [],
        'count': 0,
    }
    for index, item in enumerate(sequence):
        if item == target:
            result['positions'].append(index)
            result['count'] += 1
    return result


def pattern_search(sequence: str, pattern: str) -> set:
    window_size: int = len(pattern)
    result: set = set()
    for i in range(len(sequence) - window_size + 1):
        if sequence[i:i + window_size] == pattern:
            result.add(i + window_size // 2)
    return result


def main():
    sequential_data: list[int] = read_data('sequential.json', 'unordered_numbers')
    print('Unordered sequence:', sequential_data)
    print('Linear search result:', linear_search(sequential_data, 5))
    dna_sequence: str = read_data('sequential.json', 'dna_sequence')
    print('Pattern search:', pattern_search(dna_sequence, 'TGA'))


if __name__ == '__main__':
    main()