"""
Design and implement a TwoSum class. It should support the following operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.

Example 1:

add(1); add(3); add(5);
find(4) -> true
find(7) -> false
Example 2:

add(3); add(1); add(2);
find(3) -> true
find(6) -> false

"""


from collections import defaultdict

class TwoSum:

    def __init__(self):

        self.cache = defaultdict(int)


    def add(self, number):

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


