def flatten(nested: list) -> list:
    out = []
    for e in nested:
        if not isinstance(e, list):
            out.append(e)
        else:
            for i in flatten(e):
                out.append(i)
    return out
