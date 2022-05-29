import bisect
import heapq

class Solution:
    def kthSmallestPrimeFraction(self, A, K):
        n = len(A)
        heap = []
        for i in range(1, n):
            heapq.heappush(heap, (float(A[0]) / A[i], 0, i))

        for _ in range(K):
            node, nu, de = heapq.heappop(heap)
            if nu + 1 < de:
                heapq.heappush(heap, (float(A[nu + 1]) / A[de], nu + 1, de))
        return [A[nu], A[de]]



class SolutionBS:
    def kthSmallestPrimeFraction(self, arr, k: int):
        # copy book --> binary search fractions --> check if there is k fraction less than it

        left, right = 0, 1
        while left + 1e-9 < right:
            mid = left + (right - left) / 2
            cnt, best = self.count(arr, mid)
            if cnt < k:
                left = mid
            else:
                res = best
                right = mid
        return res

    def count(self, nums, target):  # get num of smaller fractions and get max fractions
        n = len(nums)
        cnt = 0
        res = [0, nums[-1]]

        for i in range(len(nums)):
            j = bisect.bisect_left(nums, nums[i] / target)
            cnt += n - j
            if j < n and nums[i] / nums[j] > res[0] / res[1]:
                res = [nums[i], nums[j]]
        return cnt, res



