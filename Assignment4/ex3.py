def create_train_test_splits(data: list, train_size: float) -> tuple:
    training = []
    test = []

    split = int(len(data)*train_size)

    for i in range(split):
        training.append(data[i])
        test.append(data[split+i])

    #doesnt yet split correctly, floats are a problem!!!!!!!!!!!!!

    return training, test

print(create_train_test_splits([], 0.5))
print(create_train_test_splits(list(range(10)), 0.5))
print(create_train_test_splits(list(range(10)), 0.67))