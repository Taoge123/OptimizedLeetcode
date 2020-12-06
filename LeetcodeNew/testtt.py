import collections


class Solution:
    def concatenatedBinary(self, n: int) -> int:

        stack = []
        mod = 10 ** 9 + 7
        for i in range(1, n + 1):
            stack.append(bin(i)[2:])
        stack = "".join(stack)
        stack = stack[::-1]
        # print(stack)
        res = 0
        count = 0
        for i, ch in enumerate(stack):
            # print(int(ch), i)
            if ch == '1':
                count += 1
                res += pow(2, i)
            if count > 57000:
                break

        return res % mod


n = 8933
a = Solution()
print(a.concatenatedBinary(n))

