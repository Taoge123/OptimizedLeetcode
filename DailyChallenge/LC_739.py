
"""
73 74 75 71 69 72 76 73
1  1  4  2  1  1  0  0


"""

class Solution:
    def dailyTemperatures(self, T):
        stack = []
        res = [0] * len(T)
        for i, num in enumerate(T):
            while stack and T[stack[-1]] < num:
                node = stack.pop()
                res[node] = i - node
            stack.append(i)
        return res

