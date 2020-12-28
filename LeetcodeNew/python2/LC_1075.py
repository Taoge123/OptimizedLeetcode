import heapq


class Solution:
    def eatenApples(self, apples, days) -> int:
        heap = []
        res = 0
        n = len(apples)
        # maximum date to eat
        for i in range(n + max(days)):
            # when we have apples to store.
            if i< n and apples[i]:
                heapq.heappush(heap, [i + days[i], apples[i]])
            if heap:
                heap[0][1] -= 1
                res += 1
            # pop rotten apple at next day or clear empty apple
            while heap and (heap[0][0] <= i + 1 or heap[0][1] == 0):
                heapq.heappop(heap)
        return res


