class Solution:
    def reverseOnlyLetters(self, S: str) -> str:

        left, right = 0, len(S) - 1
        S = list(S)

        while left < right:
            if not S[left].isalpha():
                left += 1
            if not S[right].isalpha():
                right -= 1

            if S[left].isalpha() and S[right].isalpha():
                S[left], S[right] = S[right], S[left]

                left += 1
                right -= 1

        return "".join(S)



class Solution2:
    def reverseOnlyLetters(self, S):
        S, i, j = list(S), 0, len(S) - 1
        while i < j:
            if not S[i].isalpha():
                i += 1
            elif not S[j].isalpha():
                j -= 1
            else:
                S[i], S[j] = S[j], S[i]
                i, j = i + 1, j - 1
        return "".join(S)
