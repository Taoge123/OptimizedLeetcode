"""
Additive number is a string whose digits can form additive sequence.

A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.

Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.



Example 1:

Input: "112358"
Output: true
Explanation: The digits can form an additive sequence: 1, 1, 2, 3, 5, 8.
             1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
Example 2:

Input: "199100199"
Output: true
Explanation: The additive sequence is: 1, 99, 100, 199.
             1 + 99 = 100, 99 + 100 = 199
"""



class Solution:
    def isAdditiveNumber(self, num: str) -> bool:

        return self.dfs(num, [])

    def dfs(self, num, path):
        if len(path) >= 3 and path[-1] != path[-2] + path[-3]:
            return False
        if not num and len(path) >= 3:
            return True

        for i in range(len(num)):
            temp = num[:i + 1]
            if temp[0] == '0' and len(temp) != 1:
                continue
            if self.dfs(num[i + 1:], path + [int(temp)]):
                return True
        return False








