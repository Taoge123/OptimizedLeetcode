"""

我们首先计算每个位置上字符需要自增的次数，也就是s[i]-t[i]之差。假设如果有两个位置都需要自增5，那么最终的方案是我们只能先给其中一个位置自增5（在第5次move时操作），另一个位置则通过自增5+26=31（在第31次move时操作））来实现转换。

所以我们的算法是，遍历每个位置，然后统计count[k] (k=1,2...,25)，表示需要自增k次的位置有几个。如果有若干个，那么它们分别需要在第k次、第k+26次、第k+52次...来实现。最终的答案就是所有位置里，需要操作的最晚的那一次。

"""


import collections


class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False

        count = collections.defaultdict(int)
        for i, j in zip(s, t):
            if i == j:
                continue
            diff = ord(j) - ord(i)
            if diff < 0:
                diff += 26
            if diff > k:
                return False
            if diff not in count:
                count[diff] = diff
            else:
                prev = count[diff]
                if prev + 26 > k:
                    return False
                count[diff] = prev + 26

        return True




