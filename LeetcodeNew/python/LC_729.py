"""
Implement a MyCalendar class to store your events. A new event can be added if adding the event will not cause a double booking.

Your class will have the method, book(int start, int end). Formally, this represents a booking on the half open interval [start, end), the range of real numbers x such that start <= x < end.

A double booking happens when two events have some non-empty intersection (ie., there is some time that is common to both events.)

For each call to the method MyCalendar.book, return true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.

Your class will be called like this: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)
Example 1:

MyCalendar();
MyCalendar.book(10, 20); // returns true
MyCalendar.book(15, 25); // returns false
MyCalendar.book(20, 30); // returns true
Explanation:
The first event can be booked.  The second can't because time 15 is already booked by another event.
The third event can be booked, as the first event takes every time less than 20, but not including 20.


Note:

The number of calls to MyCalendar.book per test case will be at most 1000.
In calls to MyCalendar.book(start, end), start and end are integers in the range [0, 10^9].

"""


import bisect

class Node:
    def __init__(self, s, e):
        self.e = e
        self.s = s
        self.left = None
        self.right = None


class MyCalendarCs:
    def __init__(self):
        self.calender = []

    def book(self, start: int, end: int) -> bool:
        for event in self.calender:
            if event[0] < end and start < event[1]:
                return False

        self.calender.append([start, end])
        return True


class MyCalendar:

    def __init__(self):
        self.root = Node(0, 0)

    def book(self, start, end):
        return self.helper(start, end, self.root)

    def helper(self, start, end, node):
        if start >= node.e:
            if not node.right:
                node.right = Node(start, end)
                return True
            return self.helper(start, end, node.right)
        elif end <= node.s:
            if not node.left:
                node.left = Node(start, end)
                return True
            return self.helper(start, end, node.left)
        return False


#This is exactly my thought, first binary search to find the index (first num greater than start
# if the start less than previous num's end, violation
# if the end greater than later num's start, violation)
class MyCalendar2:
    def __init__(self):
        self.starts = []
        self.ends = []

    def book(self, start, end):
        i = bisect.bisect_left(self.starts, start)
        if i - 1 >= 0:
            if start < self.ends[i - 1]:
                return False
        if i < len(self.starts):
            if end > self.starts[i]:
                return False

        self.starts.insert(i, start)
        self.ends.insert(i, end)
        return True


"""
[10, 20], [15, 25], [20, 30]
starts = [10]
ends   = [20]

"""
a = MyCalendar2()
print(a.book(10, 20))
print(a.book(15, 25))
print(a.book(20, 30))


