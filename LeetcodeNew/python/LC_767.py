import collections
import heapq


class Solution:
    def reorganizeString(self, S):
        if not S:
            return ''

        freq = collections.Counter(S)
        heap = [[-count, char] for char, count in freq.items()]
        heapq.heapify(heap)
        res = ''

        while len(heap) >= 2:
            count1, char1 = heapq.heappop(heap)
            count2, char2 = heapq.heappop(heap)

            res += char1 + char2
            if count1 < -1:
                heapq.heappush(heap, [count1 + 1, char1])

            if count2 < -1:
                heapq.heappush(heap, [count2 + 1, char2])

        if len(heap) == 0:
            return res
        else:
            count, char = heapq.heappop(heap)
            if count < -1:
                return ''
            else:
                return res + char






