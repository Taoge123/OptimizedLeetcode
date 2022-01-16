
"""

ok so there is concept of binary lifting,
what is binary lifting ??

So any number can be expressed power of 2,
and we can greedily find that ,
by taking highest powers and taking the modulo,
or just utilising the inbuilt binary format that
how numbers are stored in computer,
so we know how to represent k in binary format,
so now using the same concept we will jump on k height using binary powers,
and remove the highest power ,
but here we must know the 2^i th height parent from every node,
so we will preprocess the tree as shown in the code,
so u could see as 2^i = 2^(i-1) + 2^(i-1),
so if we calculated 2^(i-1) th parent of every node beforehand
we could calculate 2^i th parent from that,
like 2^(i-1) th parent of 2^(i-1) th parent of the node,
right like 4th parent is 2nd parent of 2nd parent of node,
this is called binary lifting.

so now utilise the binary version of k and jump accordingly.
I have also made parent of 0 to -1,
so that I could stop if I went above the node.

假设parent[node][0]标记了每个node的1代祖先，所以如果想知道node的7代祖先，可以将node=parent[node][0]执行7次。

假设我们额外知道每个node的2代祖先，记做p[node][1]，那么我们对node的7代祖先只要做4次操作：（7=2^0+2^1+2^1+2^1）

node = parent[node][0], node = p[node][1], node = p[node][1], node = p[node][1]
假设我们额外知道每个node的4代祖先，记做p[node][2]，那么我们对node的7代祖先只要做3次操作：（7=2^0+2^1+2^2）

node = p[node][0], node = p[node][1], node = p[node][2]
由此可知，如果我们预先知道每个node的2^i代祖先parent[node][i]，那么我们就能减少query的次数。这样能减少多少呢？对于node的k代祖先，只需要将k做二进制分解，有多少个为1的bit，就做多少次query。考虑到k<=5*10^4，最多只需要20次query，就能够实现查询任意k代祖先。

        for (int i=0; i<20; i++)
        {
            if ((k>>i)&1)
            {
                node = p[node][i];
                if (node == -1) break;
            }
        }
        return node;
接下来我们考虑如何构建p[node][j].

我们知道node的4代祖先p[node][2]，可以通过两次2代祖先的query来实现，即node=p[node][1], node=p[node][1]。于是我们可以发现，如果知道了p[node][j-1]，就可以推出p[node][j]。即p[node][j] = p[p[node][j-1]][j-1]。所以我们设置两层循环，外循环从小到大确定j，内循环设置node，就可以设置所有的p[node][j]了。

这种思想叫做binary lifting.


binary lifting
p[node][0]  2^0 = 1

p[node][1]  2^1 = 2

p[node][2]  2^2 = 4

p[node][3]  2^3 = 8

k = a0*2^0 + a1*2^1 + a2*2^2 + a3*2^3 + ... + ak*2^k ai = 1/0

p[node][j] : node's 2 ^ j-th ancester

"""

from functools import lru_cache


class TreeAncestor:
    def __init__(self, n: int, parent):
        self.dp = [[-1 for i in range(20)] for j in range(n)]
        for i in range(n):
            self.dp[i][0] = parent[i]

        for i in range(n):
            for j in range(1, 20):
                if self.dp[i][j - 1] != -1:
                    self.dp[i][j] = self.dp[self.dp[i][j - 1]][j - 1]

    def getKthAncestor(self, node: int, k: int) -> int:
        for i in range(20):
            if ((k >> i) & 1):
                node = self.dp[node][i]
                if node == -1:
                    break
        return node



class TreeAncestor2:
    def __init__(self, n: int, parent):
        self.p = parent

    @lru_cache(None)
    def helper(self, node, p2):  # return getKthAncestor(node, 2**p2)
        if node == -1:
            return -1
        if p2 == 0: return self.p[node]
        return self.helper(self.helper(node, p2 - 1), p2 - 1)

    def getKthAncestor(self, node: int, k: int) -> int:
        i = 0
        while k:
            if k & 1: node = self.helper(node, i)
            k //= 2
            i += 1
        return node
