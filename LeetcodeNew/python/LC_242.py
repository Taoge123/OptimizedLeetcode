"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?

"""


class Solution:
    def isAnagram(self, s, t):
        dic = {}
        for i in s:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1

        for i in t:
            if i in dic:
                dic[i] -= 1
            else:
                return False

        for i in dic:
            if dic[i] > 0:
                return False

        return True



