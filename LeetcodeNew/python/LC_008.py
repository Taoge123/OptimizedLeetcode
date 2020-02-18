"""
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
Example 1:

Input: "42"
Output: 42
Example 2:

Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.
Example 3:

Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
Example 4:

Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical
             digit or a +/- sign. Therefore no valid conversion could be performed.
Example 5:

Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−231) is returned.
"""

import re

class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.strip()
        str = re.findall('(^[\+\-0]*\d+)\D*', str)

        try:
            result = int(''.join(str))
            MAX_INT = 2147483647
            MIN_INT = -2147483648
            if result > MAX_INT > 0:
                return MAX_INT
            elif result < MIN_INT < 0:
                return MIN_INT
            else:
                return result
        except:
            return 0


class Solution1:
    def myAtoi(self, s):

        ###better to do strip before sanity check (although 8ms slower):
        # ls = list(s.strip())
        if len(s) == 0:
            return 0
        ls = list(s.strip())
        if not ls:
            return 0
        sign = -1 if ls[0] == '-' else 1
        if ls[0] in ['-', '+']:
            del ls[0]
        res, i = 0, 0
        while i < len(ls) and ls[i].isdigit():
            res = res * 10 + ord(ls[i]) - ord('0')
            i += 1
        return max(-2 ** 31, min(sign * res, 2 ** 31 - 1))


class Solution2:
    def myAtoi(self, s):

        if (len(s) == 0):
            return 0

        s = s.strip()    #去除空格

        if(s[0].isdigit()):         #首字符是数字
            sign = 1
        elif(s[0] == '+'):          #首字符是+-
            sign = 1
            s = s[1:]
        elif(s[0] == '-'):
            sign = -1
            s = s[1:]
        else:
            return 0

        l = len(s)
        val = 0;    i = 0
        while(i < l and s[i].isdigit()):
            val = val * 10 + eval(s[i])
            i += 1

        val = sign * val

        if(val > 2147483647):
            return 2147483647
        elif(val < -2147483648):
            return -2147483648
        else:
            return val


