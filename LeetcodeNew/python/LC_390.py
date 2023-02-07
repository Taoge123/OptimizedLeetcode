
"""
https://www.youtube.com/watch?v=50YxyEPRDZQ

There is a list of sorted integers from 1 to n. Starting from left to right, remove the first number and every other number afterward until you reach the end of the list.

Repeat the previous step again, but this time from right to left, remove the right most number and every other number from the remaining numbers.

We keep repeating the steps again, alternating left to right and right to left, until a single number remains.

Find the last number that remains starting with a list of length n.

Example:

Input:
n = 9,
1 2 3 4 5 6 7 8 9
2 4 6 8
2 6
6

Output:
6
"""

"""
1 2 3 4 5 6 7 8 9 10 11 12 13 14 -> head, step, remain
1 2 3 4 5 6 7 8 9 10 11 12 13 14 ->   1,    1,   14
  2   4   6   8   10    12    14 ->   2,    2,   7
      4       8         12       ->   4,    4,   3
              8                  ->   8,    8,   1

1 2 3 4 5 6 7 8 9 10 11 12 13    -> head, step, remain
1 2 3 4 5 6 7 8 9 10 11 12 13    ->   1,    1,   13
  2   4   6   8   10    12       ->   2,    2,   6
  2       6       10             ->   2,    4,   3
          6                      ->   6,    8,   1

从左删除: head + step
从右删除:
    odd remain: head + step. ie: 2, 4, 6
    even remain: head不变. ie: 2, 4, 6, 8
每次删除, 数字之间距离增加一倍，step ✖️ 2

"""


class SolutionTony:
    def lastRemaining(self, n: int) -> int:
        head, step, remain = 1, 1, n
        is_left = True
        while remain != 1:
            # if from left or (from right but has odd numbers)
            if is_left or (not is_left and remain % 2 == 1):
                head += step
            remain //= 2
            step *= 2
            is_left = not is_left
            # print(head, step, remain, is_left)
        return head


class Solution:
    def lastRemaining(self, n: int) -> int:
        nums = range(1, n + 1)
        while len(nums) > 1:
            nums = nums[1::2][::-1]
        return nums[0]


class Solution2:
    def lastRemaining(self, n: int) -> int:
        if n == 2 or n == 3:
            return 2
        elif n == 1:
            return 1
        else:
            base = 4 * self.lastRemaining(n // 4)
            if n % 4 == 0 or n % 4 == 1:
                return base - 2
            else:
                return base





