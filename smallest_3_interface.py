'''
Write a program to find the smallest number in the list. Make your program as extendible and flexible as possible.

Assumption :  constantly increasing list of numbers has been given which are shifted right or left by k values.
'''

import abc


class MinimumInterface(abc.ABC):
    '''
    We can implement this method for strings or objects
    '''

    @abc.abstractmethod
    def findMinimum(self):
        pass


class MinimumNumberImplementation(MinimumInterface):

    def findMinimum(self, array):
        if len(array) == 1:
            return array[0]
        last_element = len(array) - 1
        # increasing list with no rotation
        if array[0] < array[last_element]:
            return array[0]
        # find middle of the array
        mid_element = int((0 + last_element) / 2)
        # what if middle element is the minimum
        if mid_element < last_element and array[mid_element] < array[mid_element - 1]:
            return array[mid_element]
        # check with the next element if we can find the shift in the
        if mid_element < last_element and array[mid_element] > array[mid_element + 1]:
            return array[mid_element + 1]
        # Now choose the half and call again
        if array[last_element] > array[mid_element]:
            return self.findMinimum(array[0: mid_element])
        else:
            return self.findMinimum(array[mid_element: last_element + 1])


def main():
    array = [42, 49, 86, 143, 234, 334, 401, 435, 2, 14, 21]
    min_int = MinimumNumberImplementation()
    print(min_int.findMinimum(array))


if __name__ == "__main__":
    main()
