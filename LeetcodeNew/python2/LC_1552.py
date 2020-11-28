

class Solution:
    def maxDistance(self, position, m: int) -> int:
        position.sort()
        left, right = 1, position[-1] - position[0]

        while left < right:
            # left=0, right=1, then left is still 0
            mid = right - (right - left) // 2
            if self.check(mid, position, m):
                left = mid
            else:
                right = mid - 1
        return left

    def check(self, dist, position, m):

        # first ball is always in postion[0]
        count = 1
        i = 0
        while i < len(position):
            j = i
            # find that position
            while j < len(position) and position[j] - position[i] < dist:
                j += 1
            if j == len(position):
                break
            else:
                # found it
                count += 1
                i = j
            if count == m:
                return True
        return False



class Solution2:
    def maxDistance(self, position, m: int) -> int:
        n = len(position)
        position.sort()

        left, right = 0, position[-1] - position[0]
        while left < right:
            mid = right - (right - left) // 2
            if self.count(mid, position) >= m:
                left = mid
            else:
                right = mid - 1
        return left

    def count(self, dist, position):
        n = len(position)
        res, curr = 1, position[0]
        for i in range(1, n):
            if position[i] - curr >= dist:
                res += 1
                curr = position[i]
        return res





