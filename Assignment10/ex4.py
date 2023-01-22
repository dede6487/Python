import numpy as np
import random


def create_minefield(rows: int, cols: int, n_mines: int, seed=None) -> np.ndarray:
    if n_mines < 1 or n_mines >= rows*cols or rows < 2 or cols < 2:
        raise ValueError

    # determine where to put the "mines"
    mines = np.zeros(n_mines, dtype=int)
    j = 0
    while j < n_mines:
        temp = random.randint(0, rows*cols - 1)
        if temp not in mines:
            mines[j] = temp
            j += 1

    arr = np.zeros(rows*cols, dtype=int)

    for i in mines:
        if i % cols != 0:
            arr[i - 1] += 1
        if i % cols != cols - 1:
            arr[i + 1] += 1
        if i >= cols:
            arr[i - cols] += 1
            if i % cols != 0:
                arr[i - cols - 1] += 1
            if i % cols != cols - 1:
                arr[i - cols + 1] += 1
        if i < cols*(rows - 1):
            arr[i + cols] += 1
            if i % cols != 0:
                arr[i + cols - 1] += 1
        if i < cols * (rows - 1) - 1 and i % cols != cols - 1:
            arr[i + cols + 1] += 1

    for i in mines:
        arr[i] = -1  # placing mines

    arr = arr.reshape((rows, cols))
    return arr
