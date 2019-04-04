
"""
Given a string S and a character C, return an array of integers
representing the shortest distance from the character C in the string.

Example 1:

Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
"""

"""
Algorithm

When going left to right, we'll remember the index prev of the last character C we've seen. Then the answer is i - prev.

When going right to left, we'll remember the index prev of the last character C we've seen. Then the answer is prev - i.

We take the minimum of these two answers to create our final answer.
"""


class Solution:
    def shortestToChar(self, S, C):
        prev = float('-inf')
        ans = []
        for i, x in enumerate(S):
            if x == C:
                prev = i
            ans.append(i - prev)

        prev = float('inf')
        for i in range(len(S) - 1, -1, -1):
            if S[i] == C:
                prev = i
            ans[i] = min(ans[i], prev - i)

        return ans


"""
Explanation
Initial result array.
Loop twice on the string S.
First forward pass to find shortest distant to character on left.
Second backward pass to find shortest distant to character on right.

Note
In python solution, I merged these two for statement.
I can do the same in C++/Java by:

for (int i = 0; i >= 0; res[n-1] == n ? ++i : --i)
But it will become less readable.

Time Complexity O(N)
"""
class SolutionLee:
    def shortestToChar(self, S, C):
        n = len(S)
        res = [n] * n
        pos = -n
        for i in range(n) + range(n)[::-1]:
            if S[i] == C: pos = i
            res[i] = min(res[i], abs(i - pos))
        return res


"""
Another idea is quite similar.
We give it one more loop at first to find all character C and initialize distance to 0.
The same, we can merge the extra pass to the forward pass one, like:
"""

class SolutionLee2:
    def shortestToChar(self, S, C):
        n = len(S)
        res = [0 if c == C else n for c in S]
        for i in range(n - 1): res[i + 1] = min(res[i + 1], res[i] + 1)
        for i in range(n - 1)[::-1]: res[i] = min(res[i], res[i + 1] + 1)
        return res

"""
Dictionary
把所有的char对应的index存储进字典，之后再一个一个的比对。

Time: O(N * size of dic[char]) | Worst case O(N^2)
Space: O(N)
"""
class Solution3:
    def shortestToChar(self, s, target):
        dic = {}
        res = []
        for i, char in enumerate(s):
            if char not in dic:
                dic[char] = [i]
            else:
                dic[char].append(i)

        for cur_index, char in enumerate(s):
            closest = float('inf')
            for index in dic[target]:
                closest = min(closest, abs(cur_index - index))
            res.append(closest)
        return res


"""
Two Pass
Time: O(N)
Space: O(N)
上面代码能优化的地方在于，再每个index位置，你真正需要比对的其实只有最左边 target_index - cur_index 
和最右边的target_index - cur_index，所以根据这个特性
我们从左往右走一遍，记录所有从左往右的最小值，通用从右边往左的时候，把最小值和之前的最小值比对，并更改即可。
"""


class Solution4:
    def shortestToChar(self, s, target):
        closest = float('-inf')
        res = []
        for i, char in enumerate(s):
            if char == target:
                closest = i
            res.append(i - closest)

        closest = float('inf')
        for i in range(len(s) - 1, -1, -1):
            if s[i] == target:
                closest = i
            res[i] = min(res[i], closest - i)
        return res






