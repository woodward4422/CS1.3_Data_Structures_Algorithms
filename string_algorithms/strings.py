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
    # TODO: Implement find_all_indexes here (iteratively and/or recursively)


def contains_and_first_index(text, pattern):
    if pattern == '':
        return (True, 0)
    else:
        counter = 0
        index_counter = None
        for i in range(len(text)):
            index_counter = i
            if counter == len(pattern):
                return (True, index_counter - len(pattern))
            if text[i] == pattern[counter] or text[i] == pattern[0]:
                if text[i] == pattern[counter]:
                    counter += 1
                else:
                    counter = 1
            else:
                counter = 0
        if counter == len(pattern):
            return (True, index_counter - len(pattern) + 1)
        else:
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
