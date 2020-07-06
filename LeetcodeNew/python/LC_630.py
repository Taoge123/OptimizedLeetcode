"""
We start learning courses with earliest closing date first. If we find a course that can't fit into its close date,
we can un-learn one of the previous course in order to fit it in.
We can safely un-learn a previous course because it closes earlier and there is no way for it to be picked up again later.
We pick up the one with longest learning time to un-learn, if the longest learning time happend to be the newly added course,
then it is equivalent to not learning the newly added course.

"""

import heapq

class Solution:
    def scheduleCourse(self, courses) -> int:
        heap = []
        nums = sorted(courses, key=lambda x: x[1])

        day = 0
        for time, end in nums:
            day += time
            heapq.heappush(heap, -time)
            while day > end:
                day += heapq.heappop(heap)

        return len(heap)



