"""
N couples sit in 2N seats arranged in a row and want to hold hands. We want to know the minimum number of swaps so that every couple is sitting side by side. A swap consists of choosing any two people, then they stand up and switch seats.

The people and seats are represented by an integer from 0 to 2N-1, the couples are numbered in order, the first couple being (0, 1), the second couple being (2, 3), and so on with the last couple being (2N-2, 2N-1).

The couples' initial seating is given by row[i] being the value of the person who is initially sitting in the i-th seat.

Example 1:

Input: row = [0, 2, 1, 3]
Output: 1
Explanation: We only need to swap the second (row[1]) and third (row[2]) person.
Example 2:

Input: row = [3, 2, 0, 1]
Output: 0
Explanation: All couples are already seated side by side.
Note:

len(row) is even and in the range of [4, 60].
row is guaranteed to be a permutation of 0...len(row)-1.
"""
"""
下面我们来看一种使用联合查找Union Find的解法。该解法对于处理群组问题时非常有效，比如岛屿数量有关的题就经常使用UF解法。核心思想是用一个root数组，每个点开始初始化为不同的值，如果两个点属于相同的组，就将其中一个点的root值赋值为另一个点的位置，这样只要是相同组里的两点，通过find函数会得到相同的值。 那么如果总共有n个数字，则共有 n/2 对儿，所以我们初始化 n/2 个群组，我们还是每次处理两个数字。每个数字除以2就是其群组号，那么属于同一组的两个数的群组号是相同的，比如2和3，其分别除以2均得到1，所以其组号均为1。那么这对解题有啥作用呢？作用忒大了，由于我们每次取的是两个数，且计算其群组号，并调用find函数，那么如果这两个数的群组号相同，那么find函数必然会返回同样的值，我们不用做什么额外动作，因为本身就是一对儿。如果两个数不是一对儿，那么其群组号必然不同，在二者没有归为一组之前，调用find函数返回的值就不同，此时我们将二者归为一组，并且cnt自减1，忘说了，cnt初始化为总群组数，即 n/2。那么最终cnt减少的个数就是交换的步数，还是用上面讲解中的例子来说明吧：

[3   1   4   0   2   5]

最开始的群组关系是：

群组0：0，1

群组1：2，3

群组2：4，5

取出前两个数字3和1，其群组号分别为1和0，带入find函数返回不同值，则此时将群组0和群组1链接起来，变成一个群组，则此时只有两个群组了，cnt自减1，变为了2。

群组0 & 1：0，1，2，3

群组2：4，5

此时取出4和0，其群组号分别为2和0，带入find函数返回不同值，则此时将群组0 & 1和群组2链接起来，变成一个超大群组，cnt自减1，变为了1

群组0 & 1 & 2：0，1，2，3，4，5

此时取出最后两个数2和5，其群组号分别为1和2，因为此时都是一个大组内的了，带入find函数返回相同的值，不做任何处理。最终交换的步数就是cnt减少值
"""

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.count = n // 2

    def find(self, i):
        if self.parent[i] == i:
            return i
        return self.find(self.parent[i])

    def union(self, i, j):
        x = self.find(i)
        y = self.find(j)
        if x != y:
            self.count -= 1
            self.parent[x] = y


class Solution:
    def minSwapsCouples(self, row) -> int:
        n = len(row)
        uf = UnionFind(n)
        for i in range(0, n, 2):
            uf.union(row[i] // 2, row[i + 1] // 2)
        return n // 2 - uf.count



"""
[3, 2, 0, 1]
 1  1  0  0
 
row = [0, 2,  1, 3]
       0  1   0  1 

"""


