
"""
Given two strings S and T, return if they are equal when both are typed into empty text editors.
# means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
"""

"""
Intuition:
The intuition and quick methode is to find the final text.
You can just use a string if you don't care time complexity on string modification.
Or you can use a stack or string builder to do it in O(N).
"""
filter()

class SolutionLee1:
    def backspaceCompare(self, S, T):
        back = lambda res, c: res[:-1] if c == '#' else res + c
        return reduce(back, S, "") == reduce(back, T, "")


class SolutionLee2:
    def backspaceCompare(self, S, T):
        def back(res, c):
            if c != '#': res.append(c)
            elif res: res.pop()
            return res
        return reduce(back, S, []) == reduce(back, T, [])

"""
Follow up:

Can you do it in O(N) time and O(1) space?
I believe you have one difficulty here: 
When we meet a char, we are not sure if it will be still there or be deleted.

However, we can do a back string compare (just like the title of problem).
If we do it backward, we meet a char and we can be sure this char won't be deleted.
If we meet a '#', it tell us we need to skip next lowercase char."""

class SolutionLee:
    def backspaceCompare(self, S, T):
        i, j = len(S) - 1, len(T) - 1
        backS = backT = 0
        while True:
            while i >= 0 and (backS or S[i] == '#'):
                backS += 1 if S[i] == '#' else -1
                i -= 1
            while j >= 0 and (backT or T[j] == '#'):
                backT += 1 if T[j] == '#' else -1
                j -= 1
            if not (i >= 0 and j >= 0 and S[i] == T[j]):
                return i == j == -1
            i, j = i - 1, j - 1


class Solution11:
    def backspaceCompare(self, S, T):

        si, ti = len(S) - 1, len(T) - 1
        count_s = count_t = 0

        while si >= 0 or ti >= 0:
            # si stops at non-deleted character in S or -1
            while si >= 0:
                if S[si] == '#':
                    count_s += 1
                    si -= 1
                elif S[si] != '#' and count_s > 0:
                    count_s -= 1
                    si -= 1
                else:
                    break

            # ti stops at non-deleted character in T or -1
            while ti >= 0:
                if T[ti] == '#':
                    count_t += 1
                    ti -= 1
                elif T[ti] != '#' and count_t > 0:
                    count_t -= 1
                    ti -= 1
                else:
                    break

            if (ti < 0 and si >= 0) or (si < 0 and ti >= 0):
                # eg. S = "a#", T = "a"
                return False
            if (ti >= 0 and si >= 0) and S[si] != T[ti]:
                return False

            si -= 1
            ti -= 1
        return True


"""
Solution 1: Stack
Time Complexity O(m + n)
Space Complexity O(m + n)
刚开始试着思考这题的Two Pointers算法，没有思路，却发现这个题的性质特别符合Stack，
就用Stack先解决了。当char is not '#'的时候要缩减，这和Stack的pop一个性质。
"""


class Solution111:
    def backspaceCompare(self, S, T):
        l1 = self.stack(S, [])
        l2 = self.stack(T, [])
        return l1 == l2

    def stack(self, S, stack):
        for char in S:
            if char is not "#":
                stack.append(char)
            else:
                if not stack:
                    continue
                stack.pop()
        return stack


"""
Solution 2: Two Pointers
类型：从右往左Index
Time Complexity O(n)
Space Complexity O(1)
解题思路：
对两个字符串从右往左遍历，用子方程getChar() 从两个字符串分别取值，如取值不等则返回False，
相等就继续迭代，知道迭代技术返回True

子方程getChar()的取值规则：

While循环退出条件：下标出界或者返回值不为空。
Case 1: 当值等于`#`, `count`增值
Case 2: 如果`count == 0` 说明这个值没有被`#`给抵消，返回
Case 3: 如果`count != 0` 切这个值不为`#`，这个值要被`#`抵消掉
三个Case运行完后，记得锁紧下标`r`"""


class Solution(object):
    def backspaceCompare(self, S1, S2):
        r1 = len(S1) - 1
        r2 = len(S2) - 1

        while r1 >= 0 or r2 >= 0:
            char1 = char2 = ""
            if r1 >= 0:
                char1, r1 = self.getChar(S1, r1)
            if r2 >= 0:
                char2, r2 = self.getChar(S2, r2)
            if char1 != char2:
                return False
        return True

    def getChar(self, s, r):
        char, count = '', 0
        while r >= 0 and not char:
            if s[r] == '#':
                count += 1
            elif count == 0:
                char = s[r]
            else:
                count -= 1
            r -= 1
        return char, r


