'''
Write a program to find the smallest number in the list. Make your program as readable as possible.

Assumption :  constantly increasing list of numbers has been given which are shifted right or left by k values.
'''


def findMinimum(array):
    # iterate over the enumerated array for both index and value
    for i, val in enumerate(array):
        # initalize min value with first index value of array
        if i == 0:
            min = val
        # for every value compare with minimum if true assign new value
        if (val < min):
            min = val
    # return value
    return min



array = [42, 49, 86, 143, 234, 334, 401, 435, 2, 14, 21]
print(findMinimum(array))




