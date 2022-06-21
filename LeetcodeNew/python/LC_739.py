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

# for each value, once num > prev, then we pop out each of their index and get the diff distance

class SolutionTony:
    def dailyTemperatures(self, nums):
        stack = []
        n = len(nums)
        res = [0] * n

        for i, num in enumerate(nums):
            while stack and nums[stack[-1]] < num:
                node = stack.pop()
                res[node] = i - node
            stack.append(i)
        return res


# T = [73, 74, 75, 71, 69, 72, 76, 73]
T = [1,2,3,4,5,6,7]
# T = [7,6,5,4,3,2,1]
a = SolutionTony()
print(a.dailyTemperatures(T))
