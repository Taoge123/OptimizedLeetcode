
"""
[1,2,3,4]
rain[i] = 0 -> 抽水日
    dryDay.insert(i)
rain[i] = x
1) x is empty: fill[x] = i
2) x is full: when to drain x?
    must be in dryDays
    must be later than fill[x]

      1  2  3  4  5  6
fill  x     y     x
dryD     -     x

1488.Avoid-Flood-in-The-City
我们来分析一下贪心的策略会是什么。

我们如果在第i天遇到一个晴天，那么我们肯定会利用它来抽干某个湖。但是抽干哪个湖最合算呢？其实我们这时候是不确定的。如果某个湖在以后的日子里再也不会被下雨，那么我们在当前的晴天取抽水，并没有任何意义。所以我们只有在日后某个雨天时发现，某个湖已经充满、但是又要被下雨的时候，才会“回溯性”地决策在之前的某个晴天提前把这个湖抽干。因此，在晴天的时候，我们暂时不会做任何事情，只是默默把当前的日子加入一个集合dryDays。以后发现需要确定抽水日的时候，就从里面选。

我们如果在第i天遇到要对湖x下雨，我们必然会查看这个湖是否已经充满。

如果尚未充满，我们就标记为充满fill[x]=i，但不着急做任何抽水的规划。
如果湖x已经充满了，为了避免泛滥，我们一定要在第i天之前提前把湖x抽干。那么是哪一天最合适呢？首先，这一天一定是dryDays的集合中；其次一定要在fill[x]之后做（因为只有先充满了才能去抽干）。那么是否满足这两个条件的任意一天都可以呢？其实我们还希望越早越好。举个例子：
fillDays:     x       y       x   y
dryDays:          _       _
第8天的时候湖x可能会泛滥，所以我们必须在第5天或者第7天的时候把湖x抽干。但是如果我们选择在第7天取抽干湖x的话，当第9天y要泛滥的时候，我们就没有dry day去抽干湖y了。这就说明了，要抽干得趁早。在敲定了第5天抽干湖x之后，就把dryDays里去掉这一天。同时要更新fill[x]=8,即当天的下雨日。
"""

import bisect

class Solution:
    def avoidFlood(self, rains):
        filled = {}
        dryDays = []
        res = [1] * len(rains)
        for day, lake in enumerate(rains):
            if not lake:
                dryDays.append(day)
            else:
                res[day] = -1
                if lake in filled:
                    if not dryDays:
                        return []
                    # use the first dry day after the lake was filled (stored in filled[lake])
                    idx = bisect.bisect_left(dryDays, filled[lake])
                    if idx >= len(dryDays):
                        return []
                    dry_on_day = dryDays.pop(idx)
                    res[dry_on_day] = lake

                filled[lake] = day # we fill it on day

        return res


