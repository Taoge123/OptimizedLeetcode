import collections

class Solution:
    def mostCommonWord(self, paragraph: str, banned) -> str:
        banned = set(banned)
        res = ""
        max_count = 0
        table = collections.defaultdict(int)
        word_buffer = []

        for i, char in enumerate(paragraph):
            # 1). consume the characters in a word
            if char.isalnum():
                word_buffer.append(char.lower())
                if i != len(paragraph ) -1:
                    continue

            # 2). at the end of one word or at the end of paragraph
            if len(word_buffer) > 0:
                word = "".join(word_buffer)
                if word not in banned:
                    table[word] +=1
                    if table[word] > max_count:
                        max_count = table[word]
                        res = word
                # reset the buffer for the next word
                word_buffer = []

        return res

