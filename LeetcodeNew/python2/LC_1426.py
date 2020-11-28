
class Solution:
    def countElements(self, arr) -> int:
        arr_set = set(arr)

        res = 0
        for num in arr:
            if num + 1 in arr_set:
                res += 1
        return res


