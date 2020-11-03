
class Solution:
    def sumOfDigits(self, A) -> int:
        mini = min(A)
        return 0 if sum([int(i) for i in str(mini)]) % 2 == 1 else 1

