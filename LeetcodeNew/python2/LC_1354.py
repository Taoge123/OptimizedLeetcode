"""
last   round : X X X X a
last-1 round : X X m X b
last-2 round : X X d X b

a = x+x+x+x+b
b = a - others (others = x+x+x+x)

The total sum always bigger than all elements.
We can decompose the biggest number.
Each round we get the current maximum value,
delete it by the sum of other elements.

Time O(N) to build up the priority queue.
Time O(logMaxAlogN)) for the reducing value part.
We have O(maxA) loops, which is similar to gcd
Space O(N)

% operation is totally much more important than using heap.
If brute force solution is accepted,
then the solutions without % are right and good.

But the truth is that, solution without % should be TLE.
So I afraid that, without % is wrong to me.

"""

import heapq


class Solution:
    def isPossible(self, target: List[int]) -> bool:
        summ = sum(target)
        heap = []
        for num in target:
            heapq.heappush(heap, -num)

        while heap[0] != -1:
            maxi = -heapq.heappop(heap)
            # print(maxi)
            others = summ - maxi

            if others == 0:
                return False
            if maxi - others <= 0:
                return False

            #optimization, it was maxi - others
            b = maxi % others

            summ = others + b
            heapq.heappush(heap, -b)

        return True




class SolutionLee:
    def isPossible(self, target) -> bool:
        total = sum(target)
        nums = [-num for num in target]
        heapq.heapify(nums)
        while True:
            node = -heapq.heappop(nums)
            total -= node
            if node == 1 or total == 1:
                return True
            if node < total or total == 0 or node % total == 0:
                return False
            node %= total
            total += node
            heapq.heappush(nums, -node)




target = [9, 3, 5]
a = Solution()
print(a.isPossible(target))

