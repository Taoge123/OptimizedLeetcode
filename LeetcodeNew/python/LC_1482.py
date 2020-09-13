

class Solution:
    def minDays(self, bloomDay, m: int, k: int) -> int:
        left = 1
        right = max(bloomDay)
        n = len(bloomDay)

        # total is less then m * k flowers
        if n < m * k:
            return -1

        while left < right:
            mid = left + (right - left) // 2
            if self.check(mid, bloomDay, m, k):
                right = mid
            else:
                left = mid + 1
        return left

    def check(self, day, bloomDay, m, k):
        consecutive = 0  # count
        bouquets = 0  # res
        for i in range(len(bloomDay)):
            if bloomDay[i] > day:
                consecutive = 0
            else:
                consecutive += 1
                if consecutive == k:
                    bouquets += 1
                    consecutive = 0

        return bouquets >= m


