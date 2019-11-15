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



import collections


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:

        #         table = collections.defaultdict(int)
        #         for item in s:
        #             table[item] = table.get(item, 0) + 1
        #         odd = 0
        #         for val in table.values():
        #             if val % 2 == 1:
        #                 odd += 1
        #             if odd > 1:
        #                 return False
        #         return True

        counter = collections.Counter(s)

        odd = 0

        for count in counter.values():
            if count % 2:
                odd += 1

            if odd > 1:
                return False

        return True



