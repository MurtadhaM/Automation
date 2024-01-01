#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://adventofcode.com/2023/day/1

digits = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}


def read_file(path):
    """
    Read the contents of a file and return a list of lines.

    Args:
        path (str): The path to the file.

    Returns:
        list: A list of lines read from the file.
    """
    with open(path, 'r') as f:
        return f.readlines()


DEBUG = False


def process_line(line):
    """
    Process a line of text and convert it into a single integer.

    Args:
        line (str): The input line to be processed.

    Returns:
        int: The combined integer value extracted from the line.
    """

    text_numbers = ['one', 'two', 'three', 'four',
                    'five', 'six', 'seven', 'eight', 'nine']
    new_line = []

    for i in range(0, len(line)):
        if DEBUG:
            print(f'line[{i}] = {line[i]}')
        if line[i].isdigit():
            new_line.append(line[i])
        else:
            for text_number in text_numbers:
                if DEBUG:
                    print(f'line[{i}:] = {line[i:]}')
                    print(f'text_number = {text_number}')
                if line[i:].startswith(text_number):
                    new_line.append(str(digits[text_number]))
                    break
    if DEBUG:
        print(f'new_line = {new_line}')
    combined = new_line[0] + new_line[-1]
    return int(combined)


def process(read_file, process_line):
    """
    Process the lines from a file using a given function.

    Args:
        read_file (function): A function that reads the file and returns a list of lines.
        process_line (function): A function that processes a single line and returns a value.

    Returns:
        None
    """
    lines = read_file('input.txt')
    total = 0
    values = []
    for line in lines:
        if DEBUG:
            print(f'line = {line}')
            print(f'process_line(line) = {process_line(line)}')
        values.append(process_line(line))
        total += process_line(line)
    print(f'Total: {total}')


if __name__ == '__main__':
    process(read_file, process_line)
