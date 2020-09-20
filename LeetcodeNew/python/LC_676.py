
import collections


class MagicDictionary:
    def __init__(self):
        self.table = collections.defaultdict(set)

    def buildDict(self, dictionary) -> None:
        for word in dictionary:
            n = len(word)
            if n not in self.table:
                self.table[n] = set()
            self.table[n].add(word)

    def search(self, searchWord: str) -> bool:
        n = len(searchWord)
        if n not in self.table:
            return False

        for s in self.table[n]:
            count = 0
            for i in range(n):
                if searchWord[i] != s[i]:
                    count += 1

            if count == 1:
                return True

        return False



