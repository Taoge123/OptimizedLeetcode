"""
1643. Kth Smallest Instructions

The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.
Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"

"""
"""
1 + {2,3,4}
2 + {1,3,4}
3 + {1,2,4}
4 + {1,2,3}

18 = 3421

res  :
fact :

i = 4 index=17/6=2  k=17%6=5 
i = 3 index=5/2=2   k=5%2=1
i = 2 index=1/1=1   k=1%1=0

4 3 2 1
3 4 2 1

"""

from itertools import permutations
import math

"""
"123"
"132"
"213"
"231"
"312"
"321"


1234567
1765432


1XXXXXX
2XXXXXX
...
YXXXXXX


1 + {2, 3, 4}
2 + {1, 3, 4}
3 + {1, 2, 4}
4 + {1, 2, 4}

res  : 1 2 3 4 
fact : 1 1 2 6

k = 17
i = 4 index = 17 // 6 = 2 -> k = 17 % 6 = 5
i = 3 index = 5 // 2 = 2  -> k = 5 % 2 = 1
i = 4 index = 1 // 1 = 1  -> k = 1 % 1 = 0

首先，创建一个集合，存储数字选项1,2,3,4,5,6,7,8,9。

假设第一个位置的数字是1，那么总共有多少个这样的全排列呢？显然就是考虑第2~N位上用数字2~N去做全排列，就是(N-1)!个可能。
同理，第一个位置如果是2的话，那么也有(N-1)!个可能；第一个数字是3，同理也有(N-1)!个可能……

所以，用k除以(N-1)!得到的结果，就可以确定第一个位置的数字。例如：4xxxxxxxx符合要求的全排列共有(N-1)!*4个，
形如5xxxxxxxx符合要求的全排列共有(N-1)!*5个，假设k除以(N-1)!的结果大于4且小于5，那么说明所需要的第k大的全排列一定在这两者之间。
故它的第一个位置的数字一定是5。这里需要注意一个技巧，我们预先将k减去1，这样我们其实寻找的是0-index标准下的第k个全排列。
这样a=k/(N-1)!无论是否整除，a的值就意味着我们需要在digit（剩余）的集合里面找第a个元素（同样是0-index）。

同理，接下来考虑第二个位置的数字。注意到刚才已经排除了形如4xxxxxxxx的排列，剩下来我们其实寻找的就是以5开头的、第k-(N-1)!*4个全排列。
所以我们更新k-=(N-1)!*4，此时的任务演变成了：求由N-1个元素组成的全排列里面第k个是多少。
我们可以重复上面的方法，通过查看k/(N-2)!的结果来判定第二位上的数字是什么。注意，每确定了一个数字，
就需要从digit集合中删除那一个避免重复使用。

依次类推，就可以确定所有位置上的数字。值得指出的是，当n降为1的时候，此时的k一定会是零。


"""


class SolutionTest:
   def getPermutation(self, n: int, k: int) -> str:
       """
       O(n^2)
       O(n)
       """
       nums = list(range(1, n + 1))
       size = n
       res = ''
       k -= 1
       while size > 0:
           size -= 1
           index, k = divmod(k, math.factorial(size))
           res += str(nums[index])
           nums.remove(nums[index])
       return res


class SolutionWisdom:
    def getPermutation(self, n: int, k: int) -> str:
        digits = []
        for i in range(1, n + 1):
            digits.append(i)
        fact = [1] + [0] * (n - 1)
        for i in range(1, n):
            fact[i] = i * fact[i - 1]
        k -= 1
        res = []
        while n > 0:
            idx = k // fact[n - 1]
            res.append(digits[idx])
            k -= idx * fact[n - 1]
            n -= 1
            digits.pop(idx)

        return "".join(map(str, res))




class Solution:
    def getPermutation(self, n: int, k: int) -> str:

        nums = []
        for i in range(1, n + 1):
            nums.append(i)

        fact = [1] + [0] * (n - 1)
        for i in range(1, n):
            fact[i] = i * fact[i - 1]

        k -= 1
        res = []
        # or while nums, as long as we have nums left
        while n > 0:
            a = k // fact[n - 1]
            res.append(str(nums[a]))
            k -= a * fact[n - 1]
            n -= 1
            nums.pop(a)
        return "".join(res)






class Solution:
    def getPermutation(self, n, k):

        permutation = permutations(range(1, n+1))
        while k>0:
            res = next(permutation)
            k -= 1
        return ''.join([str(i) for i in res])



class SolutionCaikehe:
    def getPermutation(self, n, k):
        res, nums = "", range(1, n + 1)
        k -= 1
        while n:
            n -= 1
            index, k = divmod(k, math.factorial(n))
            res += str(nums.pop(index))
        return res


class Solution2:
    def getPermutation(self, n, k):
        numbers = range(1, n+1)
        permutation = ''
        k -= 1
        while n > 0:
            n -= 1
            # get the index of current digit
            index, k = divmod(k, math.factorial(n))
            permutation += str(numbers[index])
            # remove handled number
            numbers.remove(numbers[index])

        return permutation


class Solution3:
    def getPermutation(self, n: int, k: int) -> str:
        res = []
        for i in range(1, n + 1):
            res.append(i)

        fact = [1] + [0] * (n - 1)
        for i in range(1, n):
            fact[i] = i * fact[i - 1]

        k -= 1
        sb = []
        for i in range(n, 0, -1):
            index = k // fact[i - 1]
            k = k % fact[i - 1]
            print(index, k, res, res[index])
            sb.append(res[index])
            res.pop(index)

        return "".join(map(str, sb))


n = 4
k = 9

a = Solution3()
print(a.getPermutation(n, k))

