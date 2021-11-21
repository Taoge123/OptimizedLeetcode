"""


left = min(nums)
right = sum(nums)

if count(mid) >= k + 1:
    left = mid + 1
else:
    right = mid
return left

2.
count()

3. == K + 1



3 4 = 7 / 2 = 3.5 -> 3
3 4 = 7 + 1 / 2 = 4


https://leetcode.com/problems/divide-chocolate/solution/
https://www.youtube.com/watch?v=AtewfTorv0g


"""


class SolutionTony1:
    def maximizeSweetness(self, sweetness, K: int) -> int:
        left, right = min(sweetness), sum(sweetness)

        while left < right:
            # check right instead of left (3 + 4) // 2 -> 4 instead of 3
            mid = (left + right + 1) // 2
            if self.count(sweetness, mid) >= K + 1:
                left = mid + 1
            else:
                right = mid
        return left

    def count(self, sweetness, mid):
        count = 0
        summ = 0
        for i in range(len(sweetness)):
            summ += sweetness[i]
            if summ >= mid:
                count += 1
                summ = 0
        return count


class SolutionTonnie:
    def maximizeSweetness(self, sweetness, K: int) -> int:
        left, right = min(sweetness), sum(sweetness) // (K + 1)

        while left < right:
            # check right instead of left (3 + 4) // 2 -> 4 instead of 3
            mid = (left + right + 1) // 2
            if self.count(sweetness, mid) >= K + 1:
                left = mid
            else:
                right = mid - 1
        return left

    def count(self, sweetness, mid):
        count = 0
        summ = 0
        for i in range(len(sweetness)):
            summ += sweetness[i]
            if summ >= mid:
                count += 1
                summ = 0
        return count


class SolutionTony:
    def maximizeSweetness(self, nums, k):
        people = k + 1

        left, right = 1, sum(nums) // people
        while left <= right:
            mid = (left + right) // 2
            chunks = curr = 0
            for num in nums:
                curr += num
                if curr >= mid:
                    chunks += 1
                    curr = 0

            if chunks >= people:
                left = mid + 1
            else:
                right = mid - 1
        return right


class Solution:
    def maximizeSweetness(self, sweetness, K: int) -> int:
        left, right = 0, sum(sweetness)
        while left < right:
            mid = right - (right - left) // 2
            if self.check(mid, sweetness, K):
                left = mid
            else:
                right = mid - 1

        return left

    def check(self, num, sweetness, K):
        summ = 0
        count = 0
        for i in range(len(sweetness)):
            summ += sweetness[i]
            if summ >= num:
                count += 1
                summ = 0
        #需要K+1份
        return count >= K + 1




class Solution2:
    def maximizeSweetness(self, A, K: int) -> int:
        left, right = 1, sum(A) // (K + 1)
        while left < right:
            mid = (right - left) // 2 + left + 1
            cur = cuts = 0
            for num in A:
                cur += num
                if cur >= mid:
                    cuts += 1
                    cur = 0
            if cuts > K:
                left = mid
            else:
                right = mid - 1
        return right





