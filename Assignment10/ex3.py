import numpy as np


# setups is a list of dicts
def create_data(setups: list[dict], seed=None) -> dict:
    data = dict()
    np.random.seed(seed)
    for d in setups:
        arr_ = np.empty(shape=d["n"], dtype=np.float32)
        arr_[:] = np.random.uniform(size=d["n"], low=d["a"], high=d["b"])
        data[f"{d['id']}"] = arr_
    return data