class Solution:
    def replaceElements(self, arr):
        maxi = -1
        for i in range(len(arr) - 1, -1, -1):
            arr[i], maxi = maxi, max(arr[i], maxi)
        return arr


