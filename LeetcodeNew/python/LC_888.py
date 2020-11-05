
class Solution:
    def fairCandySwap(self, A, B):
        sumA = sum(A)
        sumB = sum(B)
        setB = set(B)

        for num in A:
            if num + (sumB - sumA) // 2 in setB:
                return [num, num + (sumB - sumA) // 2]


