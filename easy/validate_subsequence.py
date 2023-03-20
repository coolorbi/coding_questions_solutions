# check if sub sequence exists in the array.


def isValidSubsequence(array, sequence):
    # Write your code here.
    index = 0
    for num in array:
        if num == sequence[index]:
            index = index + 1
        if index == len(sequence):
            return True
    return False


array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [22, 25, 6]
print(isValidSubsequence(array, sequence))

# time complexity: 0(N) because we have to travese whole array with the length of N

# space complexity will be constant o(1) because we are storing constant value, because storage is not increasing according to the size of the array.
