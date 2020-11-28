"""

dp(i) : min[1+dp(i-1), 1+dp(i//2), 1+dp(i//3)]
1553.Minimum-Number-of-Days-to-Eat-N-Oranges
本题并没有严格的数学解，只能通过递归探索。通常而言，每一步我们都有三个分支：-1，/2（如果能被2整除），/3（如果能被3整除）。但事实上，一直往1这条分支走下去的话，肯定不是效率高的解。我们需要探索的其实尽可能地去/2或者/3.能“早做除法”肯定不会比“晚做除法”吃亏。

举个例子，当n=11时，你可以先减一，就能除以2，这样2步得到5，再减1能得到4. 你也可以先减3次1，在除以2，这样4步得到4，但这比之前相比效率是低的。所以，直观上来说，能早做除法就尽量早出除法，不能做除法的时候，就做一些减法，再去做除法。

但是，/2和/3相比较，并没有更加优势的操作。比如说n=11，你是先打算减1再除以2呢，还是打算减2再除以3呢？很难判断。事实上最优方案是先实现/3：11,10,9,3,1,0. 但对于n=17，反而是先实现/2更优：17,16,8,4,2,1,0。所以我们需要对于/2和/3并行的探索。

所以递归方程其实就是：

f(n) = min(n%2+1+f(n/2), n%3+1+f(n/3))
那么时间复杂度如何计算呢？我们可以知道，从n递归到底的过程中，每层递归都会将参数/2(或者/3)，那么大致的层数就是logN。

对于第k层，意味着我们做了k次除法，这k次除法中/2的个数可能有0次，1次，2次...，直至有k次，这对应了k+1种不同状态。
举个例子，我们从n开始做了5次除法，假设有2次是/2，另外3次是/3，考虑到除法的顺序不影响递归的结果。只要n经过了两次/2和三次/3，剩下来的n'肯定都是一样。因此我们从n开始，经过第k层递归后，得到的只会是k+1种不同的n'。所以这是一个公差为1的等差数列。所以递归完所有的状态，需要记录总的状态就是 1+2+...+logN ~ o(logN^2)

2 ^ log(N) -> N -> (logN)^2
kth level : -> 1+k
f(n) -> k -> f(n')
        f(20)
    f(10)    f(6)
  f(5)  f(3)  f(2)


"""

import collections
from functools import lru_cache


class Solution:
    def __init__(self):
        self.res = {}

    def minDays(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 2
        if n in self.res:
            return self.res[n]

        res = min(n % 2 + self.minDays(n // 2), n % 3 + self.minDays(n // 3)) + 1
        self.res[n] = res
        return res



class Solution2:
    @lru_cache()
    def minDays(self, n: int) -> int:
        if n <= 1:
            return n
        return 1 + min(n % 2 + self.minDays(n // 2), n % 3 + self.minDays(n // 3))


class SolutionBFS:
    def minDays(self, n: int) -> int:
        queue = collections.deque([n])
        days = 0
        visited = set()

        while queue:
            days += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if node == 1:
                    return days
                if node % 3 == 0 and node % 3 not in visited:
                    queue.append(node // 3)
                    visited.add(node // 3)
                if node % 2 == 0 and node % 2 not in visited:
                    queue.append(node // 2)
                    visited.add(node // 2)
                if node - 1 not in visited:
                    queue.append(node - 1)
                    visited.add(node - 1)



