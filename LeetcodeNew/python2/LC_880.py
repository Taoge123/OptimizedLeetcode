"""
假设我们当前的容器里面有一串已经解码的字符串t，其字符的长度是count。

这个时候如果我们接下来处理的是一个字符ch，那么显然，说明第count+1个字符一定就是ch。特别地，如果count+1==K，那么ch就是答案，否则我们还会继续往后扫描S。

这个时候如果我们接下来处理的是一个数字num，那么说明解码容器里的字符串t要增加num倍的长度。如果count*num < K，说明还没有走到第K个字符，我们还需要继续往后扫描S。
反之count*num >= K的话，说明这么多字符串t的串联用力过猛，我们可能只需要部分t的串联即可到达K。
考虑到t就是“循环节”，所求的第K个字符，其实就是在这个循环节里找第K%count元素即可。至此，我们发现，decodeAtIndex(S,K)此时变成了decodeAtIndex(t,K%count)，原来这题就是一个递归的解法。

特别注意，如果K%num==0的话，我们需要输出的是循环节里最后一个字符。

ha22 : 5
-> ha2 : 5 % 4 = 1
-> h
"""


class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        count = 0
        for i in range(len(S)):
            char = S[i]
            if char.isalpha():
                count += 1
                if count == K:
                    return char
            else:
                times = ord(char) - ord('0')
                if (count * times) < K:
                    count *= times
                elif K % count == 0:
                    return self.decodeAtIndex(S[0:i], count)
                else:
                    return self.decodeAtIndex(S[0:i], K % count)


class SolutionCs:
    def decodeAtIndex(self, S: str, K: int) -> str:
        i = 0
        size = 0
        while size < K:
            if S[i].isdigit():
                size *= (ord(S[i]) - ord('0'))
            else:
                size += 1
            i += 1
        i -= 1

        while True:
            if S[i].isdigit():
                size //= (ord(S[i]) - ord('0'))
                K %= size
            elif K % size == 0:
                return S[i]
            else:
                size -= 1
            i -= 1


S = "leet2code3"
K = 14
a = Solution()
print(a.decodeAtIndex(S, K))

