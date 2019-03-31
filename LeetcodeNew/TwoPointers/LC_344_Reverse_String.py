
"""
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array,
you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""

class Solution1:
    def reverseString(self, s):
        if len(s) <= 1:
            return s
        n = len(s)
        return self.reverseString(s[n // 2:]) + self.reverseString(s[:n // 2])


class Solution2:
    """Reverse String class."""
    def reverse_string_by_position(self, s):
        return s[::-1]

    def reverse_string_recursive(self, s):
        if len(s) < 1:
            return s
        return s[-1] + self.reverse_string_recursive(s[:-1])

    def reverse_string_iteratively(self, s):
        length = len(s)
        result = list(s)
        for i in range(length / 2):
            result[length - 1], result[i] = s[length - 1], s[i]
            length -= 1
        return ''.join(result)

    def reverse_string_using_built_in_method(self, s):
        return ''.join(reversed(s))


class Solution3L:
    def reverseString(self, s):
        a, b = 0, len(s) - 1
        s = list(s)

        while a <= b:
            s[a], s[b] = s[b], s[a]
            a += 1
            b -= 1

        return ''.join(s)


class Solution4:
    def reverseString(self, s):
        n = len(s)
        s = list(s)

        # return self.reverseStringRecurse(s, 0, len(s)-1)
        # return self.reverseString2(s)
        # return self.reverseString3(s)

        for i in range(n / 2):
            s[i], s[~i] = s[~i], s[i]

        return "".join(s)

    def reverseString2(self, s):
        return s[::-1]

    def reverseString3(self, s):
        return "".join(reversed(list(s)))

    def reverseStringRecurse(self, s, lo=0, hi=None):
        if hi <= lo:
            return "".join(s)

        s[lo], s[hi] = s[hi], s[lo]
        return self.reverseStringRecurse(s, lo + 1, hi - 1)

