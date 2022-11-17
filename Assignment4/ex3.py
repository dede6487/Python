from math import floor


def create_train_test_splits(data: list, train_size: float) -> tuple:
    training = []
    test = []

    split = floor(len(data) * train_size)

    for i in range(split):
        training.append(data[i])

    for i in range(split, len(data)):
        test.append(data[i])

    return training, test
