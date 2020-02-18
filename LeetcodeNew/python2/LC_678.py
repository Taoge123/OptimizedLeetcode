
"""
Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.
Example 1:
Input: "()"
Output: True
Example 2:
Input: "(*)"
Output: True
Example 3:
Input: "(*))"
Output: True
"""

"""
Intuition:
One pass on the string S,
we need to know,
how many ')' we are waiting for.

If we meet too many ')', we can return false directly.
If we wait for no ')' at the end, then we are good.


Explanation:
We count the number of ')' we are waiting for,
and it's equal to the number of open parenthesis.
This number will be in a range and we count it as [mini, maxi]

maxi counts the maximum open parenthesis,
which means the maximum number of unbalanced '(' that COULD be paired.
mini counts the minimum open parenthesis,
which means the number of unbalanced '(' that MUST be paired.


Example:
It's quite straight forward actually.
When you met "(", you know you need one only one ")", mini = 1 and maxi = 1.
When you met "(*(", you know you need one/two/three ")", mini = 1 and maxi = 3.

The string is valid for 2 condition:

maxi will never be negative.
mini is 0 at the end.

Time Complexity:
One pass O(N) time, Space O(1)
左括号加一
右括号减一
*可以加一可以减一
"""

class SolutionLee:
    def checkValidString(self, s):
        mini = maxi = 0
        for char in s:
            if char == '(':
                maxi += 1
                mini += 1
            if char == ')':
                maxi -= 1
                mini = max(mini - 1, 0)
            if char == '*':
                maxi += 1
                mini = max(mini - 1, 0)
            if maxi < 0:
                return False
        return mini == 0

class Solution:
    def checkValidString(self, s):
        mini = maxi = 0
        for i in s:
            maxi = maxi - 1 if i == ")" else maxi + 1
            mini = mini + 1 if i == '(' else max(mini - 1, 0)
            if maxi < 0: return False
        return mini == 0







