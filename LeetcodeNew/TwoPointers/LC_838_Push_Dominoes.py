
"""
There are N dominoes in a line, and we place each domino vertically upright.

In the beginning, we simultaneously push some of the dominoes either to the left or to the right.



After each second, each domino that is falling to the left pushes the adjacent domino on the left.

Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.

Given a string "S" representing the initial state. S[i] = 'L', if the i-th domino has been pushed to the left; S[i] = 'R', if the i-th domino has been pushed to the right; S[i] = '.', if the i-th domino has not been pushed.

Return a string representing the final state.

Example 1:

Input: ".L.R...LR..L.."
Output: "LL.RR.LLRRLL.."
Example 2:

Input: "RR.L"
Output: "RR.L"
Explanation: The first domino expends no additional force on the second domino.
Note:

0 <= N <= 10^5
String dominoes contains only 'L', 'R' and '.'

"""

"""
Intuition:
Whether be pushed or not, depend on the shortest distance to 'L' and 'R'.
Also the direction matters.
Base on this idea, you can do the same thing inspired by this problem.
https://leetcode.com/problems/shortest-distance-to-a-character/discuss/125788/

Here is another idea that focus on 'L' and 'R'.
'R......R' => 'RRRRRRRR'
'R......L' => 'RRRRLLLL' or 'RRRR.LLLL'
'L......R' => 'L......R'
'L......L' => 'LLLLLLLL'
"""
"""
解题方法
如果理解了一个推倒了的牌只能对另一个站着的牌起作用这句话那么基本上就能做出来这个题了，否则是做不出来的。

我们对这个题的理解应该是找出最近的两个被推倒了的牌，然后判断这两个牌是什么样子的即可，不用考虑这个区间以外的牌，
因为这两张牌被推倒了，而这个区间外的其他牌不会对推倒了的牌起作用。所以使用双指针的方式解决。
"""


class SolutionLee:
    def pushDominoes(self, d):
        d = 'L' + d + 'R'
        res = []
        i = 0
        for j in range(1, len(d)):
            if d[j] == '.': continue
            middle = j - i - 1
            if i:
                res.append(d[i])
            if d[i] == d[j]:
                res.append(d[i] * middle)
            elif d[i] == 'L' and d[j] == 'R':
                res.append('.' * middle)
            else:
                res.append('R' * (middle / 2) + '.' * (middle % 2) + 'L' * (middle / 2))
            i = j
        return ''.join(res)


class Solution2:
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        while(True):
            new = dominoes.replace('R.L', 'S')
            new = new.replace('.L','LL').replace('R.','RR')
            if new == dominoes:
                break
            else:
                dominoes = new
        return dominoes.replace('S', 'R.L')


"""
思路：
用res存储最后的结果，遍历整个字符串，’.’直接跳过，当遍历到’L’时，看上一个出现的是’L’还是’R’,如果是’L’，
全往左边倒，如果是’R’，计算距离一半R一半L；遍历到’R’同理。
"""


class Solution5:
    def pushDominoes(self, dominoes):

        res = ''
        i = 0
        # 上一个出现的关键点用last表示，初始为None，处理左边界情况
        last = None
        while i < len(dominoes):
            j = i
            # 遍历到'.'就不管，一直到找到一个'R或L'为止
            while j + 1 < len(dominoes) and dominoes[j] == '.':
                j += 1
            # 找到L的情况
            if dominoes[j] == 'L':
                if last == 'R':
                    res += (j - i) / 2 * 'R' + (j - i) % 2 * '.' + (j - i) / 2 * 'L' + 'L'
                else:
                    res += 'L' * (j - i + 1)
                last = 'L'
            # 找到R的情况
            elif dominoes[j] == 'R':
                if last == 'R':
                    res += (j - i + 1) * 'R'
                else:
                    res += (j - i) * '.' + 'R'
                last = 'R'
            i = j + 1

        # 出来之后，处理右边界情况
        if last == 'R':
            res += 'R' * (len(dominoes) - len(res))
        else:
            res += '.' * (len(dominoes) - len(res))
        return res


