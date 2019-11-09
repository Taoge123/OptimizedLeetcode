import collections

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return 0

        res = ""
        res += "-" if (numerator > 0) ^ (denominator > 0) else ""
        num, den = abs(numerator), abs(denominator)

        res += str(num // den)
        num %= den
        if num == 0:
            return res
        res += "."
        table = collections.defaultdict(int)
        table[num] = len(res)

        while num != 0:
            num *= 10
            res += str(num // den)
            num %= den

            if num in table:
                index = table[num]
                res = res[:index] + "(" + res[index:] + ")"
                break
            else:
                table[num] = len(res)
        return res



a = Solution()
print(a.fractionToDecimal(2,3))









