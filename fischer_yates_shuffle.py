import random


def fisher_yates_shuffle(arr):

    for i in range(len(arr)):
        random_index = random.randint(i, len(arr) - 1)
        arr[random_index], arr[i] = arr[i], arr[random_index]

    return arr


print(fisher_yates_shuffle([1, 2, 3, 4, 5, 6, 7, 8, 9]))
