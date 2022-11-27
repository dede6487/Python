def gen_range(start: int, stop: int, step: int = 1):
    if not isinstance(start, int) or not isinstance(stop, int) or not isinstance(step, int):
        print("Error: start, stop or step is not of type int")
        raise TypeError

    if step == 0:
        print("Error: step = 0")
        raise ValueError

    y = start
    while True:
        yield y
        y += step
        if y >= stop:
            break


print(list(gen_range(0, 10)))
print(list(gen_range(0, 10, 3)))
print(list(gen_range(0, 10, -1))) #not yet working
print(list(gen_range(10, 0)))
print(list(gen_range(10, 0, -2)))
print(list(gen_range(-10, -3, 2)))
print(list(gen_range(0.0, 10)))
print(list(gen_range(0, 10, 0)))
