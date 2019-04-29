
class Solution(object):
    def redact_problem(self, words, banned_words):
        banned_set = set(banned_words)
        result = []
        for item in words:
            if item not in banned_set:
                result.append(item)
        return result

    # def test_redact(self):
    #     all_words = ["Hello", "Noah", "Dog"]
    #     all_banned_words = ["Hello", "Noah", "Dog"]
    #     assert redact_problem(all_words, all_banned_words) == []
    #     no_words = ["dog", "cow", "chicken"]
    #     no_words_banned = ["eggs", "rice", "beans"]
    #     assert redact_problem(no_words, no_words_banned) == [
    #         "dog", "cow", "chicken"]
    #     some_words = ["dog", "cat", "mouse"]
    #     some_banned_words = ["cat", "mouse", "chicken"]
    #     assert redact_problem(some_words, some_banned_words) == ["dog"]


# if __name__ == "__main__":
#     test_redact()
