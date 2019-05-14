from sets import Sets
import unittest

if not hasattr(unittest.TestCase, 'assertCountEqual'):
    unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual


class SetTest(unittest.TestCase):

    def test_init(self):
        st = Sets([1, 2, 3, 4])
        assert st.size == 4
        assert len(st.items.keys()) == 4
        st_two = Sets()
        assert st_two.size == 0
        assert len(st_two.items.keys()) == 0

    def test_add_and_contains(self):
        st = Sets()
        st.add(5)
        assert st.size == 1
        st.add(2)
        assert st.size == 2
        assert st.contains(5) == True
        assert st.contains(2) == True
        assert st.contains(7) == False

    def test_add_strings_and_contains(self):
        st = Sets()
        st.add("Hello")
        assert st.size == 1
        st.add("Noah")
        assert st.size == 2
        assert st.contains("Hello") == True
        assert st.contains("Noah") == True
        assert st.contains("Woodward") == False

    def test_delete(self):
        st = Sets()
        st.add(1)
        st.add(3)
        st.add("hello")
        assert st.size == 3
        st.delete(3)
        assert st.size == 2
        assert st.contains(3) == False

    def test_union(self):
        first_set = Sets([1, 2, 3, 4])
        second_set = Sets([1, 2, 3])
        union_set = second_set.union(first_set)
        assert union_set.size == 4
        assert union_set.contains(1) == True
        assert union_set.contains(2) == True
        assert union_set.contains(3) == True
        assert union_set.contains(4) == True

    def test_intersection(self):
        first_set = Sets([1, 2, 3, 6])
        second_set = Sets([1, 2, 3, 4, 5, 7])
        intersection_set = first_set.intersection(second_set)
        assert intersection_set.size == 3
        assert intersection_set.contains(1) == True
        assert intersection_set.contains(2) == True
        assert intersection_set.contains(3) == True
        assert intersection_set.contains(4) == False
        assert intersection_set.contains(5) == False
        assert intersection_set.contains(6) == False
        assert intersection_set.contains(7) == False

    def test_difference(self):
        first_set = Sets([2, 3, 4, 5, 6])
        second_set = Sets([1, 2, 3, 4])
        difference_set = first_set.difference(second_set)
        assert difference_set.size == 2
        assert difference_set.contains(5) == True
        assert difference_set.contains(6) == True
        assert difference_set.contains(1) == False
        assert difference_set.contains(2) == False
        assert difference_set.contains(3) == False
        assert difference_set.contains(4) == False

    def test_is_subset(self):
        first_set = Sets([1, 2, 3, 4, 5, 6])
        second_set = Sets([1, 2, 3, 4])
        assert first_set.is_subset(second_set) == True
        third_set = Sets([11, 12, 13, 14])
        assert first_set.is_subset(third_set) == False
        fourth_set = Sets([2, 2, 2, 2])
        assert first_set.is_subset(fourth_set) == True
        fifth_set = Sets([4, 5, 6, 7, 8])
        assert first_set.is_subset(fifth_set) == False
