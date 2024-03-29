
class Solution:
    def isOneBitCharacter(self, bits) -> bool:
        n = len(bits)
        index = 0
        while index < n:
            if index == n-1:
                return True

            if bits[index] == 0:
                index += 1

            if bits[index] == 1:
                index += 2

        return False


class Solution2:
    def isOneBitCharacter(self, bits) -> bool:
        index = len(bits) - 2
        while index >= 0 and bits[index] > 0:
            index -= 1
        return (len(bits) - index) % 2 == 0








