
"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"
Note:
The vowels does not include the letter "y".

"""

"""
The idea is really simple. But I think my code is somewhat ugly in two ways:

Convert string to list then convert back
Pointer processing is verbose.
Any suggestion? Thanks.
"""


class Solution1:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        #define a set
        vowels = {'a', 'e', 'i', 'o', 'u'}
        left, right = 0, len(s) - 1

        while left < right:
            if s[left].lower() not in vowels:
                left += 1
            elif s[right].lower() not in vowels:
                right -= 1
            else:
                s[left], s[right] = s[right], s[left]
                left, right = left + 1, right - 1

        return ''.join(s)




