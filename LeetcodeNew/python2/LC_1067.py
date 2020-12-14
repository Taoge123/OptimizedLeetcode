"""
https://xingxingpark.com/Leetcode-1067-Digit-Count-in-Range/
解题思路
这道题我们用递归的方式，递归函数为recursiveCount(N, d), 将N当中出现d的次数分为个位数中出现的次数，加上非个位数出现的次数。
个位数出现的次数为N/10, 非个位数中出现的次数为recursiveCount(N / 10, d) * 10, 可以理解为N / 10中每一个数都可以加后缀0 - 9成为N中的一个数字。
当然还要考虑最后一位的大小，从而加减一个偏差，详见代码注释。


"""


class Solution:
    def digitsCount(self, d, low, high):
        return self.count(high + 1, d) - self.count(low, d)

    def count(self, num, d):
        if num == 0:
            return 0
        if d == 0 and num <= 10:
            return 0
        res = 0
        # 判断最后一次个位数字是否包含d，e.g. N=797，判断790-797之间个位数字是否出现d
        if num % 10 > d:
            res += 1

        # 前面默认最后一位到9，因此我们要减去最后一位不到9的情况，e.g. N=797, 我们计算798 - 799两数非个位数字出现d的次数
        if num // 10 > 0:
            res += str(num // 10).count(str(d)) * (num % 10)
        if d:
            res += num // 10
        else:
            res += num // 10 - 1
        # 个位数字d出现的次数，不包含最后一次，e.g. N=797，这里只计算1 - 789之间个位数字出现d的次数
        res += self.count(num // 10, d) * 10
        return res


