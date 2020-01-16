
"""
Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 231.

Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.

Could you do this in O(n) runtime?

Example:

Input: [3, 10, 5, 25, 2, 8]

Output: 28

Explanation: The maximum result is 5 ^ 25 = 28.
"""


"""
[3, 10, 5, 25, 2, 8] = [00011, 01010, 00101, 11001, 00010, 01000]
a^b=c, a^c=b,
a^b=max, a^max=b
mask = 10000 -> [00000, 00000, 00000, 10000, 00000, 00000], maximum = 10000 ? true
mask = 11000 -> [00000, 01000, 00000, 11000, 00000, 01000], maximum = 11000 ? true
mask = 11100 -> [00000, 01000, 00100, 11000, 00000, 01000], maximum = 11100 ? true
mask = 11110 -> [00010, 01010, 00100, 11000, 00010, 01000], maximum = 11110 ? false -> maximum = 11100
mask = 11111 -> [00011, 01010, 00101, 11001, 00010, 01000], maximum = 11101 ? false -> maximum = 11100
maximum = 11100 = 28


我们还需要用上一个异或的特性，假设a和b产生了最终的答案max，即a ^ b = x，
那么根据异或的特性，a ^ x = b。同理，a和b的最高位（前n位）也有相同的性质。

先以最高位为例子，我们可以把所有的数字的最高位放到一个HashSet里面，
然后使用1与set里面的所有数字进行异或，如果得出的结果仍然在set里面，那么最终结果的最高位必然为1，
否则为0。也即，先假定结果为1，然后与set中所有数字异或，假定a与1异或得到结果b（a ^ 1 = b），
而b仍然在set里面，那么说明set中有两个数字异或能得到1（a ^ b = 1）。
否则，set中没有两个数字能够异或得到1，那么最终结果的最高位为1的假设失败，说明最终结果的最高位为0。
以此类推可以得到第二位、第三位。。。的数字。

再做一下推广，我们将所有数字的前N位放到一个HashSet里面，然后使用之前N-1位得到的最大值前缀prefix与set里面的所有数字进行异或，
如果得出的结果仍然在set中，那么第N位必然为1，否则为0。

举个例子，给定数组[14, 11, 7, 2]，二进制表示分别为[1110, 1011, 0111, 0010]。
题目说了，数字最长不会超过32位，所以应从i = 31开始，但是所有数字中最多位4位数，简单起见，我直接从最高位i=3开始

1. i = 3, set = {1000, 0000} => max = 1000
2. i = 2, set = {1100, 1000, 0100, 0000} => max = 1100
3. i = 1, set = {1110, 1010, 0110, 0010} => max = 1100
4. i = 0, set = {1110, 1011, 0111, 0010} => max = 1100
最终答案是1100 => 12，1011 ^ 0111 = 1100(11 ^ 7 = 12)

"""


class Solution:
    def findMaximumXOR(self, nums) -> int:

        res, mask = 0, 0
        for i in range(31, -1, -1):
            possible_mx = res | 1 << i
            mask = mask | 1 << i
            bits = set()
            for num in nums:
                bits.add(num & mask)
                # print(bin(num)[2:], bin(num&mask)[2:])
            print([bin(i)[2:] for i in bits])

            for bit in bits:
                if bit ^ possible_mx in bits:
                    res = possible_mx
                    break
        return res



nums = [3, 10, 5, 25, 2, 8]
a = Solution()
print(a.findMaximumXOR(nums))





