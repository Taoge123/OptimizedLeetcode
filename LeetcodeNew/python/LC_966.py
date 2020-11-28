"""
For each word in the wordlist,
get its the lower pattern and devowel pattern,

For each lower pattern, record the first such match to hashmap cap.
For each vowel pattern, record the first such match to hashmap vowel.

For each query,
check if it's in the words set,
check if there is a match in cap,
check if there is a match in vowel,
otherwise return "".


"""



class Solution:
    def spellchecker(self, wordlist, queries):
        def devowel(word):
            return "".join('*' if c in 'aeiou' else c
                           for c in word)

        words_perfect = set(wordlist)
        words_cap = {}
        words_vow = {}

        for word in wordlist:
            wordlow = word.lower()
            words_cap.setdefault(wordlow, word)
            words_vow.setdefault(devowel(wordlow), word)

        def solve(query):
            if query in words_perfect:
                return query

            queryL = query.lower()
            if queryL in words_cap:
                return words_cap[queryL]

            queryLV = devowel(queryL)
            if queryLV in words_vow:
                return words_vow[queryLV]
            return ""

        res = []
        for query in queries:
            res.append(solve(query))
        return res


