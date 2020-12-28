"""
1702.Maximum-Binary-String-After-Change
将字符串最大化的最高效的一步操作，就是将最高位的0变成1.而我们能用的规则就是操作1："00"->"10"。但是这一步需要0后面有个额外的0才能实现。
那么0后面紧接着的如果是个1怎么办呢？这时候观察操作2，它的本质就是将0往前移动。这说明如果只要字符串的后面还有0，就可以将它提上来凑成两个连续的0，利用规则1，将此时最高位的0变成1.

接下来，此时最高位的0就是之前被提上来的0。想要将它也变成1的话，也需要同样的步骤：将字符串后面的0提前，凑成连续的两个0，再把最高位置成1.

可以想见，如果原先的字符串里有m个0的话，那么从最高位的0开始，连续m-1个位置都会重复上面的操作。最终留下第m个位置上是0，这是整个字符串目前为止仅剩的一个0，我们再也无法做其他操作使其变大了。

Greedy

"""


class Solution:
    def maximumBinaryString(self, binary: str) -> str:

        n = len(binary)
        count = 0

        for ch in binary:
            if ch == '0':
                count += 1

        if count <= 1:
            return binary

        i = 0
        res = ""
        while i < n and binary[i] == '1':
            res += '1'
            i += 1

        for i in range(count - 1):
            res += '1'

        res += '0'
        while len(res) < n:
            res += '1'

        return res






