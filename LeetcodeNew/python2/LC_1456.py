class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        res = count = 0
        for i, char in enumerate(s):
            if char in vowels:
                count += 1
            if i >= k and s[i - k] in vowels:
                count -= 1
            res = max(count, res)
        return res



class SolutionTony:
    def maxVowels(self, s: str, k: int) -> int:
        if k >= len(s):
            return s.count('a') + s.count('e') + s.count('i') + s.count('o') + s.count('u')

        vow = ['a', 'e', 'i', 'o', 'u']
        count = 0
        left = 0
        res = 0
        for right in range(len(s)):

            if s[right] in vow:
                count += 1
            if right >= k:
                if s[left] in vow:
                    count -= 1
                left += 1

            res = max(res, count)

        return res





