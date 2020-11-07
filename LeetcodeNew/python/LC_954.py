import collections


class Solution:
    def canReorderDoubled(self, A) -> bool:
        count = collections.Counter(A)
        for num in sorted(A, key=abs):
            if count[num] == 0:
                continue
            if count[2 * num] == 0:
                return False
            count[num] -= 1
            count[2 * num] -= 1

        return True




class Solution2:
    def canReorderDoubled(self, A) -> bool:
        count = collections.Counter(A)
        for i in sorted(count.keys()):
            if count[i] <= 0:
                continue
            while count[i] > 0:
                count[i] -= 1
                if count[i * 2] > 0:
                    count[i * 2] -= 1
                elif count[i / 2] > 0:
                    count[i / 2] -= 1
                else:
                    return False
        return True
