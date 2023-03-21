# write a function that takes in a non-empty  array of integers that are sorted in asceding order and returns a new array of the same length with the squares of the original integres also sorted in ascending order.

array = [2, 1]

# 1st solution


def sortedSquaredArray(array):
    for idx, num in enumerate(array):
        array[idx] = num * num
    array.sort()

    return array


print(sortedSquaredArray(array=array))
