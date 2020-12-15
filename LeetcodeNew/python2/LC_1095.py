
"""
https://leetcode.com/problems/find-in-mountain-array/discuss/317607/JavaC%2B%2BPython-Triple-Binary-Search
"""


class MountainArray:
    def get(self, index: int) -> int:
        pass
    def length(self) -> int:
        pass

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:


        def findpeakidx(i :int, j :int, mountain_arr :'MountainArray' )- >int:
            k = (i + j) // 2
            s = mountain_arr.get(k)
            t = mountain_arr.get(k - 1)
            u = mountain_arr.get(k + 1)
            if s > t and s > u:
                return k
            elif s > t and s < u:
                return findpeakidx(k, j, mountain_arr)
            elif s < t and s > u:
                return findpeakidx(i, k, mountain_arr)

        i = 0
        j = mountain_arr.length() - 1
        idx = findpeakidx(i, j, mountain_arr)


        def leftbin(target :int, i :int, j :int, mountain_arr )- >int:
            if i == j + 1:
                return -1
            k = (i + j) // 2
            s = mountain_arr.get(k)
            if target == s:
                return k
            elif target > s:
                return leftbin(target, k + 1, j, mountain_arr)
            else:
                return leftbin(target, i, k - 1, mountain_arr)


        def rightbin(target :int, i :int, j :int, mountain_arr )- >int:
            if i == j + 1:
                return -1
            k = (i + j) // 2
            s = mountain_arr.get(k)
            if target == s:
                return k
            elif target > s:
                return rightbin(target, i, k - 1, mountain_arr)
            else:
                return rightbin(target, k + 1, j, mountain_arr)

        left = leftbin(target, i, idx, mountain_arr)
        if left == -1:
            return rightbin(target, idx, j, mountain_arr)
        else:
            return left


