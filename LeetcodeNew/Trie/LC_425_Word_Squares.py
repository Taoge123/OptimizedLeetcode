
"""
https://leetcode.com/problems/word-squares/discuss/91344/Short-PythonC%2B%2B-solution
https://leetcode.com/problems/word-squares/discuss/91360/3-Python-Solutions-with-very-detailed-explanations
https://leetcode.com/problems/word-squares/discuss/211745/Python-Two-Methods%3A-Backtracking-Trie
https://leetcode.com/problems/word-squares/discuss/217488/Python-Beats-100
https://leetcode.com/problems/word-squares/discuss/91375/Python-Trie-solution-with-comments
https://leetcode.com/problems/word-squares/discuss/129025/AC-python3-clear-solution-using-trie-and-DFS
https://leetcode.com/problems/word-squares/discuss/91330/Python-Trie-solution
https://leetcode.com/problems/word-squares/discuss/91351/Python-486ms-beat-100




The output consists of two word squares.
The order of output does not matter (just the order of words in each word square matters).
Example 2:

Input:
["abat","baba","atan","atal"]

Output:
[
  [ "baba",
    "abat",
    "baba",
    "atan"
  ],
  [ "baba",
    "abat",
    "baba",
    "atal"
  ]
]

Explanation:
The output consists of two word squares.
The order of output does not matter (just the order of words in each word square matters).

"""
import collections

class Solution1:
    def wordSquares(self, words):

        trie = {}
        self.build_trie(words, trie)

        size = len(words[0])

        result = []
        self.find_word_squares(trie, size, [], result)
        return result

    def build_trie(self, words, trie):
        for word in words:
            self.add_str(word, trie)

    def add_str(self, string, root):
        node = root
        for letter in string:
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        node['#'] = string

    def search_prefix(self, node, prefix, candidates):
        if '#' in node:
            candidates.append(node['#'])
            return

        for letter in prefix:
            if letter not in node:
                return
            node = node[letter]

        for letter in node:
            self.search_prefix(node[letter], '', candidates)

    def find_word_squares(self, trie, size, cur, result):
        if len(cur) == size:
            result.append(cur[:])
            return

        candidates = []
        prefix = ''.join([string[len(cur)] for string in cur])
        self.search_prefix(trie, prefix, candidates)

        for candidate in candidates:
            self.find_word_squares(trie, size, cur + [candidate], result)


"""
1. All words are equal length. So the dimensions of a word square will be len(word[0])
2. Now our approach will be to incrementally build a solution. 
   The solution built will be kept in so_far array. 
  This buildup of the solution will follow a general backtracking template - process_solution and generate_candidates.
3. generate_candidates will produce prefix using the so_far array. 
   Now the next word that can be added to the so_far array must have this prefix. 
   Check the visual in this link to understand this better: 
   https://discuss.leetcode.com/topic/63516/explained-my-java-solution-using-trie-126ms-16-16
"""

class Solution2:
    def generate_candidates(self, so_far, words):
        prefix =  "".join([x[len(so_far)] for x in so_far])
        for w in words:
            if w.startswith(prefix):
                yield w

    def helper(self, so_far, N, words, results):
        if len(so_far) == N:
            results.append([x for x in so_far])
        else:
            for c in self.generate_candidates(so_far, words):
                so_far.append(c)
                self.helper(so_far, N, words, results)
                so_far.pop()
        return

    def wordSquares(self, words):

        results = []
        if words:
            self.helper([], len(words[0]), words, results)
        return results


"""
Optimized solution using Hash-Tables

1. In the previous brute force solution, the bottle-neck was that we had to linearly scan 
   all the words to filter those words which start with a prefix.
2. What if we pre-process all words and store in a hash table. 
   The key would be the prefix and value would be the list of words with that prefix.
3. Then we can lookup all words with a prefix in constant time!
4. We implement a new class called PrefixHashTable and store a mapping of all prefixes to words in it.
"""


class PrefixHashTable:
    def __init__(self, words):
        self.prefix_table = {}
        for w in words:
            for prefix in (w[0:i] for i in range(len(w))):
                self.prefix_table.setdefault(prefix, set([])).add(w)
        return

    def get_prefix_matches(self, prefix):
        candidates = self.prefix_table[prefix] if prefix in self.prefix_table else set([])
        return candidates


class Solution3:
    def helper(self, so_far, N, words, results, table):
        if len(so_far) == N:
            results.append([x for x in so_far])
        else:
            prefix = "".join([x[len(so_far)] for x in so_far])
            for c in table.get_prefix_matches(prefix):
                so_far.append(c)
                self.helper(so_far, N, words, results, table)
                so_far.pop()
        return

    def wordSquares(self, words):

        results = []
        if words:
            table = PrefixHashTable(words)
            self.helper([], len(words[0]), words, results, table)
        return results


"""
Optimized solution using Tries

Prefix matching can also be done using Tries.
We implement a simple Trie and encapsulate it within the PrefixTrie API.
"""


class TrieNode:
    def __init__(self, value):
        self.nxt = [None] * 26
        self.value = value
        return


class PrefixTrieTable(object):
    def __init__(self, words):
        self.root = TrieNode(None)
        for w in words:
            self.add_to_trie(w)
        return

    def add_to_trie(self, w):
        root = self.root
        for ch in w:
            offset = ord(ch) - ord('a')
            if root.nxt[offset] != None:
                root = root.nxt[offset]
            else:
                root.nxt[offset] = TrieNode(None)
                root = root.nxt[offset]
        root.value = w
        return

    def collect(self, root, candidates):
        if root.value:
            candidates.append(root.value)
        else:
            for i in range(26):
                if root.nxt[i]:
                    self.collect(root.nxt[i], candidates)
        return

    def get_prefix_matches(self, prefix):
        candidates, root = [], self.root
        for ch in prefix:
            offset = ord(ch) - ord('a')
            root = root.nxt[offset]
            if root == None:
                return candidates
        self.collect(root, candidates)
        return candidates


class Solution5:
    def helper(self, so_far, N, words, results, table):
        if len(so_far) == N:
            results.append([x for x in so_far])
        else:
            prefix = "".join([x[len(so_far)] for x in so_far])
            for c in table.get_prefix_matches(prefix):
                so_far.append(c)
                self.helper(so_far, N, words, results, table)
                so_far.pop()
        return

    def wordSquares(self, words):

        results = []
        if words:
            table = PrefixTrieTable(words)
            self.helper([], len(words[0]), words, results, table)
        return results


"""
Append next prefix if row[i] == col[i] in arr
"""
class Solution6:
    def wordSquares(self, words):
        pref, res = collections.defaultdict(set), []
        for w in words:
            for i in range(len(w)):
                pref[w[:i + 1]].add(w)
        def dfs(i, arr):
            if i == len(arr[0]):
                res.append(arr)
            else:
                for w in pref["".join(row[i] for row in arr)]:
                    dfs(i + 1, arr + [w])
        for w in words:
            dfs(1, [w])
        return res


