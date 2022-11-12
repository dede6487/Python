def clip(*values, min_=0, max_=1) -> list:
    temp = []
    for v in values:
        if v < min_:
            temp.append(min_)
        elif v > max_:
            temp.append(max_)
        else:
            temp.append(v)
    return temp
