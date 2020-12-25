
class Solution:
    def containsPattern(self, arr, m: int, k: int) -> bool:
        for i in range(len(arr)):
            subSet = arr[i: i +m]
            if subSet * k == arr[i: i + m *k]:
                return True
        return False


