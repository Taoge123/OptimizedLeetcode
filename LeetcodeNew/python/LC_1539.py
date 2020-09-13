import collections

class SolutionTony:
    def findKthPositive(self, arr, k: int) -> int:
        maxi = max(arr)
        count = collections.Counter(arr)

        for num in range(1, maxi):
            if not count[num]:
                k -= 1
                if k == 0:
                    return num
        return maxi + k

