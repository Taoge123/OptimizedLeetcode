"""
Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].

Accepted
116,308
Submissions
188,309
"""


"""
Improved from the stack solution, which iterates backwards.
We itereate forward here so that enumerate() can be used.
Everytime a higher temperature is found, we update answer of the peak one in the stack.
If the day with higher temperature is not found, we leave the ans to be the default 0.
"""

class Solution:
    def dailyTemperatures(self, T):

        res = [0] * len(T)
        stack = []
        for i, num in enumerate(T):
            while stack and T[stack[-1]] < num:
                print(stack[-1], T[stack[-1]])
                cur = stack.pop()
                res[cur] = i - cur
            stack.append(i)

        return res



class Solution2:
    def dailyTemperatures(self, T):
        n = len(T)
        res = [0] * n

        for i in range(n - 2, -1, -1):
            j = i + 1

            while T[i] >= T[j] and res[j] > 0:
                j += res[j]

            if T[j] > T[i]:
                res[i] = j - i

        return res



# T = [73, 74, 75, 71, 69, 72, 76, 73]
T = [1,2,3,4,5,6,7]
# T = [7,6,5,4,3,2,1]
a = Solution()
print(a.dailyTemperatures(T))
