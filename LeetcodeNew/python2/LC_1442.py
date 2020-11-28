
class Solution:
    def countTriplets(self, arr) -> int:
        res = 0
        n = len(arr)
        for i in range(n - 1):
            summ = arr[i]
            for j in range(i + 1, n):
                summ ^= arr[j]
                if summ == 0:
                    res += j - i
        return res




class SolutionLee:
    def countTriplets(self, arr) -> int:
        arr.insert(0, 0)
        n = len(arr)

        for i in range(n - 1):
            arr[i + 1] ^= arr[i]

        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                if arr[i] == arr[j]:
                    res += j - i - 1
        return res




