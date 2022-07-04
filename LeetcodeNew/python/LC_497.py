from sortedcontainers import SortedList, sortedset, sorteddict

"""
https://www.youtube.com/watch?v=1lfAuryQYLg
rand() % M -> [0, M-1]

____|   _____|    _________
0                       M-1 

l1 -> [0, 10] -> 7



"""
import random
import bisect

class SolutionTony:
    def __init__(self, rects):
        self.rects = rects
        self.areas = []
        self.sum = 0
        for i in range(len(rects)):
            self.sum += (rects[i][2] - rects[i][0] + 1) * (rects[i][3] - rects[i][1] + 1)
            self.areas.append(self.sum)

    def pick(self):
        rand = random.randint(1, self.sum)
        i = bisect.bisect_left(self.areas, rand)
        rect = self.rects[i]
        return [random.randint(rect[0], rect[2]), random.randint(rect[1], rect[3])]




class Solution:

    def __init__(self, rects):
        self.rects = rects
        self.table = {}
        self.sum = 0
        for i in range(len(rects)):
            self.sum += (rects[i][2] - rects[i][0] + 1) * (rects[i][3] - rects[i][1] + 1)
            self.table[self.sum] = i

    def pick(self):
        area = random.randint(1, self.sum)
        rect = self.getRect(area)

        # get a random point from this rectangle
        coordinates = self.rects[rect]
        rand_x = random.randint(coordinates[0], coordinates[2])
        rand_y = random.randint(coordinates[1], coordinates[3])
        return ([rand_x, rand_y])

    def getRect(self, area):
        if area in self.table:
            return self.table[area]

        mini = []
        for key in self.table:
            if key > area:
                mini.append(key)
        return self.table[min(mini)]





