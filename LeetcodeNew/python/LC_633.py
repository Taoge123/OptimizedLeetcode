import math


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for i in range(int(math.sqrt(c)) + 1):
            num = math.sqrt(c - i * i)
            if num == int(num):
                return True
        return False



class Solution2:
    def judgeSquareSum(self, c: int) -> bool:
        for i in range(int(math.sqrt(c)) + 1):
            num = c - i * i
            if self.binarySearch(0, num, num):
                return True
        return False


    def binarySearch(self, left, right, num):
        if left > right:
            return False

        mid = (right - left) // 2 + left
        if mid * mid == num:
            return True
        elif mid * mid > num:
            return self.binarySearch(left, mid - 1, num)
        else:
            return self.binarySearch(mid + 1, right, num)


