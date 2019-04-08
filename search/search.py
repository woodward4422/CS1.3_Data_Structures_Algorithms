#!python


def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here
    ''' Parameter array: An array that will be searched through
        Parameter item: The search target that we are looking for
        Parameter index: The index to be used to be used in the recursive calls to keep track of what index to search
        Return: Returns either the index of the found item or None if the item is not found
     '''
    # Base case that handles when the element is not found in the array
    if index > len(array) - 1:
        return None
    # Base case that handles when the element has been found
    else:
        if array[index] == item:
            return index
        # recursively call the function with a passed in index incremented
        return linear_search_recursive(array, item, index + 1)


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    ''' Parameter array: An array that will be searched through
        Parameter item: The search target that we are looking for
        Return: Returns either the index of the found item or None if the item is not found
     '''
    lower = 0  # lower boundary that we are searching for
    upper = len(array) - 1  # upper boundry
    while lower <= upper:
        # Find the middle of the current array that we are searching through
        mid = (lower + upper) // 2
        if array[mid] == item:
            return mid  # found
        elif array[mid] < item:  # set our new boundaries
            lower = mid + 1  # Set boundary for the right side of the array
        else:
            upper = mid - 1  # Set boundary for left side of the array
    return None


def binary_search_recursive(array, item, left=None, right=None):

    pass
