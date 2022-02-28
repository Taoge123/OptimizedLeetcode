"""
Similar with 1238

https://leetcode.com/problems/gray-code/discuss/30007/Python-Easy-Bit-Manipulation-Solution

The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

Example 1:

Input: 2
Output: [0,1,3,2]
Explanation:
00 - 0
01 - 1
11 - 3
10 - 2

For a given n, a gray code sequence may not be uniquely defined.
For example, [0,2,3,1] is also a valid gray code sequence.

00 - 0
10 - 2
11 - 3
01 - 1
Example 2:

Input: 0
Output: [0]
Explanation: We define the gray code sequence to begin with 0.
             A gray code sequence of n has size = 2n, which for n = 0 the size is 20 = 1.
             Therefore, for n = 0 the gray code sequence is [0].
"""
"""
089.Gray-Code
一个比较好理解、记忆和实现的生成算法如下：

假设我们已经有了两位的格雷码：00,01,11,10，如何生成三位的格雷码呢？

第一步将其镜像翻转并添加到自身的队列后面，得到00,01,11,10,||10,11,01,00。显然，除了镜像边缘的两个数，其他的数相邻之间都满足differ by 1 bit的关系。

然后，我们再将前一半的数最高位设为0，后一半的数最高位设为1，就得到000,001,011,010,||110,111,101,100.此时，镜像边缘的两个数也满足differ by 1 bit的关系，而其他位置的数相邻之间的格雷码约束依然不变。于是，这就得到了三位的格雷码！

我们循环利用上述的算法，不断往后推进，可以得到任意n位数的格雷码！

LC 1238. Circular Permutation in Binary Representation 和本题一模一样。
"""
"""
0   00    0 00
1   01    0 01
    11    0 11
    10    0 10
          1 10
          1 11
          1 01
          1 00
"""
"""
镜像法:

0 1
0 1 1 0 -> 00 01 11 10
00 01 11 10 | 10 11 01 00 -> 000 001 011 010 110 111 101 100


0   00    000
1   01    001
    11    011
    10    010
          110
          111
          101
          100

"""

class SolutionRika:
    def grayCode(self, n: int):
        res = []
        res.append(0)

        visited = set()
        visited.add(0)

        self.dfs(n, visited, 0, res)
        return res

    def dfs(self, n, visited, code, res):

        if len(res) == 1 << n:
            return True

        mask = 1
        for i in range(n):
            new_code = code ^ (mask << i)
            if new_code in visited:
                continue
            visited.add(new_code)
            res.append(new_code)
            if self.dfs(n, visited, new_code, res):
                return True
            visited.remove(new_code)
            res.pop()

        return False





class Solution:
    def grayCode(self, n):
        res = [0]
        if n == 0:
            return res
        for i in range(n):
            step = len(res)
            for j in range(step - 1, -1, -1):
                # 每次新加的要左移i位
                res.append(res[j] | (1 << i))

        return res


# class SolutionMirror:
#     def grayCode(self, n):
#         if n == 0:
#             return [0]
#         res = [0, 1]
#         for i in range(2, n + 1):
#             for j in range(len(res) - 1, -1, -1):
#                 res.append(res[j] | 1 << i - 1)
#         return res



class Solution:
    def grayCode(self, n):
        res = [0]
        for i in range(n):
            for num in reversed(res):
                # print(num, pow(2, i), list(reversed(res)), bin(num)[2:], bin(pow(2, i))[2:])
                res.append(num + pow(2, i))
                print(bin(num)[2:], bin(pow(2, i))[2:], bin(num + pow(2,i))[2:])

        return res





n = 4
a = Solution()
print(a.grayCode(n))



"""
0 1 [0]
1 2 [1, 0]
0 2 [3, 1, 0]
2 4 [2, 3, 1, 0]
3 4 [6, 2, 3, 1, 0]
1 4 [7, 6, 2, 3, 1, 0]
0 4 [5, 7, 6, 2, 3, 1, 0]
[0, 1, 3, 2, 6, 7, 5, 4]
"""


