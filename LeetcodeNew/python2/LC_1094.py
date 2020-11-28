"""
Please see and vote for my solutions for similar problems.
253. Meeting Rooms II
731. My Calendar II
732. My Calendar III
1094. Car Pooling
1109. Corporate Flight Bookings
218. The Skyline Problem

"""

"""
Intuition
Same as 253. Meeting Rooms II.
Track the change of capacity in time order.

Explanation
Save all time points and the change on current capacity
Sort all the changes on the key of time points.
Track the current capacity and return false if negative
Complexity
Time O(NlogN)
Space O(N)
"""

import heapq

class SolutionLee:
    def carPooling(self, trips, capacity):
        for i, v in sorted(x for n, i, j in trips for x in [[i, n], [j, - n]]):
            capacity -= v
            if capacity < 0:
                return False
        return True


class Solution:
    def carPooling(self, trips, capacity: int) -> bool:

        temp = []
        for num, start, end in trips:
            temp.append((start, num))
            temp.append((end, -num))

        temp.sort()
        print(temp)
        count = 0  # num of passenges on car
        for item in temp:
            count += item[1]
            if count > capacity:
                return False

        return True


"""
I used a stack to store all ongoing trip.
Each time I push a new trip to the heap, weighted by ending time, I added that trip's passenger number to load. Once load > capacity, it's false.
And each time, I also popped all terminated trips. Since each trip in the heap is weighted by ending time, 
the minimal trip on heap's top would be the trip with the earliest ending time. 
Thus, I could easily use a while loop to pop all the trip whose ending time is ealier than current trip's starting time, 
and decrease load by terminated trip's passenger number.

def carPooling(trips, capacity):
"""

class Solution2:
    def carPooling(self, trips, capacity: int) -> bool:

        temp = []
        count = 0

        for num, start, end in sorted(trips, key=lambda x: (x[1], x[2], x[0])):
            count += num
            while temp and temp[0][0] <= start:
                count -= heapq.heappop(temp)[1]
            if count > capacity:
                return False
            heapq.heappush(temp, (end, num))
        return True




