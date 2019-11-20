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


class Solution:

    def __init__(self):
        self.answer = []
        self.nums = None
        self.target = None

    """
        The backtracking function.

        index: Current index in the digits string that we are processing.
        value: Value of the expression till now.
        ops: The expression string represented as a list.
        prev_val: Previous operand in our expression. This is used for the negation effect when considering multiplication operator.
    """
    def recurse(self, index, value, ops, prev_val):
        nums = self.nums
        # Base case. If we have considered all the digits
        if index == len(nums):
            # And the value of the expression target, then we record this expression.
            if value == self.target:
                self.answer.append("".join(ops))
            return
        # This will keep track of the current operand. Remember that an operand is not necessarily equal
        # to a single digit.
        current_val = 0
        # Try all possible operands i.e. all suffixes nums[index:] are operands.
        for i in range(index, len(nums)):
            # Current operand calculated on the fly rather than int(nums[index: i+1])
            current_val = current_val*10 + int(nums[i])
            # If this is the first operand, we simple go onto the next recursion.
            if index == 0:
                self.recurse(i + 1, current_val, ops + [str(current_val)], current_val)
            else:
                # This is the value of the expression before the last operand came into the picture.
                # prev_val is the value of the previous operand with the appropriate sign (+ or -).
                v = value - prev_val
                # MULTIPLICATION will only be between previous value and the current value.
                self.recurse(i + 1, v + (prev_val * current_val), ops + ['*' + str(current_val)], prev_val * current_val)
                # Recurse by ADDING the current operand to the expression.
                self.recurse(i + 1, value + current_val, ops + ['+' + str(current_val)], current_val)
                # Recurse by SUBTRACTING the current operand to the expression.
                self.recurse(i + 1, value - current_val, ops + ['-' + str(current_val)], -current_val)
            # If a string starts with '0', then it has to be an operand on its own. We can't have '025' as an operand. That doesn't make sense
            if nums[index] == '0':
                break

    def addOperators(self, nums, target):
        self.nums = nums
        self.target = target
        self.recurse(0, 0, [], 0)
        return self.answer
