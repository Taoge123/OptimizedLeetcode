# """
# 题目要找天际线的关键点，首先从左至右把可能出现关键点的位置扫描一遍，然后判断每个位置是否有关键点，
# 并且确定关键点的具体坐标（也就是其高度）。
# 通过画图画出大部分可能的重叠情况，我们可以发现，所有的关键点可以分为两类：进入点和离开点。对于进入点来说，
# 如果此刻进入的这栋楼是最高的，那他的起点就是一个关键点；如果他不是最高的，或者跟当前最高的楼一样高，说明该进入点被覆盖了，
# 不需要添加关键点。对于离开点来说，如果他是最高的楼，那他的离开，一定会导致原本比他更低一点的楼露出，
# 因此对应的关键点高度就是比他更低一点的楼的高度；如果他不是最高的，那他的离开就对天际线没有影响，因此不需要更新。
# 在代码实现时，首先我们需要把“进入点”和“离开点”都加入到一个队列中，并按照从左往右的顺序开始排序。这里的构思十分巧妙。
# 首先考虑进入点，对于每栋楼的坐标(L,R,H)来说，我们先按照左下标来排序，即key为L。但是当两栋楼的左下标一样时，
# 我们应该优先考虑更高的那栋楼。因此key为(L,-H)。然后再考虑离开点，离开点的右下标可以同样作为L与进入点一起排序，
# 设想一种边界情况：当某个位置同时出现多栋楼的离开点和进入点时，此处是否有关键点以及相应关键点的高度取决于此时仍然存在的楼的高度，
# 以及刚好出现的楼的高度，也就是说，进入点必须比离开点先考虑，而离开点之间的先后顺序并无影响，
# 因为每栋楼的离开点所在的关键点不会由这栋楼的高度影响，另外一种情况是，如果某个位置只有离开点，没有进入点，
# 且没有任何还存在的楼，那(R,0)也需要加入的集合里。为了区分进入点和离开点，我们把进入点表达为(L,-H,R)，
# 把离开点表达为(R,0,None)，因此只有进入点的元组中有三个存在的数值。然后按照tuple[0]和tuple[1]来排序，
# 以保证上述边界情况下，考虑点的优先顺序都是正确的。
# 接下来就是要遍历排序后的所有候选点。首先我们需要一个有序的数据结构，能够维护当前最高的一栋楼的高度和位置信息，这里的构思也非常巧妙。
# 为什么需要知道当前最高楼的高度？因为天际线一定是当前所有楼层最高的那条，如果在遍历过程中，当前的天际线与目前最高楼的高度不一样，
# 说明发生了两种情况之一：一种是出现了一栋更高的楼，此时一定是经过了一个新的进入点，所以此时要加入一个新的天际线关键点，
# 其高度就是当前最高楼的高度；另一种情况是，最高楼的高度变低了，说明一定是经过了一个离开点，有一栋最高楼在刚才离开了，
# 天际线发生了变化，因此也要加入一个新的天际线关键点，其高度就是刚才最高楼离开之后，剩下楼层里最高的高度。
# 如果目前已经没有任何大楼，说明到达了最低点。因此我们在初始化这个有序的结构时，需要加一个高度为0，横坐标位置无限大的点，
# 用来完成这种“特殊情况”。总结来说，就是只要当前维护的最大楼高度不等于上一个添加的天际线关键点的高度，
# 就需要增加一个新的关键点了。另外一个边界情况是，当目前还没有任何天际线时，我们如何判断当前最大楼高是否发生了变化呢？
# 也就是在我们遍历第一栋楼时，我们应该直接加入这个进入点，因为这个进入点一定高于地平线，地平线就是上一个“天际线”。
# 所以我们需要在初始化最终集合的时候，加入一个高度为0的元素，来解决这个问题。当然在最后返回的时候，还需要扔掉这个元素。
# 除此之外也可以通过增加if逻辑来应对这种情况。
# 最后一个问题是，我们用什么数据结构来维护当前的最高楼层，以及如何在遍历过程中进行更新。首先我们思考一下，需要进行哪些操作：
# 取出当前最大的楼层高度；删除已经离开的楼层高度；增加刚进入的楼层高度。何时需要增加楼层高度？当此时的点是进入点时。
# 何时需要删除已经离开点楼层高度？当此时遍历的点已经超过了楼层的最右位置时。也就是说，我们需要存的数据，
# 应该包含了楼的高度和最右位置。总结一下就是：每次当我们遍历到进入点时，把对应的楼高和右下标加入到这个有序结构中；
# 每次当我们遍历到的点的位置已经超过或者等于当前最高楼的右下标时，说明这栋楼已经失效（为什么等于也不行：
# 因为最开始分析过，楼的离开对这栋楼所构成的天际线是没有影响的，可以看作是左闭右开的区间），这个操作需要一直执行，
# 直到当前的最高楼仍然在范围内为止。总结到这里，我们就可以开始选择合适的数据结构。如何能够快速的维护最大值、
# 删除最大值以及增加一个新的元素？答案就是堆。python中heapq库可以方便地维护一个有序的list，
# 通过heappop和heappush可以方便地增删元素。取最大值则只需要通过获取第一个元素（注意heapq默认是升序排列，
# 因此我们仍存储-H来实现降序）。
# """
# """
#
# Use an infinite vertical line x to scan from left to right. If max height changes,
# record [x, height] in res. Online judge is using Python 2.7.9 and there's no max heap's push and pop method,
# so we can use a min heap hp storing -H as "max heap".
# Thanks to this discussion, set comprehension is faster and shorter than list(set((R, 0, None) for L, R, H in buildings))
#
# """
# from heapq import *
#
# class Solution:
#     def getSkyline(self, buildings):
#         skyline = []
#         i, n = 0, len(buildings)
#         liveHR = []
#         while i < n or liveHR:
#             if not liveHR or i < n and buildings[i][0] <= -liveHR[0][1]:
#                 x = buildings[i][0]
#                 while i < n and buildings[i][0] == x:
#                     heappush(liveHR, (-buildings[i][2], -buildings[i][1]))
#                     i += 1
#             else:
#                 x = -liveHR[0][1]
#                 while liveHR and -liveHR[0][1] <= x:
#                     heappop(liveHR)
#             height = len(liveHR) and -liveHR[0][0]
#             if not skyline or height != skyline[-1][1]:
#                 skyline += [x, height],
#         return skyline
#
#
# from heapq import heappush, heappop
# import heapq
#
#
# class Solution1:
#     def getSkyline(self, buildings):
#         # add start-building events
#         # also add end-building events(acts as buildings with 0 height)
#         # and sort the events in left -> right order
#         events = [(L, -H, R) for L, R, H in buildings]
#         events += list({(R, 0, 0) for _, R, _ in buildings})
#         events.sort()
#
#         # res: result, [x, height]
#         # live: heap, [-height, ending position]
#         res = [[0, 0]]
#         live = [(0, float("inf"))]
#         for pos, negH, R in events:
#             # 1, pop buildings that are already ended
#             # 2, if it's the start-building event, make the building alive
#             # 3, if previous keypoint height != current highest height, edit the result
#             while live[0][1] <= pos:
#                 heappop(live)
#             if negH:
#                 heappush(live, (negH, R))
#             if res[-1][1] != -live[0][0]:
#                 res += [ [pos, -live[0][0]] ]
#         return res[1:]
#
#
# class Solution2:
#     def getSkyline(self, buildings):
#         # 对于一个 building, 他由 (l, r, h) 三元组组成, 我们可以将其分解为两种事件:
#         #     1. 在 left position, 高度从 0 增加到 h(并且这个高度将持续到 right position);
#         #     2. 在 right position, 高度从 h 降低到 0.
#         # 由此引出了 event 的结构: 在某一个 position p, 它引入了一个高度为 h 的 skyline, 将一直持续到另一 end postion
#
#         # 对于在 right position 高度降为 0 的 event, 它的持续长度时无效的
#         # 只保留一个 right position event, 就可以同时触发不同的两个 building 在同一 right position 从各自的 h 降为 0 的 event, 所以对 right
#         # position events 做集合操作会减少计算量
#
#         # 由于需要从左到右触发 event, 所以按 postion 对 events 进行排序
#         # 并且, 对于同一 positon, 我们需要先触发更高 h 的事件, 先触发更高 h 的事件后, 那么高的 h 相比于低的 h 会占据更高的 skyline, 低 h 的 `key point` 就一定不会产生;
#         # 相反, 可能会从低到高连续产生冗余的 `key point`
#         # 所以, event 不仅需要按第一个元素 position 排序, 在 position 相同时, 第二个元素 h 也是必须有序的
#         events = sorted([(l, -h, r) for l, r, h in buildings] + list({(r, 0, 0) for l, r, h in buildings}))
#
#         # res 记录了 `key point` 的结果: [x, h]
#         # 同时 res[-1] 处的 `key point` 代表了在下一个 event 触发之前, 一直保持的最高的 skyline
#
#         # hp 记录了对于一条高为 h 的 skyline, 他将持续到什么 position 才结束: [h, endposition]
#         # 在同时有多条 skyline 的时候, h 最高的那条 skyline 会掩盖 h 低的 skyline, 因此在 event 触发时, 需要得到当前最高的 skyline
#         # 所以利用 heap 结构存储 hp, 它的第一个值永远为列表中的最小值: 因此在 event 中记录的是 -h, heap 结构就会返回最高的 skyline. 同时, h 必须在 endposition 之前,
#         # 因为它按第一个元素排序
#         res, record = [[0, 0]], [(0, float('inf'))]
#
#         for l, neg_h, r in events:
#             # 触发 event 时, 首先要做的就是清除已经到 endposition 的 skyline
#             # hp: [h, endposition]
#             # 如果当前 position 大于等于了 hp 中的 endposition, 那么该 skyline 会被清除掉
#             # 由于在有 high skyline 的情况下, low skyline 不会有影响,
#             # 因此, 只需要按从高到低的方式清除 skyline, 直到剩下一个最高的 skyline 并且它的
#             # endposition 大于当前 position
#             while l >= record[0][1]:
#                 heapq.heappop(record)
#
#             # 对于高度增加到 h 的时间(neg_h < 0), 我们需要添加一个 skyline, 他将持续到 r 即 endposition
#             if neg_h:
#                 heapq.heappush(record, (neg_h, r))
#
#             # 由于 res[-1][1] 记录了在当前事件触发之前一直保持的 skyline
#             # 如果当前事件触发后 skyline 发生了改变
#             #     1. 来了一条新的高度大于 h 的 skyline
#             #     2. res[-1] 中记录的 skyline 到达了 endposition
#             # 这两种事件都会导致刚才持续的 skyline 与现在最高的 skyline 不同; 同时, `key point` 产生了, 他将被记录在 res 中
#             if res[-1][1] != -record[0][0]:
#                 res.append([l, -record[0][0]])
#
#         return res[1:]
#
#
#
# class SolutionTest:
#     def getSkyline(self, buildings):
#
#         events = [(L, -H, R) for L, R, H in buildings]
#         events += list({(R, 0, 0) for _, R, _ in buildings})
#         events.sort()
#         res = [[0, 0]]
#         record = [(0, float("inf"))]
#         for pos, negH, R in events:
#             while record[0][1] <= pos:
#                 heappop(record)
#             if negH:
#                 heappush(record, (negH, R))
#             if res[-1][1] != -record[0][0]:
#                 res += [[pos, -record[0][0]] ]
#         return res[1:]
#
#
#
# # buildings = [[0,1,2],[1,2,3],[2,3,4],[3,4,3],[4,6,2],[5,7,3]]
# buildings = [[0,2,1],[1,6,2],[3,4,3],[5,7,1]]
#
#
# a = SolutionTest()
# print(a.getSkyline(buildings))
#
#
#
#
#
# import bisect
# import collections
#

