

class Solution:
    def removeVowels(self, S: str) -> str:

        remove = "aeiou"
        res = []
        for char in S:
            if char not in remove:
                res.append(char)

        return "".join(res)



