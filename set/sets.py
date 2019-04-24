
from hashtable import HashTable


class Sets(object):

    def __init__(self, elements=None):
        # Impement the set with a hashtable since we will have unique keys
        self.items = HashTable()
        self.size = 0

        if elements is not None:
            for item in elements:
                self.add(item)

    def add(self, element):
        """Add an element to the set, only will add it if it is unique.
        Best case running time: O(1) under what conditions? Element is placed in a bucket with no collissions
        Worst case running time: O(c) under what conditions? Where c is the amount of entries in a bucket, this is in a hashtable with a high load factor"""

        # Only add the element if the element isnt already in the set
        if self.contains(element) == False:
            self.items.set(element, 0)
            self.size += 1

    def contains(self, element):
        """Check to see if the given element is in the set.
        Best case running time: O(1) under what conditions? value is hashed and found in a bucket with no collisions
        Worst case running time: O(c) under what conditions? Where c is the amount of entries in a bucket, this is in a hashtable with a high load factor"""
        return self.items.contains(element)  # Use the hashtable implmentation of contains

    def delete(self, element):
        """Add an element to the set, only will add it if it is unique.
        Best case running time: O(1) under what conditions? Key is placed in a bucket with no collissions
        Worst case running time: O(c) under what conditions? Where c is the amount of entries in a bucket, this is in a hashtable with a high load factor"""
        self.items.delete(element)
        self.size -= 1

    def union(self, other_set):
        """Get the Union of the two sets(which elements are in both sets).
        Best case running time: O(n) under what conditions? Needs to iterate through the other set with entries n and then calls the contains which could run at best constant time
        Worst case running time: O(nm) under what conditions? Where n is the amount of entries in the other_set and m would be the runtime of calling the contains on a hashtable with a high load factor with many collissions."""
        union_set = Sets()

        # Iterate through the keys of the other_set and see if any of the keys are in the set
        for element in other_set.items.keys():
            if self.items.contains(element):
                union_set.add(element)  # the key is in both sets, so we add it
        return union_set

    def intersection(self, other_set):
        """Get the intersection of the two sets (A new set with elements that are in both).
        Best case running time: O(n + m) under what conditions? Needs to iterate through the other set with entries n and then also needs to iterate through items in self with entries of m
        Worst case running time: O(nc + mf) under what conditions? Needs to iterate through the other set with entries n and then also needs to iterate through items in self with entries of m. Also, we call add which isnt always constant and when called on a hashtable with a high load factor and many collisions, it would yield a runtime of c and f respectively where c and f are the number of collisions in a bucket"""
        intersection_set = Sets()
        for element in self.items.keys():  # Iterate through the set keys and add elements, duplicate elements will not be added
            intersection_set.add(element)
        for element in other_set.items.keys():
            # Iterate through the other set and add the elements, duplicate elements will not be added
            intersection_set.add(element)
        return intersection_set

    def difference(self, other_set):
        """Get what is the difference of the two sets(what is in the set and not in the other_set) .
        Best case running time: O(n) under what conditions? Needs to iterate through the other set with entries n and then calls the contains which could run at best constant time
        Worst case running time: O(nm) under what conditions? Where n is the amount of entries in the other_set and m would be the runtime of calling the contains on a hashtable with a high load factor with many collissions."""
        difference_set = Sets()
        for element in self.items.keys():
            if other_set.contains(element) == False:  # opposite logic to the union
                difference_set.add(element)
        return difference_set

    def is_subset(self, other_set):
        """Check to see if other_set is a subset of the set.
        Best case running time: O(n) under what conditions? Needs to iterate through the other set with entries n and then calls the contains which could run at best constant time
        Worst case running time: O(nm) under what conditions? Where n is the amount of entries in the other_set and m would be the runtime of calling the contains on a hashtable with a high load factor with many collissions."""
        for item in other_set.items.keys():  # iterare through the other set and see if an element isnt in our set
            if self.contains(item) == False:
                return False  # It looks like a key doesnt exist on our set, so we will return False
        return True  # We iterated through the other_set and we didnt have a key that wasnt in our set, so we can return true
