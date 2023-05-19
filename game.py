"""Игра угадай число"""

import numpy as np

def game(number: int, predict_number: int):
    # if not number:
    #    number = np.random.randint(1, 101)  # загадываем число
    if predict_number > number:
        return "less"
    elif predict_number < number:
        return "more"
    else:
        return "exact"

