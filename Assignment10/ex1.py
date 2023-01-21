import numpy as np


def extend(arr: np.ndarray, size_: int, fill=None) -> np.ndarray:
    if arr.ndim != 1:
        raise ValueError
    elif arr.size >= size_:
        raise ValueError
    else:
        temp = np.empty(size_, dtype=arr.dtype)  # empty array of right size and datatype
        if fill == "mean" and np.issubdtype(arr.dtype, np.number):
            temp = np.full_like(temp, arr.sum()/arr.size)  # fill temp with fill value
        elif fill is not None:
            temp = np.full_like(temp, fill)  # fill temp with fill value
        temp[:arr.size] = np.copy(arr)  # create a copy of arr that will be stored in the respective part of temp
        return temp
