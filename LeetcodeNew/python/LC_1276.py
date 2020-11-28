"""
Intuition
Classic problem, https://w.wiki/D2S
Sorry that I don't know the name in English.
Maybe Chickens and Rabbits problem


Explanation
tomate number t should not be odd,
and it should valid that c * 2 <= t && t <= c * 4.

From
jumbo + small = cheese
jumbo * 2 + small = tomate / 2

We can get that
jumb0 = tomate / 2 - cheese
So that
small = cheese * 2 - tomate / 2


Complexity
Time O(1)
Space O(1)

T and C are given

4*J + 2S = T
J  +  S  = C

"""


class Solution:
    def numOfBurgers(self, t, c):
        return [t // 2 - c, c * 2 - t // 2] if t % 2 == 0 and c * 2 <= t <= c * 4 else []



