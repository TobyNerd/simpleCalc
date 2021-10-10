from art import *

from functions.math import Subtraction, Division, Summation
from functions.util import PlayMusic


def startup_prompt():
    PlayMusic.play_music()
    print('--------------------------')
    print('Specify type of operation.')
    print('--------------------------')
    print('1. Summation of x amount of values'
          '\n2. Subtraction of y from x'
          '\n3. Division of x by y')

    calc_input = input("\nSpecify calculation: ")

    if calc_input == '1':
        Summation.calculate_summation()
    elif calc_input == '2':
        Subtraction.calculate_subtraction()
    elif calc_input == '3':
        Division.calculate_division()
    elif calc_input not in ('1', '2', '3'):
        for i in range(0, 10):
            print("no trolling plz goober")
    startup_prompt()


if __name__ == '__main__':
    tprint("simplecalc", "Doh")
    startup_prompt()
