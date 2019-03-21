
"""
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.

"""

import collections
from heapq import *


class Solution1:
    def frequencySort(self, str):
        """
        :type str: str
        :rtype: str
        """
        return "".join([char * times for char, times in collections.Counter(str).most_common()])


"""
Frequency of a character can vary from 0 to len(s).
Create a hashmap H1 of character to character frequency for the input string.
Iterate H1 to create hashmap H2 with key as frequency 
and value as substrings of repeated strings with length as the frequency.
Finally lookup all potential frequencies in decreasing order in H2 and produce the final result.
"""

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        c1, c2 = collections.Counter(s), {}
        for k, v in c1.items():
            c2.setdefault(v, []).append(k * v)
        return "".join(["".join(c2[i]) for i in range(len(s), -1, -1) if i in c2])


class Solution3:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ''
        bucket = [None for i in range(len(s) + 1)]
        hashmap = {}

        for char in s:
            hashmap[char] = hashmap.get(char, 0) + 1

        for key, value in hashmap.items():
            if bucket[value] is None:
                bucket[value] = []

            bucket[value].append(key)

        for i in reversed(range(len(bucket))):
            if bucket[i] is not None:
                for char in bucket[i]:
                    result += char * i

        return result



class Solution4:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        chars = collections.Counter(s)

        heap = []
        for c in chars:
            heappush(heap, (chars[c], c))

        output = ""
        while len(heap):
            c = heappop(heap)
            output += c[1] * c[0]
        return output[::-1]

