
from collections import defaultdict

class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.cache = defaultdict(int)


    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
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



# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)


