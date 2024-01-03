
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://adventofcode.com/2023/day/2


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


class GAME:

    def __init__(self, input):
        # INPUT IS A LIST OF LISTS
        # input.split(' ')
        self.id = input.split(':')[0]
        self.SETS = []
        self.create_sets(input.split(':')[1].split(';'))

    def create_sets(self, inputSets):
        SET = []
        for i in range(0, len(inputSets)):
            SET.append(inputSets[i].strip().split(' '))
            self.SETS = SET

    def get_id(self):
        return self.id

    def get_sets(self):
        formatted_sets = dict({"red": 0, "green": 0, "blue": 0})
        mySets = []
        for set in self.SETS:
            for color in set:
                if color == 'red':
                    formatted_sets['red'] += 1
                elif color == 'green':
                    formatted_sets['green'] += 1
                elif color == 'blue':
                    formatted_sets['blue'] += 1
            mySets.append(formatted_sets)
        return mySets

    def get_rules(self):
        return self.Rules

    def get_max(self):
        return self.max

    def get_min(self):
        return self.min

    def __str__(self):
        return f'GAME: {self.id}'

    def is_allowed(self, color):
        return color in self.Rules
GAMES = []
input = read_file('input.txt')
print(f'GAMES: {GAMES}')
for line in input:

    GAMES.append(GAME(line))
    print(f'Game: {line}')
    CurrentGame = GAME(line)
    print(f'CurrentGame: {CurrentGame}')
    print(f'CurrentGame.id: {CurrentGame.id}')
    print(f'CurrentGame.SETS: {CurrentGame.SETS}')
    sets = CurrentGame.get_sets()
    print(f'colors: {sets[0].items()}')
    print(f'CurrentGame.get_sets(): {CurrentGame.get_sets()}')
