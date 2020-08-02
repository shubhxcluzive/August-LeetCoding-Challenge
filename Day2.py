#Design a HashSet without using any built-in hash table libraries.
#To be specific, your design should include these functions:
#add(value): Insert a value into the HashSet.
#contains(value) : Return whether the value exists in the HashSet or not.
#remove(value): Remove a value in the HashSet.
# If the value does not exist in the HashSet, do nothing.


class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """

        self.set_table = []

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """

        if not self.contains(key):
            self.set_table.append(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """

        try:
            self.set_table.remove(key)
        except:
            pass

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """

        return key in self.set_table

