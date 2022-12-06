import os


def write_dict(d: dict, path: str = os.path.join(os.getcwd(), "dict.txt"), encoding: str = "utf-8"):
    with open(path, "w") as f:  # , encoding=encoding
        for key in d:
            print((str(d[key])).encode(encoding), file=f)
            print(key.encode(encoding), file=f)


def read_dict(path: str = os.path.join(os.getcwd(), "dict.txt"), encoding: str = "utf-8") -> dict:
    d = dict()
    with open(path, "r", encoding=encoding) as f:
        lines_ = f.readlines()
        for data, k in zip(lines_[0::2], lines_[1::2]):  # creates a list of tuples containing data and keys
            data = data[2:-2]
            k = k[2:-2]
            data = data.replace("\\n", "\n")
            k = k.replace("\\n", "\n")
            d[k] = data
    return d

