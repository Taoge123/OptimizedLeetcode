
"""
Given a non-empty string containing an out-of-order English representation of digits 0-9, output the digits in ascending order.

Note:
Input contains only lowercase English letters.
Input is guaranteed to be valid and can be transformed to its original digits. That means invalid inputs such as "abc" or "zerone" are not permitted.
Input length is less than 50,000.
Example 1:
Input: "owoztneoer"

Output: "012"
Example 2:
Input: "fviefuro"

Output: "45"
"""
import collections


class Solution:
    def originalDigits(self, s: str) -> str:
        res = ""
        res += "0" * s.count('z')
        res += "1" * (s.count('o') - s.count('z') - s.count('w') - s.count('u'))
        res += "2" * s.count('w')
        res += "3" * (s.count('h') - s.count('g'))
        res += "4" * s.count('u')
        res += "5" * (s.count('f') - s.count('u'))
        res += "6" * s.count('x')
        res += "7" * (s.count('s') - s.count('x'))
        res += "8" * s.count("g")
        res += "9" * (s.count('i') - s.count('x') - s.count("g") - s.count('f') + s.count('u'))
        return res


"""
s(6) + s(7) -- and 6 is unique 
f(4) + f(5) -- and 4 is unique

for c in s:

    if (c == 'z') count(0)++
    if (c == 'o') count(1)++  //1-0-2-4
    if (c == 'w') count(2)++
    if (c == 'h') count(3)++  //3-8
    if (c == 'u') count(4)++
    if (c == 'f') count(5)++  //5-4
    if (c == 'x') count(6)++
    if (c == 's') count(7)++  //7-6
    if (c == 'g') count(8)++
    if (c == 'i') count(9)++  //9-8-5-6

"""








