"""
370 Range Addition

Set the change of seats for each day.
If booking = [i, j, k],
it needs k more seat on ith day,
and we don't need these seats on j+1th day.
We accumulate these changes then we have the result that we want.


"""

class Solution:
    def corpFlightBookings(self, bookings, n):
        res = [0] * (n + 1)
        for i, j, val in bookings:
            res[i - 1] += val
            res[j] -= val
        for i in range(1, n):
            res[i] += res[i - 1]
        return res[:-1]


