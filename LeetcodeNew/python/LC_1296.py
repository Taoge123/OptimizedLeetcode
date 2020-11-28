import collections


class Solution:
    def isPossibleDivide(self, nums, k: int) -> bool:
        count = collections.Counter(nums)

        while count:
            mini = min(count)
            for i in range(mini, mini + k):
                if i not in count:
                    return False
                elif count[i] == 1:
                    del count[i]
                else:
                    count[i] -= 1

        return True



