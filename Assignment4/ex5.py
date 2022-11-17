def sort(elements: list, ascending: bool = True):
    if ascending:
        for j in range(len(elements)):
            for i in range(len(elements)-1):
                if elements[i] > elements[i+1]:
                    temp = elements[i]
                    elements[i] = elements[i+1]
                    elements[i+1] = temp
    else:
        for j in range(len(elements)):
            for i in range(len(elements)-1):
                if elements[i] < elements[i+1]:
                    temp = elements[i]
                    elements[i] = elements[i+1]
                    elements[i+1] = temp
