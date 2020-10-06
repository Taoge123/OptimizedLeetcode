"""
We scan through S from left to right:

If it's monotonically increasing we just adding corresponding part to result
If not then we simply decrease result by 1, which would result in some 9s in the tail
However, decrease by 1 might lead to our result being not monotonically increasing, so we run recursion base on our current result number
Example - say the input was 1221

i=0, res=1000
i=1, res=1200
i=2, res=1220
i=3, res=1219 because it's not increasing anymore
then we recursively call with input being 1219
i=0, res=1000
i=1, res=1200
i=2, res=1199 because it's not increasing anymore
then we recursively call with input being 1199
voila! we got it

"""



class Solution:
    def monotoneIncreasingDigits(self, N):
        s = str(N)
        n = len(s)
        res = 0
        for i in range(len(s)):
            if i == 0 or s[i] >= s[i-1]:
                res += int(s[i]) * pow(10, n - 1)
            else:
                return self.monotoneIncreasingDigits(res - 1)
            n -= 1
        return res




class Solution2:
    def monotoneIncreasingDigits(self, N: int) -> int:
        if N == 10:
            return 9
        if N < 20:
            return N
        num = [s for s in str(N)]
        i = len(num) - 1
        index = len(num)
        while i > 0:
            if int(num[i]) < int(num[i - 1]):
                num[i - 1] = str(int(num[i - 1]) - 1)
                index = i
            i -= 1
        for n in range(index, len(num)):
            num[n] = '9'
        return int(''.join(s for s in num))

