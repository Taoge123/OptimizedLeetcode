import math


class Solution:
    def sumFourDivisors(self, nums) -> int:
        res = 0
        for num in nums:
            div = set()
            for i in range(1, int(math.sqrt(num))+1):
                if num % i == 0 and i not in div:
                    div.add(i)
                    div.add(num//i)
                if len(div) > 4:
                    break
            if len(div) == 4:
                res += sum(div)
        return res


