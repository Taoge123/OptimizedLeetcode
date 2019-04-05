
"""
https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/discuss/130522/python-trie-solution-O(n)
https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/discuss/171747/Python-O(n)-solution-easily-explained

Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 231.

Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.

Could you do this in O(n) runtime?

Example:

Input: [3, 10, 5, 25, 2, 8]

Output: 28

Explanation: The maximum result is 5 ^ 25 = 28.
"""

"""
对于[3,10,5,25,2,8]测试用例，如果使用O(n^2)算法，选取3与剩下的数进行异或。这个过程中对于5,10,8的二进制前28位异或结果是一样的，
对于10,8而言前30位异或结果是一致的。很容易想到对数组中的数的二进制，构建前缀树。相同前缀的计算结果可复用，就能提升效率。

建树
因为二进制元素只有0,1。考虑使用二叉树来构建前缀树。

根节点为符号位0
从高位到低位依次构建
左子树为1节点，又子树为0节点
[3,10,5,25,2,8] 按照以上规则构建如下图（省略高位0）
那么这颗树包含了数组中所有的数字，从根节点到叶子节点的一条路径表示数组中的一个十进制数的二进制编码。

找最大异或值
对于25 (0000 0000 0000 0000 0000 0000 0001 1001) 而言，从第31-6位（都是正数，不考虑符号位），都为0,，且数组中的数字31-6位都为0，因此最大异或结果31-6位只能为0。
当前使得异或结果最大的数x为0000 0000 0000 0000 0000 0000 000? ????
当前指针curNode指向第图中根节点。
从第5位开始：
5 1 x的第5位为0，则结果最大。应选择右分支，curNode = curNode->right
4 1 x的第4位为0，则结果最大。应选择右分支，curNode = curNode->right
3 0 x的第3位为1，则结果最大。应选择左分支，curNode = curNode->left
2 0 x的第2位为1，则结果最大。应选择左分支，但树中左分支为null，只能选择右分支curNode = curNode->right 于是x的第2位为0。
1 1 x的第1位为0，则结果最大。应选择右分支，但树中右分支为null，只能选择左分支curNode = curNode->left 于是x的第1位为1。
找到的x为5（00101）。
"""
"""
1. Build a Trie with the nodes as 0 and 1. The trie will have the binary representation(32 bit) for each word.
2. Traverse down the Trie for each num and calculate the XOR for each.
3. Get the maximum.
"""


class TrieNode():
    def __init__(self):
        self.one = None
        self.zero = None


class Solution1:
    def findMaximumXOR(self, nums):

        root = TrieNode()
        for num in nums:
            node = root
            for j in range(31, -1, -1):
                tmp = num & 1 << j
                if tmp:
                    if not node.one:
                        node.one = TrieNode()
                    node = node.one
                else:
                    if not node.zero:
                        node.zero = TrieNode()
                    node = node.zero

        ans = 0
        for num in nums:
            node = root
            tmp_val = 0
            for j in range(31, -1, -1):
                tmp = num & 1 << j
                if node.one and node.zero:
                    if tmp:
                        node = node.zero
                    else:
                        node = node.one
                    tmp_val += 1 << j
                else:
                    if (node.zero and tmp) or (node.one and not tmp):
                        tmp_val += 1 << j
                    node = node.one or node.zero
            ans = max(ans, tmp_val)

        return ans





