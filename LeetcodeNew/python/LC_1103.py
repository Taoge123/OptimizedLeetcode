"""
Intuition
Brute force of simulation seems to be easy.
But how is the time complexity?


Explanation
The i-th distribution,
we will distribute i + 1 candies to (i % n)th people.
We just simulate the process of distribution until we ran out of candies.

Complexity
Time O(sqrt(candies))
Space O(N) for result

The number of given candies is i + 1, which is an increasing sequence.
The total number distributed candies is c * (c + 1) / 2 until it's bigger than candies.
So the time it takes is O(sqrt(candies))
"""


class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:

        cur = 1
        res = [0] * num_people
        i = 0
        while candies:
            if candies >= cur:
                candies -= cur
                res[i] += cur
                cur += 1
                i = (i + 1) % num_people
            else:
                res[i] += candies
                candies = 0
        return res


class SolutionLee:
    def distributeCandies(self, candies, n):
        res = [0] * n
        i = 0
        while candies > 0:
            res[i % n] += min(candies, i + 1)
            candies -= i + 1
            i += 1
        return res

