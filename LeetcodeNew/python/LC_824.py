
class Solution:
    def toGoatLatin(self, S: str) -> str:
        vowel = set('aeiouAEIOU')
        return ' '.join(self.latin(word, i, vowel) for i, word in enumerate(S.split()))

    def latin(self, word, i, vowel):
        if word[0] not in vowel:
            word = word[1:] + word[0]
        return word + 'ma' + 'a' * (i + 1)


class SolutionCs:
    def toGoatLatin(self, S: str) -> str:
        vowels = set("aeiouAEIOU")
        # for ch in "aeioAEIOU":
        res = []
        count = 0
        for word in S.split(" "):
            count += 1
            if count > 1:
                res.append(" ")
            if word[0] in vowels:
                res.append(word)
            else:
                res.append(word[1:] + word[0])

            res.append("ma")
            for j in range(count):
                res.append("a")

        return "".join(res)



