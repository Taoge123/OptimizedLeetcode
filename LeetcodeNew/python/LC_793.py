
class Solution:
    def preimageSizeFZF(self, K: int) -> int:
        left = 0
        right = 10 ** 5 * (K + 1)
        while left < right:
            mid = left + (right - left) // 2
            count = self.cal2(mid)
            if count == K:
                return 5
            elif count < K:
                left = mid + 1
            else:
                right = mid
        return 0

    def cal(self, num):
        res = 0
        while num > 0:
            res += num // 5
            num //= 5
        return res

    def cal2(self, num):
        if num == 0:
            return 0
        else:
            return num // 5 + self.cal2(num // 5)

