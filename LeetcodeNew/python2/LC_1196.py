class Solution:
    def maxNumberOfApples(self, arr) -> int:
        arr.sort()
        presum = [arr[0]]
        for i in range(1, len(arr)):
            presum.append(presum[-1] + arr[i])

        print(arr)
        print(presum)
        for i in range(len(presum)):
            if presum[i] > 5000:
                return i
        return len(arr)

