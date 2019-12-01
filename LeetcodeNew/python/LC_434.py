"""
Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.

Please note that the string does not contain any non-printable characters.

Example:

Input: "Hello, my name is John"
Output: 5
"""

class Solution:
    def countSegments(self, s: str) -> int:

        count = 0
        for i in range(len(s)):
            if s[i] != ' ' and (i == 0 or s[ i -1] == ' '):
                count += 1
        return count


