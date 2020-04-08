
"""
Given many words, words[i] has weight i.

Design a class WordFilter that supports one function, WordFilter.f(String prefix,
String suffix). It will return the word with given prefix and suffix with maximum weight.
If no word exists, return -1.

Examples:

Input:
WordFilter(["apple"])
WordFilter.f("a", "e") // returns 0
WordFilter.f("b", "") // returns -1


Note:

words has length in range [1, 15000].
For each test case, up to words.length queries WordFilter.f may be made.
words[i] has length in range [1, 10].
prefix, suffix have lengths in range [0, 10].
words[i] and prefix, suffix queries consist of lowercase letters only.

"""

"""
Method 1
Store all the words corresponding to its prefixes and suffixes. 
For example, for two words bat and bar, the prefixes and suffixes dictionary will look as such:

# prefixes
{
  '': {'bat', 'bar'},
  'b': {'bat', 'bar'},
  'ba': {'bat', 'bar'},
  'bar': {'bar'},
  'bat': {'bat'},
}

# suffixes
{
  't': {'bat'},
  'at': {'bat'},
  'bat': {'bat'},
  'r': {'bar'},
  'ar': {'bar'},
  'bar': {'bar'},
}
f('b', 'at') => set intersection of {'bat', 'bar'} and {'bat'} => 'bat'.

You can use a Trie to make it more space efficient as well.
"""
import collections


class WordFilter:

    def __init__(self, words):
        self.prefixes = collections.defaultdict(set)
        self.suffixes = collections.defaultdict(set)
        self.weights = {}
        for index, word in enumerate(words):
            prefix, suffix = '', ''
            for char in [''] + list(word):
                prefix += char
                self.prefixes[prefix].add(word)
            for char in [''] + list(word[::-1]):
                suffix += char
                self.suffixes[suffix[::-1]].add(word)
            self.weights[word] = index

    def f(self, prefix, suffix):
        weight = -1
        for word in self.prefixes[prefix] & self.suffixes[suffix]:
            if self.weights[word] > weight:
                weight = self.weights[word]
        return weight


"""
Method 2
Directly save the prefix and suffix combinations for a word, where the value is the weight. 
For a word such as 'bat', store all the prefix + suffix combinations in a dictionary, 
delimited by a non-alphabet character such as '.'. 
The delimiter is important so as to distinguish between prefix/suffix pairs 
that would have been concatenated to give the same result if without - ab + c 
and a + bc would both give abc if there wasn't a delimiter present.

{
  '.': 0,
  '.t': 0,
  '.at': 0,
  '.bat': 0,
  'b.': 0,
  'b.t': 0,
  'b.at': 0,
  'b.bat': 0,
  'ba.': 0,
  'ba.t': 0,
  'ba.at': 0,
  'ba.bat': 0,
  'bat.': 0,
  'bat.t': 0,
  'bat.at': 0,
  'bat.bat': 0,
}
Later occurrences of the prefix + suffix combi will have its weight overwritten, 
so we can simply look up the dictionary and return the answer.
"""

class WordFilter2:

    def __init__(self, words):
        self.inputs = {}
        for index, word in enumerate(words):
            prefix = ''
            for char in [''] + list(word):
                prefix += char
                suffix = ''
                for char in [''] + list(word[::-1]):
                    suffix += char
                    self.inputs[prefix + '.' + suffix[::-1]] = index

    def f(self, prefix, suffix):
        return self.inputs.get(prefix + '.' + suffix, -1)


class WordFilter22:

    def __init__(self, words):

        self.dic = {}
        for weight, word in enumerate(words):
            for i in range(len(word) + 1):
                for j in range(len(word) + 1):
                    self.dic[word[:i] + "#" + word[j:]] = weight

    def f(self, prefix, suffix):

        return self.dic.get(prefix + '#' + suffix, -1)



class WordFilter3:

    def __init__(self, words):
        self.seen = {}
        for index, word in enumerate(words):
            self.seen.update({
                (word[:pre], word[post:]): index
                for pre  in range(len(word) + 1)
                for post in range(len(word) + 1)
            })

    def f(self, prefix, suffix):
        return self.seen.get((prefix, suffix), -1)


class Trie:

    def __init__(self):
        self.isWord = False
        self.children = {}

    def insert(self, word):
        node = self
        for c in word:
            if c not in node.children:
                node.children[c] = Trie()
            node = node.children[c]
        node.isWord = True

    def searchPrefix(self, prefix):
        words = []
        node = self
        for c in prefix:
            if c not in node.children:
                return words
            node = node.children[c]
        self.findAllWords(node, prefix, words)
        return words

    def findAllWords(self, node, path, words):
        if node.isWord:
            words.append(path)
        for c, nxtNode in node.children.items():
            self.findAllWords(nxtNode, path + c, words)

class WordFilter4:
    def __init__(self, words):
        self.weightMap = {word: i for i, word in enumerate(words)}
        self.prefixTrie, self.suffixTrie = Trie(), Trie()
        for word in words:
            self.prefixTrie.insert(word)
            self.suffixTrie.insert(word[::-1])

        self.prefixCache = {}
        self.suffixCache = {}

    def f(self, prefix, suffix):
        if prefix in self.prefixCache:
            prefixWords = self.prefixCache[prefix]
        else:
            prefixWords = self.prefixTrie.searchPrefix(prefix)
            self.prefixCache[prefix] = prefixWords

        if suffix in self.suffixCache:
            suffixWords = self.suffixCache[suffix]
        else:
            suffixWords = [word[::-1] for word in self.suffixTrie.searchPrefix(suffix[::-1])]
            self.suffixCache[suffix] = suffixWords

        matchedWords = set(prefixWords) & set(suffixWords)
        maxWeight = -1
        for word in matchedWords:
            maxWeight = max(maxWeight, self.weightMap[word])
        return maxWeight




