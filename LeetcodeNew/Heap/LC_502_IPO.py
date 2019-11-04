
"""
Suppose LeetCode will start its IPO soon. In order to sell a good price of its shares to Venture Capital,
LeetCode would like to work on some projects to increase its capital before the IPO. Since it has limited resources,
it can only finish at most k distinct projects before the IPO.
Help LeetCode design the best way to maximize its total capital after finishing at most k distinct projects.

You are given several projects. For each project i, it has a pure profit Pi
and a minimum capital of Ci is needed to start the corresponding project. Initially, you have W capital.
When you finish a project, you will obtain its pure profit and the profit will be added to your total capital.

To sum up, pick a list of at most k distinct projects from given projects to maximize your final capital,
and output your final maximized capital.

Example 1:
Input: k=2, W=0, Profits=[1,2,3], Capital=[0,1,1].

Output: 4

Explanation: Since your initial capital is 0, you can only start the project indexed 0.
             After finishing it you will obtain profit 1 and your capital becomes 1.
             With capital 1, you can either start the project indexed 1 or the project indexed 2.
             Since you can choose at most 2 projects, you need to finish the project indexed 2 to get the maximum capital.
             Therefore, output the final maximized capital, which is 0 + 1 + 3 = 4.

"""

"""
Loop k times:
Add all possible projects (Capital <= W) into the priority queue with the priority = -Profit.
Get the project with the smallest priority (biggest Profit).
Add the Profit to W
"""
import heapq
class SolutionLee:
    def findMaximizedCapital(self, k, W, Profits, Capital):
        heap = []
        projects = sorted(zip(Profits, Capital), key=lambda l: l[1])
        i = 0
        for _ in range(k):
            while i < len(projects) and projects[i][1] <= W:
                heapq.heappush(heap, -projects[i][0])
                i += 1
            if heap: W -= heapq.heappop(heap)
        return W



class SolutionRefactor:
    def findMaximizedCapital(self, k, W, Profits, Capital):
        projects = sorted(zip(Profits,Capital), key = lambda project : project[1])
        heap     = []
        project = 0
        while k:
            while project < len(projects) and projects[project][1] <= W:
                heapq.heappush(heap,-projects[project][0])
                project += 1
            if heap:
                W -= heapq.heappop(heap)
            k -= 1
        return W


"""
Basic idea: Find and do the most profitable job available K times.

First, Capital and Profit are zipped into tuples, 
then sorted in ascending order to create a stack where the top elements require less capital.

Then, available jobs are popped off the stack, its profit pushed onto a maxheap with most profitable jobs on top.

Finally, the most profitable job available gets popped and current capital gets updated.

This process is done K times.

Since Python does not explicitly support maxheaps, the profits are negated and pushed onto a minheap/priority queue. 
Encapsulating each profit into a tuple yields a speed boost over naked Integers.

"""

class SolutionStefan:
    def findMaximizedCapital(self, k, W, Profits, Capital):
        current = []
        future = sorted(zip(Capital, Profits))[::-1]
        for _ in range(k):
            while future and future[-1][0] <= W:
                heapq.heappush(current, -future.pop()[1])
            if current:
                W -= heapq.heappop(current)
        return W


class SolutionRefactor:
    def findMaximizedCapital(self, k, W, Profits, Capital):
        projects = sorted(zip(Profits,Capital), key = lambda project : project[1])
        heap     = []
        project = 0
        while k:
            while project < len(projects) and projects[project][1] <= W:
                heapq.heappush(heap,-projects[project][0])
                project += 1
            if heap:
                W -= heapq.heappop(heap)
            k -= 1
        return W
#
# def find(worst, expected):
#     projects = sorted(zip(worst, expected), key=lambda project: project[1])
#     print(projects)
#
#     W = max([i[0] for i in projects])
#     print([i[0] for i in projects])
#     res = W
#     # print(W, res)
#     for i, project in enumerate(projects):
#         if W >= project[0]:
#             W -= project[1]
#         else:
#             res += abs(W - project[0])
#     # print(W, res)
#     # print(res)
#     return res
#
#
# find([6,5,7, 8], [4,2,1, 1])


import bisect
def test(a, b):
    res = 2
    dp = [1, 2]
    diff = a[1] - a[0]
    for i in range(2, len(a)):
        if a[i] - a[i-1] == diff:
            dp.append(dp[-1] + 1)
        else:
            next = bisect.bisect_right(b, a[i], 0, len(b))
            if b[next] - a[i-1] == diff:
                dp.append(dp[-1] + 1)
            else:
                diff = a[i] - a[i-1]
                dp.append(1)
    print(dp)

    return max([i for i in dp])


a = [1,2,3,5,6,67]
b = [6,7]

print(test(a, b))











