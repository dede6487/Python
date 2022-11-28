def gen_range(start: int, stop: int, step: int = 1):
    if not isinstance(start, int) or not isinstance(stop, int) or not isinstance(step, int):
        print("Error: start, stop or step is not of type int")
        raise TypeError

    if step == 0:
        print("Error: step = 0")
        raise ValueError

    y = start
    while (y < stop and step > 0) or (y > stop and step < 0):
        yield y
        y += step
