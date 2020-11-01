import collections
import copy


class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        queue = collections.deque([s])
        visited = {s}
        res = s
        while queue:
            node = queue.popleft()
            if res > node:
                res = node
            addA = list(node)
            for i, c in enumerate(addA):
                if i % 2 == 1:
                    addA[i] = str((int(c) + a) % 10)

            addA = ''.join(addA)
            if addA not in visited:
                visited.add(addA);
                queue.append(addA)
            rotate = node[-b:] + node[: -b]
            if rotate not in visited:
                visited.add(rotate)
                queue.append(rotate)
        return res






class SolutionTony:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        nums = list(map(int, s))
        queue = collections.deque()
        queue.append(tuple(nums))
        visited = set()
        visited.add(tuple(nums))

        res = [float('inf')] * len(nums)
        while queue:
            node = queue.popleft()
            nums = list(node)
            val = self.compare(res, nums)
            if val < 0:
                res = nums
            temp = copy.copy(nums)
            nums1 = self.add(temp, a)
            if tuple(nums1) not in visited:
                queue.append(tuple(nums1))
                visited.add(tuple(nums1))
            temp = copy.copy(nums)
            nums2 = self.rotate(temp, b)
            if tuple(nums2) not in visited:
                queue.append(tuple(nums2))
                visited.add(tuple(nums2))
        return "".join(map(str, res))

    def compare(self, res, nums):
        for i in range(len(res)):
            if res[i] > nums[i]:
                return -1
            elif res[i] < nums[i]:
                return 1
        return 0

    def add(self, nums, a):
        for i in range(len(nums)):
            if i % 2 == 1:
                nums[i] += a
                nums[i] %= 10
        return nums

    def rotate(self, nums, k):

        k = k % len(nums)
        n = len(nums)
        self.reverse(nums, 0, n - k - 1)
        self.reverse(nums, n - k, n - 1)
        self.reverse(nums, 0, n - 1)
        return nums

    def reverse(self, nums, i, j):
        while i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1












