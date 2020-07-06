
import collections

class Solution:
    def leastInterval(self, tasks, n):
        counter = collections.Counter(tasks)
        freq = sorted(counter.values())

        maxi = freq[-1] - 1
        freq.pop()

        idle = maxi * n
        for f in reversed(freq):
            idle -= min(f, maxi)

        if idle > 0:
            return len(tasks) + idle
        else:
            return len(tasks)

        # return len(tasks) + idle if idle > 0 else len(tasks)



class SolutionHeap:
    def leastInterval(self, tasks, n: int) -> int:
        if not tasks:
            return

        count = collections.Counter(tasks)
        heap = [[-freq, char] for char, freq in count.items()]
        heapq.heapify(heap)
        res = 0
        while heap:
            length = min(n+1, len(heap))
            temp = []
            for _ in range(length): #在堆中取任务
                node = heapq.heappop(heap)
                if node[0] != -1:
                    node[0] += 1
                    temp.append(node)
            for node in temp:  #将未执行完的任务放回堆中
                heapq.heappush(heap, node)
            if heap:
                res+=n+1
            else:
                res+=length
        return res

