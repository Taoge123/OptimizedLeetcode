"""
We store an array self.overlaps of intervals that are double booked, and self.calendar for intervals which have been single booked.
We use the line start < j and end > i to check if the ranges [start, end) and [i, j) overlap.

The clever idea is we do not need to "clean up" ranges in calendar: if we have [1, 3] and [2, 4],
this will be calendar = [[1,3],[2,4]] and overlaps = [[2,3]].
We don't need to spend time transforming the calendar to calendar = [[1,4]].

"""
"""
--------
    --------
        --------
            --------
            
[1, 3], [2, 4], [3, 5]. [4, 6]
calendar = [1, 3] [2, 4]
overlaps = [2, 3]

"""



class MyCalendarTwo:
    def __init__(self):
        # doubel booked
        self.overlaps = []
        # single booked
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        for i, j in self.overlaps:
            if start < j and end > i:
                return False

        for i, j in self.calendar:
            if start < j and end > i:
                self.overlaps.append((max(start, i), min(end, j)))
        self.calendar.append((start, end))
        return True




