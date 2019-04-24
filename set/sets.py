
from hashtable import HashTable


class Sets(object):

    def __init__(self, elements=None):
        self.items = HashTable()
        self.size = 0

        if elements is not None:
            for item in elements:
                self.add(item)

    def add(self, element):
        if self.contains(element) == False:
            self.items.set(element, 0)
            self.size += 1

    def contains(self, element):
        return self.items.contains(element)

    def delete(self, element):
        self.items.delete(element)
        self.size -= 1

    def union(self, other_set):
        union_set = Sets()
        for element in other_set.items.keys():
            if self.items.contains(element):
                union_set.add(element)
        return union_set

    def intersection(self, other_set):
        intersection_set = Sets()
        for element in self.items.keys():
            intersection_set.add(element)
        for element in other_set.items.keys():
            intersection_set.add(element)
        return intersection_set

    def difference(self, other_set):
        difference_set = Sets()
        for element in self.items.keys():
            if other_set.contains(element) == False:
                difference_set.add(element)
        return difference_set

    def is_subset(self, other_set):
        for item in other_set.items.keys():
            if self.contains(item) == False:
                return False
        return True
