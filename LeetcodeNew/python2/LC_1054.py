"""
identical toi 767 - Reorganize String

"""

import collections
import heapq


class Solution:
    def rearrangeBarcodes(self, barcodes):
        freq = collections.Counter(barcodes)
        heap = [[-count, num] for num, count in freq.items()]
        heapq.heapify(heap)
        res = []

        while len(heap) >= 2:
            count1, num1 = heapq.heappop(heap)
            count2, num2 = heapq.heappop(heap)

            res.append(num1)
            res.append(num2)

            if count1 < -1:
                heapq.heappush(heap, [count1 + 1, num1])

            if count2 < -1:
                heapq.heappush(heap, [count2 + 1, num2])

        if len(heap) == 0:
            return res
        else:
            count, num = heapq.heappop(heap)
            if count < -1:
                return []
            else:
                return res + [num]



class SolutionLee:
    def rearrangeBarcodes(self, packages):
        i = 0
        n = len(packages)
        res = [0] * n
        print(collections.Counter(packages).most_common())
        for k, val in collections.Counter(packages).most_common():
            for _ in range(val):
                res[i] = k
                i += 2
                if i >= n:
                    i = 1
        return res





class Solution2:
    def rearrangeBarcodes(self, code):
        heap = []
        count = collections.Counter(code)
        for k,v in count.items():
            heapq.heappush(heap, (-v, k))

        pre_val, pre_count = -1, 0
        res = []
        while heap:
            # get the value with largest frequency
            count, key = heapq.heappop(heap)
            count = -count
            res.append(key)
            # add previous value and count
            if pre_count > 0:
                heapq.heappush(heap, (-pre_count, pre_val))

            count -= 1
            pre_val, pre_count = key, count
        return res



packages = [1,1,1,1,2,2,3,3]
a = Solution()
print(a.rearrangeBarcodes(packages))

