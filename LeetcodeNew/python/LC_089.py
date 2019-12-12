"""
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


class Solution:
    def grayCode(self, n):
        results = [0]
        for i in range(n):
            for x in reversed(results):
                print(x, pow(2, i), list(reversed(results)))
                results.append(x + pow(2, i))

        return results



n = 3
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


