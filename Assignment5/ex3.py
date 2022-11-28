def binary_search(elements: list, x) -> bool:

    if len(elements) == 0:
        return False

    if not isinstance(x, type(elements[0])):
        return False

    m = int(len(elements)/2)
    if len(elements) <= 0:
        return False
    if elements[m] == x:
        return True
    elif elements[m] > x:
        return binary_search(elements[:m-1], x)
    elif elements[m] < x:
        return binary_search(elements[m+1:], x)
