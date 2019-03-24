
"""
Write a program to find the nth super ugly number.

Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k.

Example:

Input: n = 12, primes = [2,7,13,19]
Output: 32
Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first 12
             super ugly numbers given primes = [2,7,13,19] of size 4.
"""
"""
The idea is similar to 264 Ugly Number II. 
The insight is that each new ugly number is generated from the previous ugly number by multiplying one of the prime. 
Thus we can maintain a pointer for each prime which indicates the current position of the generated ugly number list. 
Then there is a new ugly number from each prime, then we find the minimum one from them. 
Naturally the minimum one can be found by min-heap.

The Java version is accepted by 474 ms, but not the python version.

UPDATE: Thanks Stefan for pointing out that the complexity of this algorithm is NOT O(nlog(k)). 
I have modified the Python code and it was just accepted by 800 ms; 
the modified Java code is accepted by 160 ms. 
I will keep the original inefficient code here and Please check the updated code below...
"""

import heapq

class Solution:
    def nthSuperUglyNumber(self, n, primes):

        # Use the heap to find the next one
        q, uglyNums = [], [1]
        k = len(primes)
        for i in range(k):
            heapq.heappush(q, (primes[i], 0, primes[i]))
        while len(uglyNums) < n:
            x, i, p = q[0]
            uglyNums += [x]
            while q and q[0][0] == x:
                x, i, p = heapq.heappop(q)
                heapq.heappush(q, (p * uglyNums[i+1], i+1, p))
        return uglyNums[-1]



"""
这道题让我们求超级丑陋数，是之前那两道Ugly Number 丑陋数和Ugly Number II 丑陋数之二的延伸，质数集合可以任意给定，这就增加了难度。
但是本质上和Ugly Number II 丑陋数之二没有什么区别，由于我们不知道质数的个数，我们可以用一个idx数组来保存当前的位置，
然后我们从每个子链中取出一个数，找出其中最小值，然后更新idx数组对应位置，注意有可能最小值不止一个，要更新所有最小值的位置
"""
class Solution2:
    def nthSuperUglyNumber(self, n, primes):
        # Use the heap to find the next one
        q, uglyNums = [], [1]
        k = len(primes)
        for i in range(k):
            heapq.heappush(q, (primes[i], 0, primes[i]))

        while len(uglyNums) < n:
            x, i, p = q[0]
            uglyNums += [x]
            while q and q[0][0] == x:
                x, i, p = heapq.heappop(q)
                heapq.heappush(q, (p * uglyNums[i+1], i+1, p))

        return uglyNums[-1]

class Solution22:
    def nthSuperUglyNumber(self, n, primes):
        if not n or n < 1 or not primes:
            return 0
        res = [1]
        heap = [(prime, 0, prime) for prime in primes]
        heapq.heapify(heap)
        for i in range(1, n):
            val, idx, prime = heapq.heappop(heap)
            res.append(val)
            heapq.heappush(heap, (res[idx + 1] * prime, idx + 1, prime))
            while heap[0][0] <= val:
                _, idx, prime = heapq.heappop(heap)
                heapq.heappush(heap, (res[idx + 1] * prime, idx + 1, prime))
        return res[-1]

class Solution3:
    def nthSuperUglyNumber(self, n, primes):

        ugly = [1] * n
        i_list = [-1] * len(primes)
        v_list = [1] * len(primes)
        k = 0
        while k < n:
            x = min(v_list)
            ugly[k] = x
            for v in range(len(v_list)):
                if x == v_list[v]:
                    i_list[v] += 1
                    v_list[v] = ugly[i_list[v]] * primes[v]
            k += 1
        return ugly[k-1]



n = 12
primes = [2,7,13,19]

a = Solution22()
print(a.nthSuperUglyNumber(n, primes))




