
class Solution:
    def arraysIntersection(self, arr1, arr2, arr3):
        i = j = k = 0
        res = []
        while i< len(arr1) and j < len(arr2) and k < len(arr3):
            if arr1[i] == arr2[j] == arr3[k]:
                res.append(arr1[i])
                i, j, k = i + 1, j + 1, k + 1
                continue

            maxi = max(arr1[i], arr2[j], arr3[k])
            i = i + 1 if arr1[i] < maxi else i
            j = j + 1 if arr2[j] < maxi else j
            k = k + 1 if arr3[k] < maxi else k

        return res




