
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words) -> str:
        count = collections.defaultdict(int)
        res = ""
        for char in licensePlate:
            if char.isalpha():
                count[char.lower()] += 1

        for word in words:
            count2 = count.copy()
            for char in word:
                char = char.lower()
                if char in count2:
                    count2[char] -= 1
                    if not count2[char]:
                        del count2[char]
            if not count2 and (not res or len(word) < len(res)):
                res = word
        return res




