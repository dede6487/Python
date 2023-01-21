import numpy as np
import random


def create_minefield(rows: int, cols: int, n_mines: int, seed=None) -> np.ndarray:
    if n_mines <= 1 or n_mines >= rows*cols:
        raise ValueError

    # determine where to put the "mines"
    mines = np.zeros(n_mines, dtype=int)
    j = 0
    while j < n_mines:
        temp = random.randint(0, rows*cols)
        if temp not in mines:
            mines[j] = temp
            j += 1

    arr = np.zeros(rows*cols, dtype=int)

    for i in mines:
        arr[i] = -1

    arr = arr.reshape((rows, cols))
    return arr


print(create_minefield(7, 7, 3, 0))
