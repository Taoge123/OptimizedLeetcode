"""
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


"""


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

