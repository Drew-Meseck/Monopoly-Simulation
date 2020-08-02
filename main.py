import numpy as np 
import matplotlib.pyplot as plt
import multiprocessing
from multiprocessing import Pool
from Space import Space
from Player import Player
import random
import time
import pandas as pd

def create_board():
    board = []
    board.append(Space('Go', 'Corner', False))
    board.append(Space('Mediteranean Avenue', 'Brown', True))
    board.append(Space('Community Chest', 'Draw Card', False))
    board.append(Space('Baltic Avenue', 'Brown', True))
    board.append(Space('Income Tax', 'Tax', False))
    board.append(Space('Reading Railroad', 'Railroad', True))
    board.append(Space('Oriental Avenue', 'Light Blue', True))
    board.append(Space('Chance', 'Draw Card', False))
    board.append(Space('Vermont Avenue', 'Light Blue', True))
    board.append(Space('Conecticut Avenue', 'Light Blue', True))
    board.append(Space('Jail', 'Corner', False))
    board.append(Space('St. Charles Place', 'Purple', True))
    board.append(Space('Electric Company', 'Utility', True))
    board.append(Space('States Avenue', 'Purple', True))
    board.append(Space('Virginia Avenue', 'Purple', True))
    board.append(Space('Pennsylvania Railroad', 'Railroad', True))
    board.append(Space('St. James Place', 'Orange', True))
    board.append(Space('Community Chest', 'Draw Card', False))
    board.append(Space('Tennessee Avenue', 'Orange', True))
    board.append(Space('New York Avenue', 'Orange', True))
    board.append(Space('Free Parking', 'Corner', False))
    board.append(Space('Kentuky Avenue', 'Red', True))
    board.append(Space('Chance', 'Draw Card', False))
    board.append(Space('Indiana Avenue', 'Red', True))
    board.append(Space('Illinois Avenue', 'Red', True))
    board.append(Space('B. & O. Railroad', 'Railroad', True))
    board.append(Space('Atlantic Avenue', 'Yellow', True))
    board.append(Space('Ventnor Avenue', 'Yellow', True))
    board.append(Space('Water Works', 'Utility', True))
    board.append(Space('Marvin Gardens', 'Yellow', True))
    board.append(Space('Go To Jail', 'Corner', False))
    board.append(Space('Pacific Avenue', 'Green', True))
    board.append(Space('North Carolina Avenue', 'Green', True))
    board.append(Space('Community Chance', 'Draw Card', False))
    board.append(Space('Pennsylvania Avenue', 'Green', True))
    board.append(Space('Short Line', 'Railroad', True))
    board.append(Space('Chance', 'Draw Card', False))
    board.append(Space('Park Place', 'Dark Blue', True))
    board.append(Space('Luxury Tax', 'Tax', False))
    board.append(Space('Boardwalk', 'Dark Blue', True))

    return board


def create_players(n):
    players = []
    for i in range(n):
        players.append(Player(i))
    return players


def create_dice():
    return [2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 11, 11, 12]

def roll_dice(dice):
    rand = random.randint(0, len(dice) - 1)
    return dice[rand]

def round(board, players, dice):
    for player in players:
        roll = roll_dice(dice)
        player.move(roll)
        board[player.pos].increment()

def runsim(board, players, dice, iter):
    for i in range(iter):
        round(board, players, dice)

def get_names(board):
    names = []
    for space in board:
        names.append(space.name)

    return names


def get_groups(board):
    groups = []
    for space in board:
        groups.append(space.group)
    return groups

def get_counts(board):
    counts = []
    for space in board:
        counts.append(space.count)
    return counts

def main():
    board = create_board()
    players = create_players(4)
    dice = create_dice()
    iterations = len(players) * 10000

    runsim(board, players, dice, iterations)

    names = get_names(board)
    groups = get_groups(board)
    counts = get_counts(board)


    df = pd.DataFrame()
    df['names'] = names
    df['groups'] = groups
    df['counts'] = counts

    print(df)


    



if __name__ == '__main__':
    main()