"""
From the beginning I used a Map<Integer, Set<Integer>> to represent reserved seats as a graph.
But then I realized that we can use a bit vector instead of Set<Integer>.

Also, seats 2,3,4,5 can be represented as (1 << 2) | (1 << 3) | (1 << 4) | (1 << 5) = 60, for example.
So, I use this value to check whether the seats 2,3,4,5 are available when traversing the graph (togather with 6,7,8,9 and 4,5,6,7).

I want to add some explanations for the last line max + 2 * (n - graph.size()). We don't necessarily have reserved seats for each row. If we don't have any reserved seats in that particular row, we can maximum possibly allocate 2 families with a group of 4 people each. For example, there are seats we can allocate for these two families with seats 2, 3, 4, 5 and seats 6, 7, 8, 9, seat 1 and seat 10 dose not matter.

From the code, max means the maximum allocations we can do for the rows with reserved seats. After that, we also need to count the rows won't have any reserved seats. The graph.size() contains all rows which have seats reserved. n - graph.size() contains all rows don't have any seats reserved, and we can allocate 2 families with a group of 4 people each, so 2 * (n - graph.size()) is the total number of allocations we can do for rows don't have any seats reserved.

Finally, we have maximum number of allocations:
Maximum Allocations = Total number allocations for rows with reserved seats + Total number allocations for rows don't have any reserved seats
= max + 2 * (n - graph.size()).

"""


import collections

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats) -> int:
        graph = collections.defaultdict(int)
        for row, col in reservedSeats:
            graph[row] |= (1 << col)

        maxi = 0
        for row in graph.keys():
            reserved = graph[row]
            count = 0
            # check if seats 2,3,4,5 are available
            if reserved & 60 == 0:
                count += 1
            # check if seats 6,7,8,9 are available
            if reserved & 960 == 0:
                count += 1

            # check if seats 4,5,6,7 are available
            if reserved & 240 == 0 and count == 0:
                count = 1

            maxi += count

        return maxi + 2 * (n - len(graph))



"""
Intuition
If there are not any reserved seats, the answer should be 2n. Then we investigate the reserved seats and group them on a row basis. In this way, we subtract the seats that are not suitable for a four-person family.
"""

class Solution2:
    def maxNumberOfFamilies(self, n, reservedSeats):
        res = 2 * n
        table = collections.defaultdict(set)
        for row, seat in reservedSeats:
            table[row].add(seat)

        for x in table:
            count = 0
            if 2 not in table[x] and 3 not in table[x] and 4 not in table[x] and 5 not in table[x]:
                count += 1
            if 6 not in table[x] and 7 not in table[x] and 8 not in table[x] and 9 not in table[x]:
                count += 1
            if 4 not in table[x] and 5 not in table[x] and 6 not in table[x] and 7 not in table[x] and count == 0:
                count += 1
            res += (count - 2)
        return res


