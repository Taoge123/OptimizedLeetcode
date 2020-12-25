import heapq

class Solution:
    def maxEvents(self, events) -> int:
        # sort events by start date
        events.sort()
        heap = []
        i = 0
        count = 0
        min_day = events[0][0]
        max_day = max(x[1] for x in events)

        for day in range(min_day, max_day + 1):
            # add events priortized by earliest end date
            while i < len(events) and events[i][0] <= day:
                heapq.heappush(heap, events[i][1])
                i += 1

            # discard past events since we can't attend them anymore.
            while heap and heap[0] < day:
                heapq.heappop(heap)

            # attend an event with earliest end date
            if heap:
                heapq.heappop(heap)
                count += 1

        return count

