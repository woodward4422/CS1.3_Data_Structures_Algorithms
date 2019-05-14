#!python

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace


def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # if base == 2:
    #     power = len(digits) - 1
    #     sum = 0
    #     for digit in digits:
    #         sum += (base ** power) * int(digit)
    #         power -= 1
    #     return sum

    # ...
    # ...

    # if base == 16:
    #     power = len(digits) - 1
    #     sum = 0
    #     hex_dictionary = {
    #         'a': 10,
    #         'b': 11,
    #         'c': 12,
    #         'd': 13,
    #         'e': 14,
    #         'f': 15
    #     }

    #     for digit in digits:
    #         if digit in hex_dictionary:
    #             sum += (base ** power) * hex_dictionary[digit]
    #             power -= 1
    #         else:
    #             sum += (base ** power) * int(digit)
    #             power -= 1

    #     return sum

    # ...

    power = len(digits) - 1
    running_total = 0
    for digit in digits:
        running_total += (base ** power) * string.printable.index(digit)
        power -= 1
    return running_total


def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)
    # ...

    divided_number = number
    sum = ""
    while divided_number > 0:
        remainder = divided_number % base
        sum += string.printable[remainder]
        divided_number = divided_number // base
    return sum[::-1]


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    # First decodes it to a base ten number first
    decode_digits = decode(digits, base1)
    encoded_digits = encode(decode_digits, base2)
    return encoded_digits


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = encode(digits, base1)
        print('{} in base {} is {} in base {}'.format(
            digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()
