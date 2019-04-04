
"""
Similar to leetcode 438

Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1.
In other words, one of the first string's permutations is the substring of the second string.
Example 1:
Input:s1 = "ab" s2 = "eidbaooo"
Output:True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:
Input:s1= "ab" s2 = "eidboaoo"
Output: False
"""

"""
For each window representing a substring of s2 of length len(s1), 
we want to check if the count of the window is equal to the count of s1. 
Here, the count of a string is the list of: [the number of a's it has, the number of b's,... , the number of z's.]

We can maintain the window by deleting the value of s2[i - len(s1)] when it gets larger than len(s1). 
After, we only need to check if it is equal to the target. Working with list values of [0, 1,..., 25] 
instead of 'a'-'z' makes it easier to count later.
"""

import collections

class Solution1:
    def checkInclusion(self, s1, s2):
        A = [ord(x) - ord('a') for x in s1]
        B = [ord(x) - ord('a') for x in s2]

        target = [0] * 26
        for x in A:
            target[x] += 1

        window = [0] * 26
        for i, x in enumerate(B):
            window[x] += 1
            if i >= len(A):
                window[B[i - len(A)]] -= 1
            if window == target:
                return True
        return False


class Solution:
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        d1, d2 = collections.Counter(s1), collections.Counter(s2[:len(s1)])
        for start in range(len(s1), len(s2)):
            if d1 == d2:
                return True
            d2[s2[start]] += 1
            d2[s2[start-len(s1)]] -= 1

            if d2[s2[start-len(s1)]] == 0:
                del d2[s2[start-len(s1)]]

        return d1 == d2


"""
First, maintain a window with width len(s1), and two counters of s1 and first window.
Then, move the window, update the window counter each time, and check if it equals to the s1 counter.
"""

class Solution3:
    def checkInclusion(self, s1, s2):
        if not s1: return True
        l, r = 0, len(s1)
        count1 = collections.Counter(s1)
        count2 = collections.Counter(s2[l:r])
        if count1 == count2: return True
        while r < len(s2):
            count2[s2[r]] += 1
            count2[s2[l]] -= 1
            if not count2[s2[l]]: del count2[s2[l]]
            if count1 == count2: return True
            l+=1; r+=1
        return False
