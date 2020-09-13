
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


678.Valid-Parenthesis-String
回想一下，如果没有“*”的话，我们怎么处理？我们其实只需要一个计数器count表示未匹配的括号，遇到左括号就加一，遇到右括号就减一。在遍历的过程中，count不能小于零；在结束遍历后，count必须等于零。

那么有“*”的情况下，我们的计数器需要表示一个范围[lower,upper]，表示未匹配的左括号的可能的数目。遇到左括号，未匹配的左括号数就加一；遇到右括号，未匹配的左括号数就减一，这个规则没有变。但是遇到*的时候，它可以当做左括号，也可以当做右括号,也可以当做空号。所以我们需要处理的方法是：lower--; upper++。换句话说，lower表示我们在探索过程中尽可能地将星号转化为右括号，upper表示我们在探索过程中尽可能地将星号转化为左括号，但是同时保证当前的字符串不违法。最终遍历结束后，未匹配的左括号的数目范围需要包括零。

那么遍历的过程中这个范围会有什么变化呢？

首先，当lower小于0的时候，说明右括号太多了。那么之前出现的某个*不能再代表右括号了，可以表示成空号。所以lower此时重置为0。而upper保持不变。

（特别注意,如果题目中说的是*不能作为空号而只能用作左右括号的话,此时的lower应该置为1,因为我们是把一个可能用作右括号的*确定必须为左括号.一正一反相当于lower的值会增2。此时upper的值仍然不变。）

其次，当upper小于0的时候，依然说明右括号太多了。但因为记录upper的原则是：之前的星号都尽可能地转化为左括号。说明此刻此刻，我们并没有任何多余的星号可以再变成左括号了。因此可以提前判断终止.

最后，遍历结束时，lower和upper还需要满足什么条件？显然[lower,upper]必须包括零点（事实上，lower永远不会小于零），这样表示有可能整体未被匹配的左括号数目为零。

类似的题有lintcode 1475.Minimum-Legal-Bracket-Sequence


"""


class SolutionWisdom:
    def checkValidString(self, s: str) -> bool:
        countMax = 0  # max of  unmatched left parenthesis, try to use * as ( if possible
        countMin = 0  # min of  unmatched left parenthesis, try to use * as ) if possible
        for ch in s:
            if ch == '(':
                countMax += 1
                countMin += 1
            elif ch == ')':
                countMax -= 1
                countMin -= 1
            else:
                countMax += 1
                countMin -= 1

            # )太多
            if countMax < 0:
                return False

            # 把)改成空
            if countMin < 0:
                countMin = 0

        return countMin == 0





class Solution:
    def checkValidString(self, s: str) -> bool:
        lower, upper = 0, 0
        for char in s:
            if char == '(':
                lower += 1
                upper += 1

            elif char == ')':
                lower = max(0, lower - 1)
                upper -= 1

            elif char == '*':
                lower = max(0, lower - 1)
                upper += 1

            # 说明左括号太多了
            if upper < 0:
                return False

        return lower == 0





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







