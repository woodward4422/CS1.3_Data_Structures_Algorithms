from redacted import Solution
import unittest

if not hasattr(unittest.TestCase, 'assertCountEqual'):
    unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual


class RedactedTest(unittest.TestCase):
    def test_all_words(self):
        sol = Solution()
        all_words = ["Hello", "Noah", "Dog"]
        all_banned_words = ["Hello", "Noah", "Dog"]
        assert sol.redact_problem(all_words, all_banned_words) == []

    def test_no_words(self):
        sol = Solution()
        no_words = ["dog", "cow", "chicken"]
        no_words_banned = ["eggs", "rice", "beans"]
        assert sol.redact_problem(no_words, no_words_banned) == [
            "dog", "cow", "chicken"]

    def test_some_words(self):
        sol = Solution()
        some_words = ["dog", "cat", "mouse"]
        some_banned_words = ["cat", "mouse", "chicken"]
        assert sol.redact_problem(some_words, some_banned_words) == ["dog"]
    # These next test is thanks to Ryans feedback!

    def test_empty_list(self):
        sol = Solution()
        empty_one = []
        empty_two = []
        assert sol.redact_problem(empty_one, empty_two) == []

    def test_duplicates(self):
        sol = Solution()
        duplicate_words = ["dog", "dog", "mouse"]
        banned_words = ["cat", "chicken", "giraffe"]
        assert sol.redact_problem(duplicate_words, banned_words) == [
            "dog", "dog", "mouse"]
