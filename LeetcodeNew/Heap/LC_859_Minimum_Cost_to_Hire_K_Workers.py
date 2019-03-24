
"""
https://leetcode.com/problems/minimum-cost-to-hire-k-workers/discuss/141768/Detailed-explanation-O(NlogN)
https://leetcode.com/problems/minimum-cost-to-hire-k-workers/discuss/177269/N-log-N-explanation-no-code
https://leetcode.com/problems/minimum-cost-to-hire-k-workers/discuss/241443/Detailed-proof-%2B-explanation-for-this-question.-Hand-writing.

https://leetcode.com/problems/minimum-cost-to-hire-k-workers/discuss/141802/python

There are N workers.  The i-th worker has a quality[i] and a minimum wage expectation wage[i].

Now we want to hire exactly K workers to form a paid group.
When hiring a group of K workers, we must pay them according to the following rules:

1. Every worker in the paid group should be paid in the ratio of their quality compared to other workers in the paid group.
2. Every worker in the paid group must be paid at least their minimum wage expectation.
Return the least amount of money needed to form a paid group satisfying the above conditions.



Example 1:

Input: quality = [10,20,5], wage = [70,50,30], K = 2
Output: 105.00000
Explanation: We pay 70 to 0-th worker and 35 to 2-th worker.
Example 2:

Input: quality = [3,1,10,10,1], wage = [4,8,2,2,7], K = 3
Output: 30.66667
Explanation: We pay 4 to 0-th worker, 13.33333 to 2-th and 3-th workers seperately.
"""

"""
Let's read description first and figure out the two rules:

"1. Every worker in the paid group should be paid 
in the ratio of their quality compared to other workers in the paid group."

So for any two workers in the paid group,
we have wage[i] : wage[j] = quality[i] : quality[j]
So we have wage[i] : quality[i] = wage[j] : quality[j]
We pay wage to every worker in the group with the same ratio compared to his own quality.

"2. Every worker in the paid group must be paid at least their minimum wage expectation."
For every worker, he has an expected ratio of wage compared to his quality.

So to minimize the total wage, we want a small ratio.
So we sort all workers with their expected ratio, and pick up K first worker.
Now we have a minimum possible ratio for K worker and we their total quality.

As we pick up next worker with bigger ratio, we increase the ratio for whole group.
Meanwhile we remove a worker with highest quality so that we keep K workers in the group.
We calculate the current ratio * total quality = total wage for this group.

We redo the process and we can find the minimum total wage.
Because workers are sorted by ratio of wage/quality.
For every ratio, we find the minimum possible total quality of K workers.

Time Complexity
O(NlogN) for sort.
O(NlogK) for priority queue.
"""

import heapq

class SolutionLee:
    def mincostToHireWorkers(self, quality, wage, K):
        workers = sorted([float(w) / q, q] for w, q in zip(wage, quality))
        res = float('inf')
        qsum = 0
        heap = []
        for r, q in workers:
            heapq.heappush(heap, -q)
            qsum += q
            if len(heap) > K:
                qsum += heapq.heappop(heap)
            if len(heap) == K:
                res = min(res, qsum * r)
        return res

"""
分析：
1. 这道题有点意思，要雇佣K个人，使得所花钱最少，雇佣需满足两个条件，一是最后给的钱必须成比例，二是不能低于最小值
2. 我们不妨设最后雇佣时给第i个人的钱为p[i]，则对于被选上的K个人来说，都有相同的比例 p[i] / quality[i]（根据条件1）
3. 也就是说一旦我们选定了比例 r，那么最后选的K个人一定都满足 r * quality[i] > wage[i]（因为已经被选上了自然满足条件2）
4. 上式逆推为 r > (wage/quality),故我们将所有人按照 wage/quality 的大小排序，依次作为r 来判断最后的总价格。
5. 注意N,K都达到了10000，O(n^2)的方法显然不行（绝大部分情况下）
"""
"""
思路：
按照wage/quality排序，若选定第i个人的比例r作为标准，那么还需从0到i-1中的人选k-1个人
对于0到i-1个人，他们每个人的价格就是quality*r，r是固定的，所以quality越小越好，
所以我们用最大堆将quality大的丢弃
"""


class Solution2:
    def mincostToHireWorkers(self, quality, wage, K):

        # 按比例排序,nlogn
        workers = sorted([float(wage[i])/quality[i], quality[i]] for i in range(len(quality)))
        res,qsum = float('inf'),0
        heap = []

        for i in range(len(workers)):
            # 选定比例 r
            r,q = workers[i]
            heapq.heappush(heap,-q)
            # qsum始终记录k个人的quality之和，乘以r即为最后结果
            qsum += q
            if len(heap) > K:
                # 始终丢弃quality最大的人
                qsum += heapq.heappop(heap)
            if len(heap) == K:
                res = min(res, qsum * r)
        return res

