"""
You are given a circular array nums of positive and negative integers. If a number k at an index is positive,
then move forward k steps. Conversely, if it's negative (-k), move backward k steps.
Since the array is circular, you may assume that the last element's next element is the first element,
and the first element's previous element is the last element.

Determine if there is a loop (or a cycle) in nums. A cycle must start and end at the same index
and the cycle's length > 1. Furthermore, movements in a cycle must all follow a single direction.
In other words, a cycle must not consist of both forward and backward movements.



Example 1:

Input: [2,-1,1,2,2]
Output: true
Explanation: There is a cycle, from index 0 -> 2 -> 3 -> 0. The cycle's length is 3.
Example 2:

Input: [-1,2]
Output: false
Explanation: The movement from index 1 -> 1 -> 1 ... is not a cycle, because the cycle's length is 1. By definition the cycle's length must be greater than 1.
Example 3:

Input: [-2,1,-1,-2,-2]
Output: false
Explanation: The movement from index 1 -> 2 -> 1 -> ... is not a cycle, because movement from index 1 -> 2 is a forward movement,
but movement from index 2 -> 1 is a backward movement. All movements in a cycle must follow a single direction.


Note:

-1000 ≤ nums[i] ≤ 1000
nums[i] ≠ 0
1 ≤ nums.length ≤ 5000


Follow up:

Could you solve it in O(n) time complexity and O(1) extra space complexity?
"""


class Solution:
    def circularArrayLoop(self, nums) -> bool:

        n = len(nums)

        def next_pos(i):
            return (i + nums[i]) % n

        for i in range(n):
            slow = i
            fast = next_pos(slow)
            while nums[fast] * nums[i] > 0 and nums[next_pos(fast)] * nums[i] > 0:
                if slow == fast:
                    if slow == next_pos(slow):
                        break
                    return True
                slow = next_pos(slow)
                fast = next_pos(next_pos(fast))
        return False



class Solution2:
    def circularArrayLoop(self, nums) -> bool:
        for i, num in enumerate(nums):
            if num == 0:
                continue
            slow = i
            fast = self.nextPos(i, nums)
            while nums[fast] * nums[i] > 0 and nums[self.nextPos(fast, nums)] * nums[i] > 0:
                if slow == fast:
                    # This will become self loop
                    if slow == self.nextPos(slow, nums):
                        break
                    return True
                slow = self.nextPos(slow, nums)
                fast = self.nextPos(self.nextPos(fast, nums), nums)

            slow = i
            while nums[slow] * num > 0:
                nxt = self.nextPos(slow, nums)
                nums[slow] = 0
                slow = nxt

        return False

    def nextPos(self, i, nums):
        length = len(nums)
        return (i + nums[i]) % length


