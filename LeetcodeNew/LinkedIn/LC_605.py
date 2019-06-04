"""
Explanation:

We can put one flower in every three contingous empty spots, after put that flower in the middle of three, the thrid one can be counted into the "next three spots". So we set the count variable to be 1.

Since the head and the tail are special cases, we insert a empty spot at head and append a empty spot at the tail.
"""


def canPlaceFlowers(self, flowerbed, n):

    flowerbed.insert(0, 0)
    flowerbed.append(0)
    count = 0
    for f in flowerbed:
        if f == 0:
            count += 1
        else:
            count = 0
        if count == 3:
            n -= 1
            count = 1
        if n == 0:
            return True
    return False


def canPlaceFlowers(self, a, n):
    if n == 0: return True
    a = [0] + a + [0]
    for i in range(1, len(a) - 1):
        if a[i - 1] == a[i] == a[i + 1] == 0:
            a[i] = 1
            n -= 1
            if n == 0: return True

    return False



