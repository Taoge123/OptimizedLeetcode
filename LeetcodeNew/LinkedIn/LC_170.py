

from collections import defaultdict
class TwoSum(object):
    def __init__(self):
        """
        initialize your data structure here
        """
        self.cache = defaultdict(int)

    def add(self, number):
        """
        Add the number to an internal data structure.
        :rtype: nothing
        """
        self.cache[number] += 1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for k in self.cache:
            complement = value - k
            if (complement in self.cache):
                if (complement != k) or (complement == k and self.cache[k] >= 2):
                    return True
        return False