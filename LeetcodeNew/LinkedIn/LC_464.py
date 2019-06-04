
def canIWin(self, maxChoosableInteger, desiredTotal):
    """
    :type maxChoosableInteger: int
    :type desiredTotal: int
    :rtype: bool
    """
    if (1 + maxChoosableInteger) * maxChoosableInteger /2 < desiredTotal:
        return False
    self.memo = {}
    return self.helper(range(1, maxChoosableInteger + 1), desiredTotal)


def helper(self, nums, desiredTotal):

    hash = str(nums)
    if hash in self.memo:
        return self.memo[hash]

    if nums[-1] >= desiredTotal:
        return True

    for i in range(len(nums)):
        if not self.helper(nums[:i] + nums[ i +1:], desiredTotal - nums[i]):
            self.memo[hash ]= True
            return True
    self.memo[hash] = False
    return False


class Solution(object):
    def helper(self, allowed, target, so_far, cache):
        if len(allowed) == 0:
            return False
        state = tuple(allowed)
        if state in cache:
            return cache[state]
        else:
            cache[state] = False
            if max(allowed) + so_far >= target:
                cache[state] = True
            else:
                for x in allowed:
                    new_allowed = [y for y in allowed if x != y]
                    if self.helper(new_allowed, target, so_far + x, cache) == False:
                        cache[state] = True
                        break
            return cache[state]

    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        allowed = [x for x in range(1, maxChoosableInteger + 1)]
        if sum(allowed) < desiredTotal:
            return False
        return self.helper(allowed, desiredTotal, 0, {})


class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        choosable = tuple(range(1, maxChoosableInteger + 1))
        if sum(choosable) < desiredTotal: return False
        self.cache = {}
        return self.dfs(choosable, desiredTotal)

    def dfs(self, choosable, total):
        if choosable[-1] >= total: return True
        key = choosable
        if key in self.cache: return self.cache[key]
        for i in range(len(choosable)):
            if not self.dfs(choosable[:i] + choosable[i + 1:], total - choosable[i]):
                self.cache[key] = True
                return True
        self.cache[key] = False
        return False




