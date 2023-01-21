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


for id_, arr in create_data([{"id": "classA", "n": 10, "a": 0, "b": 1.5},{"id": "classB", "n": 20, "a": 3, "b": 4},{"id": "classC", "n": (5, 10), "a": 0, "b": 10}], 0).items():
    print(id_, arr.shape)
    print(arr)
