def read_numbers(path: str) -> list:
    out = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            for word in line.split(" "):
                try:
                    i = int(word)
                    out.append(i)
                except ValueError:
                    pass
                    try:
                        f = float(word)
                        out.append(f)
                    except ValueError:
                        pass
    return out


print(read_numbers("ex1_data.txt"))
