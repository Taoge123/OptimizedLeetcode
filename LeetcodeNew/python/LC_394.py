"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
https://leetcode.com/problems/decode-string/discuss/208633/DFS-simple-python
https://leetcode.com/problems/decode-string/discuss/428957/2-Clean-Python-Solution-(Recursion-Stack-Explained)

"""


class Solution:
    def decodeString(self, s: str) -> str:
        curNum = 0
        curString = ""
        nums = []
        string = []

        for char in s:
            if char == "[":
                string.append(curString)
                nums.append(curNum)
                curString = ""
                curNum = 0

            elif char == ']':
                prevNum = nums.pop()
                prevString = string.pop()
                curString = prevString + prevNum * curString

            elif char.isdigit():
                curNum = curNum * 10 + int(char)

            else:
                curString += char

        return curString



class Solution2:
    def decodeString(self, s):
        return self.helper(list(s)[::-1])

    def helper(self, s):
        res = ""
        while s:
            num = ""
            while s and s[-1].isdigit():
                num += s.pop()
            if num:
                num = int(num)
                s.pop()
                res += self.helper(s) * num
            else:
                c = s.pop()
                if c not in "[]":
                    res += c
                if c == ']':
                    break
        return res



s = "3[a]2[bc]"
a = Solution2()
print(a.decodeString(s))
