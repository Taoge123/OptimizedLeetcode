"""
Given a string that contains only digits 0-9 and a target value,
return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.

Example 1:

Input: num = "123", target = 6
Output: ["1+2+3", "1*2*3"]
Example 2:

Input: num = "232", target = 8
Output: ["2*3+2", "2+3*2"]
Example 3:

Input: num = "105", target = 5
Output: ["1*0+5","10-5"]
Example 4:

Input: num = "00", target = 0
Output: ["0+0", "0-0", "0*0"]
Example 5:

Input: num = "3456237490", target = 9191
Output: []
"""


class SolutionRika:
    def addOperators(self, num: str, target: int):
        self.res = []
        self.dfs(num, target, 0, 0, 0, '')
        return self.res

    def dfs(self, nums, target, pos, prev, value, path):
        if pos == len(nums):
            if value == target:
                self.res.append(path)
            return

        for i in range(pos, len(nums)):
            if i > pos and nums[pos] == '0': # no leading zero
                continue
            cur = int(nums[pos:i+1])
            if pos == 0:
                self.dfs(nums, target, i + 1, cur, cur, path + str(cur))
            else:
                self.dfs(nums, target, i + 1, cur, value + cur, path + '+' + str(cur))
                self.dfs(nums, target, i + 1, - cur, value - cur, path + '-' + str(cur))
                self.dfs(nums, target, i + 1, prev * cur, (value - prev) + cur * prev, path + '*' + str(cur))



class Solution1:
    def __init__(self):
        self.res = []
        self.target = 0

    def addOperators(self, num: str, target: int):
        self.target = target
        self.dfs(num, 0, 0, 0, [])
        return self.res

    def dfs(self, nums, index, prev, value, path):
        if index == len(nums):
            if value == self.target:
                self.res.append("".join(path))
            return

        curr = 0
        for i in range(index, len(nums)):
            curr = curr * 10 + int(nums[i])
            if index == 0:
                self.dfs(nums, i + 1, curr, curr, path + [str(curr)])
            else:
                self.dfs(nums, i + 1, curr, value + curr, path + ['+' + str(curr)])
                self.dfs(nums, i + 1, -curr, value - curr, path + ['-' + str(curr)])
                self.dfs(nums, i + 1, prev * curr, value - prev + curr * prev, path + ['*' + str(curr)])

            if nums[index] == '0':
                break


class Solution:
    def __init__(self):
        self.res = []
        self.nums = None
        self.target = None

    """
        The backtracking function.

        index: Current index in the digits string that we are processing.
        value: Value of the expression till now.
        ops: The expression string represented as a list.
        prev: Previous operand in our expression. This is used for the negation effect when considering multiplication operator.
    """
    def recurse(self, index, value, ops, prev):
        nums = self.nums
        # Base case. If we have considered all the digits
        if index == len(nums):
            # And the value of the expression target, then we record this expression.
            if value == self.target:
                self.res.append("".join(ops))
            return
        # This will keep track of the current operand. Remember that an operand is not necessarily equal
        # to a single digit.
        curr = 0
        # Try all possible operands i.e. all suffixes nums[index:] are operands.
        for i in range(index, len(nums)):
            # Current operand calculated on the fly rather than int(nums[index: i+1])
            curr = curr*10 + int(nums[i])
            # If this is the first operand, we simple go onto the next recursion.
            if index == 0:
                self.recurse(i + 1, curr, ops + [str(curr)], curr)
            else:
                # This is the value of the expression before the last operand came into the picture.
                # prev is the value of the previous operand with the appropriate sign (+ or -).
                v = value - prev
                # MULTIPLICATION will only be between previous value and the current value.
                self.recurse(i + 1, v + (prev * curr), ops + ['*' + str(curr)], prev * curr)
                # Recurse by ADDING the current operand to the expression.
                self.recurse(i + 1, value + curr, ops + ['+' + str(curr)], curr)
                # Recurse by SUBTRACTING the current operand to the expression.
                self.recurse(i + 1, value - curr, ops + ['-' + str(curr)], -curr)
            # If a string starts with '0', then it has to be an operand on its own. We can't have '025' as an operand.
            # That doesn't make sense
            if nums[index] == '0':
                break

    def addOperators(self, nums, target):
        self.nums = nums
        self.target = target
        self.recurse(0, 0, [], 0)
        return self.res







class SolutionToBeFixed:
    def addOperators(self, num: str, target: int):
        res = []
        if not num or len(num) == 0:
            return res

        self.helper(res, "", num, target, 0, 0, 0)
        return res

    def helper(self, res, path, num, target, pos, val, pre):
        if pos == len(num):
            if target == val:
                res.append(path)
                return

        for i in range(pos, len(num)):
            if i != pos and num[pos] == '0':
                break
            cur = int(num[pos:i+1])
            if pos == 0:
                self.helper(res, path + str(cur), num, target, i + 1, cur, cur)

            else:
                self.helper(res, path + "+" + str(cur), num, target, i + 1, val + cur, cur)
                self.helper(res, path + "-" + str(cur), num, target, i + 1, val - cur, cur)
                self.helper(res, path + "*" + str(cur), num, target, i + 1, val-pre+pre*cur, pre * cur)


class SolutionTest:
    def addOperators(self, num: str, target: int):

        self.res = []
        self.dfs(num, 0, target, [], 0, 0)
        return self.res

    def dfs(self, num, index, target, path, prev, cur):
        if index == len(num):
            if cur == target:
                self.res.append("".join(path))

            for i in range(index, len(num)):
                self.dfs(num, index + 1, target, path + ['+'] + [num[i]], num[i], cur + int(num[i]))
                self.dfs(num, index + 1, target, path + ['-'] + [num[i]], num[i], cur - int(num[i]))

        return self.res



num = "123"
target = 6
a = SolutionTest()
print(a.addOperators(num, target))
