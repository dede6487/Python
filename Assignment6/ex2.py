def write_dict(d: dict, path: str, encoding: str = "utf-8"):
    with open(path, "w", encoding=encoding) as f:
        for i in d:
            print(f"{i}:{i.key()}", end="")


def read_dict(path: str, encoding: str = "utf-8") -> dict:
    with open(path, "r", encoding=encoding) as f:
