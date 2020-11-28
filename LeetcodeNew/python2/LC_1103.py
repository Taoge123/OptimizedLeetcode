"""
Intuition
Brute force of simulation seems to be easy.
But how is the time complexity?


Explanation
The i-th distribution,
we will distribute i + 1 candies to (i % n)th people.
We just simulate the process of distribution until we ran out of candies.

Complexity
Time O(sqrt(candies))
Space O(N) for result

The number of given candies is i + 1, which is an increasing sequence.
The total number distributed candies is c * (c + 1) / 2 until it's bigger than candies.
So the time it takes is O(sqrt(candies))
"""


class Solution:
    def distributeCandies(self, candies: int, num_people: int):

        cur = 1
        res = [0] * num_people
        i = 0
        while candies:
            if candies >= cur:
                candies -= cur
                res[i] += cur
                cur += 1
                i = (i + 1) % num_people
            else:
                res[i] += candies
                candies = 0
        return res


class SolutionLee:
    def distributeCandies(self, candies, n):
        res = [0] * n
        i = 0
        while candies > 0:
            res[i % n] += min(candies, i + 1)
            candies -= i + 1
            i += 1
        return res


"""
 1 2 3 4 ... N                   (1+n)*n//2 + n*n*0
 N+1 N+2 N+3 N+4 ... N+N         (1+n)*n//2 + n*n*1
 2N+1 2N+2 2N+3 2N+4 ... 2N+N    (1+n)*n//2 + n*n*2

 i+1, i+1+n, i+1+n*2 -> i+1+(n*k)
 带summation公式:
 if k > 1:
     ((i+1) + (i+1+(n*k)) * k) // 2
 else:


1103.Distribute-Candies-to-People
这道题不难，用全程模拟的方法，代码可以很短，但是效率不是很高。一种提升效率的方法就是计算出这些糖能够发几轮（比如说k轮），
那么前k轮中每个人可以得到的糖的数目就可以直接用数列求和算出来。

第一轮：1,2,3,..., N
第二轮：1+N,2+N,3+N,..., 2N
第三轮：1+2N,2+2N,3+2N,..., 3N
...
可见，完整的第k轮，总共需要发放糖果数目是(1+N)*N/2+N*N*k。将candies的数目逐轮减去这个数目，就可以知道k是几。

然后，对于前k轮，第i个人得到的糖果数目也就是个等差数里：i+1, i+1+N, i+1+2N, ..., i+1+(k-1)*N，求和之后就是(i+1+i+1+(k-1)*N)*k/2.

至于剩下糖果的零头，就再走一遍即可。此时是第k+1轮，第0个人需要1+kN个糖果，第1个人需要2+kN个糖果,...。一路分发，直至看糖果最终在哪个人手里用完。

"""


class SolutionWisdom:
    def distributeCandies(self, candies: int, num_people: int):
        n = num_people
        c = candies
        k = 0

        #k 表示可以发多少轮
        while c > ((1 + n) * n // 2 + n * n * k):
            c -= ((1 + n) * n // 2 + n * n * k)
            k += 1

        res = [0] * n
        if k > 0:
            for i in range(n):
                # 用求和公式算出每个需要多少
                res[i] = ((i + 1) + (i + 1 + (n * (k - 1)))) * k // 2

        # 发出事状态
        for i in range(n):
            if c >= i + 1 + n * k:
                res[i] += i + 1 + n * k
                c -= i + 1 + n * k
            else:
                res[i] += c
                break

        return res


