
"""
This is ArrayReader's API interface.
You should not implement it, or speculate about its implementation
"""
class ArrayReader:
    # Compares the sum of arr[l..r] with the sum of arr[x..y]
	# return 1 if sum(arr[l..r]) > sum(arr[x..y])
	# return 0 if sum(arr[l..r]) == sum(arr[x..y])
	# return -1 if sum(arr[l..r]) < sum(arr[x..y])
   def compareSub(self, l: int, r: int, x: int, y: int) -> int:
        pass
    # Returns the length of the array
   def length(self) -> int:
        pass


class Solution:
    def getIndex(self, reader: 'ArrayReader') -> int:
        n = reader.length()
        left = 0
        right = n- 1

        while left < right:
            mid = left + (right - left) // 2
            if (right - left + 1) % 2 == 0:
                compare = reader.compareSub(left, mid, mid + 1, right) # even
            else:
                compare = reader.compareSub(left, mid, mid, right) # odd

            if compare < 0:
                left = mid + 1
            else:
                right = mid

        return left


