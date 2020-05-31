
class Solution:
    def relativeSortArray(self, arr1, arr2):
        table = {val: i for i, val in enumerate(arr2)}
        return sorted(arr1, key=lambda i: table.get(i, 1000 + i))


