
"""
1. Put both slots1 and slots2 into PriorityQueue/heapq (first filter slots shorter than duration, sort by starting time;
2. Pop out the slots one by one, comparing every consective two to check if having duration time in common.
"""

import heapq

class Solution:
    def minAvailableDuration(self, slots1, slots2, duration: int):
        heap = list(filter(lambda slot: slot[1] - slot[0] >= duration, slots1 + slots2))
        heapq.heapify(heap)
        while len(heap) > 1:
            if heapq.heappop(heap)[1] >= heap[0][0] + duration:
                return [heap[0][0], heap[0][0] + duration]
        return []


class Solution2:
    def minAvailableDuration(self, slots1, slots2, duration):

        slots1.sort(key=lambda x: x[0])
        slots2.sort(key=lambda x: x[0])
        i, j = 0, 0

        while i < len(slots1) and j < len(slots2):
            head = max(slots1[i][0], slots2[j][0])
            tail = min(slots1[i][1], slots2[j][1])
            if head + duration <= tail:
                return [head, head + duration]

            if slots1[i][1] < slots2[j][1]:
                i += 1
            else:
                j += 1

        return []

