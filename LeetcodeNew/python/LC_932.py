"""
Example:
1,2,3,4,5,6,7,8,9
-->
1,3,5,7,9,2,4,6,8
-->
1,5,9,3,7,2,6,4,8
-->
1,9,5,3,7,2,6,4,8

"""


class Solution:
    def beautifulArray(self, N):
        return self.helper(list(range(1, N + 1)))

    def helper(self, nums):
        if len(nums) <= 2:
            return nums

        return self.helper(nums[::2]) + self.helper(nums[1::2])


class SolutionLee:
    def beautifulArray(self, N: int) -> List[int]:
        if N == 1:
            return [1]
        odd = [i * 2 - 1 for i in self.beautifulArray(N // 2 + N % 2)]
        even = [i * 2 for i in self.beautifulArray(N // 2)]
        return odd + even

"""
1    001
2    010
3    011
4    100
5    101
6    110

"""

class SolutionLee:
    def beautifulArray(self, N: int) -> List[int]:
        return sorted(range(1, N + 1), key=lambda x: bin(x)[2:][::-1])



