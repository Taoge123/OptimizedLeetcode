class Solution:
    def transformArray(self, arr):
        changed = True
        res = arr[:]

        while changed:
            changed = False
            for i in range(1, len(arr) - 1):
                if arr[i - 1] > arr[i] and arr[i + 1] > arr[i]:
                    res[i] = arr[i] + 1
                    changed = True

                if arr[i - 1] < arr[i] and arr[i + 1] < arr[i]:
                    res[i] = arr[i] - 1
                    changed = True
            arr = res[:]
        return res

