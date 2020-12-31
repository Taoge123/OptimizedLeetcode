
import heapq

class Solution:
    def kthSmallest(self, mat, k: int) -> int:
        m, n = len(mat), len(mat[0])
        summ = sum(mat[i][0] for i in range(m))
        heap = [[summ, [0] * m]]
        visited = set()
        for _ in range(k):
            summ, nums = heapq.heappop(heap)
            for j, idx in enumerate(nums):
                if idx + 1 < n:
                    newNums = nums[:]
                    newNums[j] += 1
                    if tuple(newNums) not in visited:
                        # calculate the new summ
                        newSum = summ + (mat[j][newNums[j]] - mat[j][newNums[j] - 1])
                        heapq.heappush(heap, [newSum, newNums])
                        visited.add(tuple(newNums))
        return summ


