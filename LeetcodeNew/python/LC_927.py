"""
000[1xxxx] 00000 1xxx 00000[1xxxxx]
927.Three-Equal-Parts
本题的突破口就是全局1的个数。首先，整个数组里面1的个数必须要能被3整除。其次，确定了每个part里面1的个数后（记为count），从后往前数count个1，就已经确定了这个数长什么样了（记为X）。

然后我们从数组最前端开始忽略若干个先导零，从第一个出现1的地方开始判断这个subarray是否等于X。如果OK，那么我们再忽略若干个先导零，在从下一个出现1的地方开始判断这个subarray是否等于X。如果再OK，那么three equal parts就已经划分好了。

"""

class Solution:
    def threeEqualParts(self, A):
        count = A.count(1)
        if count % 3 != 0:
            return [-1, -1]
        if count == 0:
            return [0, len(A) - 1]

        # determine how many 1 appears in each part
        count //= 3
        res = []
        j = len(A)
        # 从后往前找1
        while count:
            j -= 1
            if A[j] == 1:
                count -= 1

        # 退出时, j到了last part的start
        # 000[1xxxx] 00000 1xxx 00000[1xxxxx]
        # j
        i = 0
        # 跳过所有的起始0
        while A[i] == 0:
            i += 1

        k = j
        while k < len(A) and A[i] == A[k]:
            i += 1
            k += 1
        # 跳出来either k goes to the end or A[i] != A[k]
        # 如果k没走到最后, 则A[i] != A[k], 直接不行了
        if k != len(A):
            return [-1, -1]
        res.append(i - 1)

        # 000[1xxxx] 00000 1xxx 00000[1xxxxx]
        #          i                  j

        # part 2 再来一次
        while A[i] == 0:
            i += 1
        # 000[1xxxx] 00000 1xxx 00000[1xxxxx]
        #                  i          j
        k = j
        while k < len(A) and A[i] == A[k]:
            i += 1
            k += 1

        if k != len(A):
            return [-1, -1]

        res.append(i)
        return res


