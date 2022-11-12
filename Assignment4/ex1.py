def fib(n: int) -> int:
    f0 = 0
    f1 = 1
    if n == 0:
        return f0
    elif n == 1:
        return f1
    elif n < 0:
        return -1
    else:
        for i in range(n-1):
            temp = f1
            f1 = f0 + f1
            f0 = temp
        return f1