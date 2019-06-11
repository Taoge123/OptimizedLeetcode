"""
Given a string, determine if a permutation of the string could form a palindrome.

Example 1:

Input: "code"
Output: false
Example 2:

Input: "aab"
Output: true
Example 3:

Input: "carerac"
Output: true
"""

class Solution1:
    def canPermutePalindrome(self, s):
        dic = {}
        for item in s:
            dic[item] = dic.get(item, 0) + 1
        # return sum(v % 2 for v in dic.values()) < 2
        count1 = 0
        for val in dic.values():
            if val % 2 == 1:
                count1 += 1
            if count1 > 1:
                return False
        return True

class Solution2:
    def canPermutePalindrome(self, s):
        left = set()
        for c in s:
            if c in left:
                left.remove(c)
            else:
                left.add(c)
        return len(left) < 2

class Solution3:
    def canPermutePalindrome(self, s):

        oddChars = set()

        for c in s:
            if c in oddChars:
                oddChars.remove(c)
            else:
                oddChars.add(c)

        return len(oddChars) <= 1



