#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
'''

abc -> cba
cab
bac
cba
'''


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    return is_palindrome_iterative(text)
    # return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    # Normalize the string to ignore punctiation and whitespace
    sanitized_string = normalize_string(text)
    word = ""
    # Go through the string backwards, and append to a new string
    for letter in reversed(sanitized_string):
        word += letter
    # Check if the strings are the same
    if word == sanitized_string:
        return True
    return False


def is_palindrome_recursive(text, left=None, right=None):
    # TODO: implement the is_palindrome function recursively here

    # once implemented, change is_palindrome to call is_palindrome_recursive
    # to verify that your iterative implementation passes all tests

    normalized_string = normalize_string(text)

    if left == None:
        left = 0
        right = len(normalized_string) - 1

    if left > right:
        return True

    if normalized_string[left] != normalized_string[right]:
        return False

    return is_palindrome_recursive(normalized_string, left + 1, right - 1)


def normalize_string(text):
    lower_case = text.lower()
    no_white_space = lower_case.replace(" ", "")
    no_punctuation = no_white_space.translate(
        str.maketrans('', '', string.punctuation))
    return no_punctuation


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
