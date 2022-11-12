def sort(elements: list, ascending: bool = True):
    for j in range(list.len):
        for i in range(len(list)):
            if list[i] > list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp
