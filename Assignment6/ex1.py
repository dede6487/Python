def read_numbers(path: str) -> list:
    out = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            for word in line.split(" "):
                try:
                    i = float(word)
                    out.append(i)
                except ValueError:
                    pass
    return out

