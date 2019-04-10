def string_test(text):
    word = ""
    for letter in reversed(text):
        word += letter
    if word == text:
        return True
    return False


def main():
    print(string_test("racecar"))


if __name__ == '__main__':
    main()
