#!python


def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement contains here (iteratively and/or recursively)
    # if pattern == '':
    #     return True
    # # if pattern[0] not in text:
    # #     return False
    # else:
    #     counter = 0
    #     for i in range(len(text)):
    #         if counter == len(pattern):
    #             return True
    #         if text[i] == pattern[counter] or text[i] == pattern[0]:
    #             counter += 1
    #         else:
    #             counter = 0
    #     if counter == len(pattern):
    #         return True
    #     else:
    #         return False

    return contains_and_first_index(text, pattern)[0]


def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    return contains_and_first_index(text, pattern)[1]


def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # Implement find_all_indexes here (iteratively and/or recursively)
    # Check if that pattern is empty
    if pattern == '':
        ret_items = []
        for i in range(len(text)):
            ret_items.append(i)
        return ret_items

    if pattern == text:
        return [0]

    start_indexes = []
    start_index = find_index_refactored(text, pattern)
    print("Start Index: {}".format(start_index))
    while start_index != None:
        start_indexes.append(start_index)
        start_index = find_index_refactored(text, pattern, start_index + 1)

    return start_indexes


def find_index_refactored(text, pattern, start=0):
    if pattern == '':
        return 0
    if pattern == text:
        return 0
    if len(pattern) > len(text):
        return None
    for index in range(start, len(text) - len(pattern) + 1):
        if text[index] == pattern[0]:
            if text[index: index+len(pattern)] == pattern:
                return index
    return None


def contains_and_first_index(text, pattern):
    # Check if that pattern is empty
    if pattern == '':
        return (True, 0)
    else:
        counter = 0  # Create a counter that will keep track of how many letters match the pattern
        index_counter = None  # Keeps track of the first index found
        index_arr = []
        for i in range(len(text)):
            index_counter = i
            if counter == len(pattern):
                # Our pattern matches our counter length so we found it! Now we can get the index by taking the index_counter subtracted by the len of the patter
                return (True, index_counter - len(pattern))
            # We found another match with the pattern, could possibly be an overlap so we test both cases
            if text[i] == pattern[counter] or text[i] == pattern[0]:
                if text[i] == pattern[counter]:  # Increase counter here
                    counter += 1
                else:
                    counter = 1  # reset the counter back to one
            else:
                counter = 0  # No pattern found yet :(
        if counter == len(pattern):
            return (True, index_counter - len(pattern) + 1)
        else:
            # we did not find any pattern, thus the text does not contain the pattern
            return (False, None)


def test_string_algorithms(text, pattern):
    print(text)
    # found = contains(text, pattern)
    # print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    # index = find_index(text, pattern)
    # print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    # indexes = find_all_indexes(text, pattern)
    # print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()
