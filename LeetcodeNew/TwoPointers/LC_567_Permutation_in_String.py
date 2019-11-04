
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

"""
First, maintain a window with width len(s1), and two counters of s1 and first window.
Then, move the window, update the window counter each time, and check if it equals to the s1 counter.
"""
import collections

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        n1, n2 = len(s1), len(s2)

        counter1, counter2 = collections.Counter(s1), collections.Counter(s2[:n1])

        for i in range(n1, n2):
            if counter1 == counter2:
                return True

            counter2[s2[i]] += 1
            counter2[s2[i - n1]] -= 1
            if counter2[s2[i - n1]] <= 0:
                del counter2[s2[i - n1]]

        return counter1 == counter2


