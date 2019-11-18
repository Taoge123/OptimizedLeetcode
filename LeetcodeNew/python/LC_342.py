
# class Solution:
#     def isPowerOfFour(self, num: int) -> bool:

#         while num > 1:
#             num /= 4
#         return num == 1

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num & num - 1 == 0 and (num - 1) % 3 == 0


