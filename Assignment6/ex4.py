import os


def chunks(path: str, size: int, **kwargs):
    if size < 1:
        print("Error: size must be greater or equal to 1")
        raise ValueError

    if not os.path.isfile(path):
        print("Error: path must be a files")
        raise ValueError

    with open(path, **kwargs) as f:
        while chars := f.read(size):
            yield chars

