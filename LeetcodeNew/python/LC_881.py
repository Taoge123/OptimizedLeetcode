"""

zzzzzzz x yyyyyyyy y
x, y 可以, y， z就可以

881.Boats-to-Save-People
解法1：
容易想到比较严谨的贪心解，就是找到当前最重的小胖x，然后找到当前最大的小瘦y使得x+y<=limit，这样x和y的配对是对资源的最优利用。

事实上这个贪心法可以进行松弛：对于当前最重的小胖x，只需要找到当前最小的小瘦y进行配对，就可以实现对资源的最优利用。分析如下。
假设我们将所有人从轻到重排序y1,y2,y3,y4,...,x4,x3,x2,x1。对于当前最重的小胖对应的是x1，假设如果根据严谨的贪心算法找到的配对是y4
（也就是恰好满足y4+x1<=limit），那么容易证明{x1,y1},{x2,y2},{x3,y3},{x4,y4}这四对其实都满足条件（即两个人加起来不超过limit）。
所以我们可以将这四对剥离（因为已经充分利用了资源），对于剩下的人同理进行递归处理就可以了。

于是这道题就转化为了双指针。左右指针朝中间移动，计算有多少对满足people[i]+people[j]<=limit.

这种解法最大的隐患是时间复杂度需要O(NlogN)，勉强可以通过。
"""

class Solution1:
    def numRescueBoats(self, people, limit: int) -> int:
        people.sort()
        i, j = 0, len(people) - 1
        count = 0
        while i <= j:
            # each boat can only accomandate 2 people, one of that person will the the j-th person, and we will see if we wanna bring the i-th person
            if people[i] + people[j] <= limit:
                i += 1
            j -= 1
            count += 1
        return count


class SolutionBucketSort:
    def numRescueBoats(self, people, limit: int) -> int:
        buckets = [0 for i in range(limit + 1)]
        for w in people:
            buckets[w] += 1
        start, end = 0, len(buckets) - 1
        count = 0
        while start <= end:
            while start <= end and buckets[start] <= 0:
                start += 1
            while start <= end and buckets[end] <= 0:
                end -= 1
            if buckets[start] <= 0 and buckets[end] <= 0:
                break
            count += 1
            if start + end <= limit:
                buckets[start] -= 1

            buckets[end] -= 1

        return count





