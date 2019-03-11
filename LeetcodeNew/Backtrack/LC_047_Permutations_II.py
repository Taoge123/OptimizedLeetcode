"""
Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

"""


class Solution:
    def permute(nums):
        permutations = [[]]

        for head in nums:
            permutations = [rest[:i] + [head] + rest[i:] for rest in permutations for i in range(len(rest) + 1)]

        return permutations

class So2lution:
    def permuteUnique(self, num):
        if not num:
            return []
        return self.permute(sorted(num))


    def permute(self, num):
        if len(num) == 1:
            return [num]

        ret = []
        for index, elt in enumerate(num):
            if index > 0 and num[index - 1] == elt:
                continue
            ret += [[elt] + p for p in self.permute(num[:index] + num[index + 1:])]
        return ret

class Solution3:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        self.permutation(nums, [],result)
        return result

    def permutation(self, numbers, curr, result):
        if len(numbers) == 0:
            result.append(curr)

        for i in range(len(numbers)):
            if i > 0 and numbers[i] == numbers[i-1]:
                continue
            self.permutation(numbers[0:i]+numbers[i+1:], curr + [numbers[i]], result)


class Solution:
    def permuteUnique(self, nums):
        def backtrack(tmp, size):
            if len(tmp) == size:
                ans.append(tmp[:])
            else:
                for i in range(size):
                    if visited[i] or (i > 0 and nums[i-1] == nums[i] and not visited[i-1]):
                        continue
                    visited[i] = True
                    tmp.append(nums[i])
                    backtrack(tmp, size)
                    tmp.pop()
                    visited[i] = False
        ans = []
        visited = [False] * len(nums)
        nums.sort()
        backtrack([], len(nums))
        return ans




