import main
import unittest

if not hasattr(unittest.TestCase, 'assertCountEqual'):
    unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual


class MainTest(unittest.TestCase):
    def test_challenge_one(self):
        price1 = main.challenge_one("+15124156620", "challenge_one.txt")
        assert price1 == 0.04
        price2 = main.challenge_one("+14204167789", "challenge_one.txt")
        assert price2 == 0.01
        price3 = main.challenge_one("+15124156620", "challenge_one.txt")
        assert price3 == 0.04
        price4 = main.challenge_one("+19876543210", "challenge_one.txt")
        assert price4 == 0
        price4 = main.challenge_one("+123456789", "challenge_one.txt")
        assert price4 == None
        price4 = main.challenge_one("+14152345378", "challenge_one.txt")
        assert price4 == 0.05

    def test_chalenge_two(self):
        prices1 = main.challenge_two(
            "challenge_two_phone_numbers.txt", "challenge_two_routes.txt")
        assert prices1 == [("+14105547746", 0.08), ("+14105542833", 0),
                           ("+19783405051", 0.02), ("+19783757242", 0.03), ("+14153757242", 0.09)]
        assert len(prices1) == 5
        assert prices1[0] == ("+14105547746", 0.08)
        assert prices1[1] == ("+14105542833", 0)
        assert prices1[2] == ("+19783405051", 0.02)
        assert prices1[3] == ("+19783757242", 0.03)
        assert prices1[4] == ("+14153757242", 0.09)

    def test_challenge_three(self):
        prices1 = main.challenge_three("challenge_three_phone_numbers.txt", [
                                       "challenge_three_routes1.txt", "challenge_three_routes2.txt", "challenge_three_routes3.txt", ])
        assert len(prices1) == 5
        assert prices1[0][0] == "+19783405051"
        assert prices1[1][0] == "+19783757242"
        assert prices1[2][0] == "+19783757230"
        assert prices1[3][0] == "+14153627298"
        assert prices1[4][0] == "+14507623456"
        assert prices1[0][1] == 0.05
        assert prices1[1][1] == 0.09
        assert prices1[2][1] == 0.09
        assert prices1[3][1] == 0.03
        assert prices1[4][1] == 0
