
class Solution:
    def toGoatLatin(self, S: str) -> str:
        vowel = set('aeiouAEIOU')
        return ' '.join(self.latin(word, i, vowel) for i, word in enumerate(S.split()))

    def latin(self, word, i, vowel):
        if word[0] not in vowel:
            word = word[1:] + word[0]
        return word + 'ma' + 'a' * (i + 1)







