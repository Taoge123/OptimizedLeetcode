
class Solution:
    def duplicateZeros(self, arr) -> None:
        zero = arr.count(0)
        n = len(arr)
        for i in range(n - 1, -1, -1):
            if i + zero < n:
                arr[i + zero] = arr[i]

            if arr[i] == 0:
                zero -= 1
                if i + zero < n:
                    arr[i + zero] = 0




class Solution2:
    def duplicateZeros(self, arr) -> None:
        zero = 0
        n = len(arr)
        for i in range(n):
            if arr[i] == 0:
                zero += 1

        N = n + zero
        i = n - 1
        j = N - 1
        # We just need O(1) space if we scan from back
        # i point to the original array, j point to the new location
        while i < j:
            if arr[i] != 0:
                if j < n:
                    arr[j] = arr[i]
            else:
                if j < n:
                    arr[j] = arr[i]
                j -= 1
                # copy twice when hit '0'
                if j < n:
                    arr[j] = arr[i]

            i -= 1
            j -= 1



arr = [1,0,2,3,0,4,5,0]
a = Solution()
print(a.duplicateZeros(arr))