class TweetCounts:
    def __init__(self):
        self.count = collections.defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        bisect.insort_left(self.count[tweetName], time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int):
        endTime += 1
        if freq == 'minute':
            bucket = 60
        elif freq == 'hour':
            bucket = 3600
        elif freq == 'day':
            bucket = 3600 * 24
        res = []
        temp = self.count[tweetName]
        left = bisect.bisect_left(temp, startTime)
        nextTimeTemp = bisect.bisect_right(temp, endTime)

        for i in range(bucket+1):
            if (left + i) % bucket == 0:
                nextTime = left + i - 1
        nextt = min(endTime, nextTime)
        right = min(bisect.bisect_right(temp, nextTime), nextTimeTemp)
        n = endTime
        leftCor, rightCor = startTime, nextt
        while n > 0:
            res.append(right - left)
            leftCor = leftCor + bucket
            rightCor = rightCor + bucket
            n -= bucket
            left = bisect.bisect_left(temp, leftCor)
            right = bisect.bisect_right(temp, rightCor)

        return res

#
# # tweetCounts = TweetCounts()
# # print(tweetCounts.recordTweet("tweet3", 0))
# # print(tweetCounts.recordTweet("tweet3", 60))
# # print(tweetCounts.recordTweet("tweet3", 10))
# # print(tweetCounts.getTweetCountsPerFrequency("minute", "tweet3", 0, 61))
# # print(tweetCounts.recordTweet("tweet3", 120))
# # print(tweetCounts.getTweetCountsPerFrequency("hour", "tweet3", 0, 210))
# #
#
#
# tweetCounts = TweetCounts()
# print(tweetCounts.recordTweet("tweet3", 0))
# print(tweetCounts.recordTweet("tweet3", 10))
# print(tweetCounts.recordTweet("tweet3", 20))
# print(tweetCounts.recordTweet("tweet3", 30))
# print(tweetCounts.recordTweet("tweet3", 40))
# print(tweetCounts.recordTweet("tweet3", 50))
# print(tweetCounts.recordTweet("tweet3", 55))
# # print(tweetCounts.getTweetCountsPerFrequency("minute", "tweet3", 0, 30))
# # print(tweetCounts.getTweetCountsPerFrequency("minute", "tweet3", 0, 120))
# print(tweetCounts.recordTweet("tweet3", 120))
# print(tweetCounts.recordTweet("tweet3", 130))
# print(tweetCounts.recordTweet("tweet3", 140))
# print(tweetCounts.recordTweet("tweet3", 170))
# print(tweetCounts.recordTweet("tweet3", 190))
# print(tweetCounts.getTweetCountsPerFrequency("minute", "tweet3", 0, 210))
#
import collections

class Solution:
    def maxStudents(self, seats) -> int:
        self.res = 0
        m, n = len(seats), len(seats[0])
        visited = {}
        for i in range(m):
            for j in range(n):
                temp = self.helper(seats, i, j, 0, m, n, visited)
                if temp:
                    self.res = max(self.res, temp)

        return self.res

    def helper(self, seats, i, j, count, m, n, visited):
        if i < 0 or j < 0 or i >= m or j >= n or seats[i][j] == '#' or visited.get((i, j)):
            return
        visited[(i, j)] = True
        count += 1
        self.res = max(self.res, count)

        self.helper(seats, i - 1, j, count, m, n, visited)
        self.helper(seats, i + 1, j, count, m, n, visited)
        self.helper(seats, i, j - 2, count, m, n, visited)
        self.helper(seats, i, j + 2, count, m, n, visited)
        visited[(i, j)] = False
        return count



seats = [["#",".","#","#",".","#"],
         [".","#","#","#","#","."],
         ["#",".","#","#",".","#"]]

a = Solution()
print(a.maxStudents(seats))



