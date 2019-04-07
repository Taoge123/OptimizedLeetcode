
"""
On a horizontal number line, we have gas stations at positions stations[0], stations[1], ...,
stations[N-1], where N = stations.length.

Now, we add K more gas stations so that D, the maximum distance between adjacent gas stations, is minimized.

Return the smallest possible value of D.

Example:

Input: stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], K = 9
Output: 0.500000
Note:

stations.length will be an integer in range [10, 2000].
stations[i] will be an integer in range [0, 10^8].
K will be an integer in range [1, 10^6].
Answers within 10^-6 of the true value will be accepted as correct.

"""
"""
思路：

1、采用优先队列：采用优先队列的思路比较简单：就是每次找出gap最大的一个区间，然后新加入一个station，
直到所有的k个station都被加入，此时最大的gap即为所求。在实现上我们采用优先队列，使得每次最大的gap总是出现在队首。
这种方法的空间复杂度是O(n)，时间复杂度是O(klogn)，其中k是要加入的新station的个数，n是原有的station个数。
这种方法应该没毛病，但是还是没有通过所有的数据测试。
"""
"""
2、采用二分查找：在网上参考了采用二分查找的实现。我们容易得知，minmaxGap的最小值left = 0，
最大值right = stations[n - 1] - stations[0]。我们每次取mid为left和right的均值，然后计算如果mimaxGap为mid，
那么最少需要添加多少个新的stations，记为count。所以如果count > K，说明均值mid选取的过小，
使得我们必须新加更多的stations才能满足要求，所以我们就更新left的值；否则说明均值mid选取的过大，
使得我们需要小于K个新的stations就可以达到要求，那么我们此时就可以寻找更小的mid，使得count增加到K。
如果我们假设stations[N - 1] - stations[0] = m，那么这种实现的空间复杂度是O(1)，时间复杂度是O(nlogm)，可以发现与k无关了
"""
"""
Why did I use s binary search?
In fact there are some similar problems on Leetcode so that is part of experience.
Secondly, I got a hint from "Answers within 10^-6 of the true value will be accepted as correct.". 
The first solution I tried was binary search.
Because binary search may not find exact value but it can approach the true answer.

Explanation of solution
Now we are using binary search to find the smallest possible value of D.
I initilze left = 0 and right = the distance between the first and the last station
count is the number of gas station we need to make it possible.
if count > K, it means mid is too small to realize using only K more stations.
if count <= K, it means mid is possible and we can continue to find a bigger one.
When left + 1e-6 >= right, it means the answer within 10^-6 of the true value and it will be accepted.

Time complexity:
O(NlogM), where N is station length and M is st[N - 1] - st[0]
"""
import math
import heapq

"""
1. what does mid mean? The variable mid here is actually a guess of the result, 
   for example, we guess the Max Distance is 1.3.

2. with this guess, how many gas stations we need? There are several situations,
   For example, mid = 1.3, arr = [1,2,4,8]
   how many gas stations between 1 and 2? 0,
   how many gas stations we need between 2 and 4? math.ceil((b - a) / mid) - 1 = ceil((4-2)/1.3) - 1 = 1
   how many gas stations we need between 4 and 8? ceil((8-4)/1.3) - 1 = 3

3. what should we do if we don't have enough K?
   Increase our guess, so we will need less extra gas stations. 
   For example, if we guess the Max Distance is 2.1, we only need K = 1

After that, shrink the range until it's accurate enough."""
class SolutionLee:

    def minmaxGasDist(self, st, K):
        left, right = 1e-6, st[-1] - st[0]
        while left + 1e-6 < right:
            mid = (left + right) / 2
            count = 0
            for a, b in zip(st, st[1:]):
                count += math.ceil((b - a) / mid) - 1
            if count > K:
                left = mid
            else:
                right = mid
        return right

class Solution11:
    def minmaxGasDist(self, stations, K):

        def possible(stations, K, guess):
            return sum(int((stations[i+1]-stations[i]) / guess)
                       for i in range(len(stations)-1)) <= K

        left, right = 0, 10**8
        while right-left > 1e-6:
            mid = left + (right-left)/2.0
            if possible(mid):
                right = mid
            else:
                left = mid
        return left

# We know that the minmax distance is no more than (station(n)-station(1)) / K, so let's start from there:
class Solution2:
    def minmaxGasDist(self, stations, K):
        d = (stations[len(stations)-1] - stations[0]) / float(K)
        heap = []
        for i in range(len(stations)-1):
            n = max(1, int((stations[i+1]-stations[i]) / d))
            K -= (n-1)
            heapq.heappush(heap, (float(stations[i]-stations[i+1]) / n, stations[i], stations[i+1], n))

        for i in range(K):
            (d, a, b, n) = heap[0]
            heapq.heapreplace(heap, ((a-b)/(n+1.0), a, b, n+1))
        return -heap[0][0]

class Solution3:
    def minmaxGasDist(self, stations, K):
        # runtime: 315ms
        s = stations
        d, heap = (s[-1] - s[0]) / float(K), []
        for v1, v2 in zip(s, s[1:]):
            x = max(1, int((v2 - v1) / d))
            K -= x - 1
            heapq.heappush(heap, (float(v1 - v2) / x, v1, v2, x))
        for i in range(K):
            (d, x, y, j) = heap[0]  # pop
            heapq.heapreplace(heap, ((x - y) / (j + 1.0), x, y, j + 1))
        return -heap[0][0]


class Solution4:
    def minmaxGasDist(self, stations, K):
        s = stations
        d, heap = float(s[-1]-s[0])/K, []
        for v1, v2 in zip(s, s[1:]):
            g = float(v2-v1)
            x = max(1, int(g/d))
            K-= x-1
            heapq.heappush(heap, (-g/x, g, x))
        for _ in range(K):
            _, g, x = heap[0]
            heapq.heapreplace(heap, (-g/(x+1), g, x+1))
        return -heap[0][0]








