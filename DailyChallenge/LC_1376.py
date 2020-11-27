class Solution:
    def numOfMinutes(self, n: int, headID: int, manager, informTime) -> int:
        cache = {}
        return max(self.cost(cache, n, i, headID, manager, informTime) for i in range(n))

    def cost(self, cache, n, index, headID, manager, informTime):
        if cache.get(index):
            return cache[index]
        else:
            if index == headID:
                return 0
            cache[index] = informTime[manager[index]] + self.cost(cache, n, manager[index], headID, manager, informTime)
            return cache[index]


