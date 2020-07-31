"""
906.Super-Palindromes
对于最大值为1e18的super palindrome，其平方根最大为1e9。因为这个平方根也要求是回文数，因此我们通过“遍历回文数的前半部分再镜像”的方法，
最多只需要遍历11e5就可以构造出11e9范围内所有的回文数，继而检查一下它的平方是否是超级回文数即可。整个时间复杂度控制在1e5的数量级，是可以接受的。

Similar to 866 - Prime Palindrome

1 - 1e5  ->construct ->  1 - 1e9 then square 1 - 1e18
                         palindrome            palindrome



"""


class Solution:
    def superpalindromesInRange(self, L: str, R: str) -> int:
        count = 0
        start = int(pow(10, len(L) // 4 - 1))
        end = int(pow(10, len(R) // 4 + 1))

        for num in range(start, end):
            for odd in range(2):
                palin = self.constructPalin(num, odd)
                if palin > 1e9:
                    continue
                superPalin = palin * palin
                if superPalin >= int(L) and superPalin <= int(R) and self.isPal(superPalin):
                    count += 1

        return count

    def constructPalin(self, num, odd):
        pal = num
        if odd == 1:
            num //= 10

        # doing reverse number for the second half of palindrome number
        while num > 0:
            pal = pal * 10 + num % 10
            num //= 10
        return pal

    def isPal(self, num):
        return str(num) == str(num)[::-1]





