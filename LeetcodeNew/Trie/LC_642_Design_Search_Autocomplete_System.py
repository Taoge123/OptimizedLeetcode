"""
https://leetcode.com/problems/design-search-autocomplete-system/solution/
Design a search autocomplete system for a search engine. Users may input a sentence (at least one word and end with a special character '#'). For each character they type except '#', you need to return the top 3 historical hot sentences that have prefix the same as the part of sentence already typed. Here are the specific rules:
The hot degree for a sentence is defined as the number of times a user typed the exactly same sentence before.
The returned top 3 hot sentences should be sorted by hot degree (The first is the hottest one). If several sentences have the same degree of hot, you need to use ASCII-code order (smaller one appears first).
If less than 3 hot sentences exist, then just return as many as you can.
When the input is a special character, it means the sentence ends, and in this case, you need to return an empty list.
Your job is to implement the following functions:
The constructor function:
AutocompleteSystem(String[] sentences, int[] times): This is the constructor. The input is historical data. Sentences is a string array consists of previously typed sentences. Times is the corresponding times a sentence has been typed. Your system should record these historical data.
Now, the user wants to input a new sentence. The following function will provide the next character the user types:
List<String> input(char c): The input c is the next character typed by the user. The character will only be lower-case letters ('a' to 'z'), blank space (' ') or a special character ('#'). Also, the previously typed sentence should be recorded in your system. The output will be the top 3 historical hot sentences that have prefix the same as the part of sentence already typed.
Example:
Operation: AutocompleteSystem(["i love you", "island","ironman", "i love leetcode"], [5,3,2,2])
The system have already tracked down the following sentences and their corresponding times:
"i love you" : 5 times
"island" : 3 times
"ironman" : 2 times
"i love leetcode" : 2 times
Now, the user begins another search:
Operation: input('i')
Output: ["i love you", "island","i love leetcode"]
Explanation:
There are four sentences that have prefix "i". Among them, "ironman" and "i love leetcode" have same hot degree. Since ' ' has ASCII code 32 and 'r' has ASCII code 114, "i love leetcode" should be in front of "ironman". Also we only need to output top 3 hot sentences, so "ironman" will be ignored.
Operation: input(' ')
Output: ["i love you","i love leetcode"]
Explanation:
There are only two sentences that have prefix "i ".
Operation: input('a')
Output: []
Explanation:
There are no sentences that have prefix "i a".
Operation: input('#')
Output: []
Explanation:
The user finished the input, the sentence "i a" should be saved as a historical sentence in system. And the following input will be counted as a new search.
Note:
The input sentence will always start with a letter and end with '#', and only one blank space will exist between two words.
The number of complete sentences that to be searched won't exceed 100. The length of each sentence including those in the historical data won't exceed 100.
Please use double-quote instead of single-quote when you write test cases even for a character input.
Please remember to RESET your class variables declared in class AutocompleteSystem, as static/class variables are persisted across multiple test cases. Please see here for more details.
"""


class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.isEnd = False
        self.data = None
        self.rank = 0


class AutocompleteSystem(object):
    def __init__(self, sentences, times):
        self.root = TrieNode()
        self.keyword = ""
        for i, sentence in enumerate(sentences):
            self.addRecord(sentence, times[i])

    def addRecord(self, sentence, hot):
        p = self.root
        for c in sentence:
            if c not in p.children:
                p.children[c] = TrieNode()
            p = p.children[c]
        p.isEnd = True
        p.data = sentence
        p.rank -= hot

    def dfs(self, root):
        ret = []
        if root:
            if root.isEnd:
                ret.append((root.rank, root.data))
            for child in root.children:
                ret.extend(self.dfs(root.children[child]))
        return ret

    def search(self, sentence):
        p = self.root
        for c in sentence:
            if c not in p.children:
                return []
            p = p.children[c]
        return self.dfs(p)

    def input(self, c):
        results = []
        if c != "#":
            self.keyword += c
            results = self.search(self.keyword)
        else:
            self.addRecord(self.keyword, 1)
            self.keyword = ""
        return [item[1] for item in sorted(results)[:3]]

"""
Can someone tell me why p.rank -= hot?
Becasue it later uses sorted() on the tuples. 
But we need to sort assending for senetce and descending for rank. 
So by negating the rank, it can easily just sort assending as the default for sorted is.
"""

"""
Let's use a trie. Because the requirement to enter the top 3 at a node can only get stronger, 
we do not have to recall discarded information. 
Thus, we can freely store the answer (top 3 sentences) directly on each node. 
When we get queries, we simply read off the answer.
Whenever we add a sentence, at each node of the corresponding trie, 
we will update that node's info appropriately in case its top 3 answers changes. 
We'll use a "ShortList" to store our answer, which will keep track of only the top 3 answers.
Our implementation could be better (for example, handling ShortList better, 
or storing sentence indices instead of full sentences), 
but because the limits are small, it doesn't matter for the question, 
so we choose the most straightforward approach.
"""
_trie = lambda: collections.defaultdict(_trie)
INFO, END = True, False


class ShortList(list):
    def append(self, val):
        for i, (nt, s) in enumerate(self):
            if s == val[1]:
                self[i] = val
                break
        else:
            list.append(self, val)

        self.sort()
        if len(self) > 3:
            self.pop()


class AutocompleteSystem(object):

    def __init__(self, sentences, counts):
        self.curnode = self.trie = _trie()
        self.sentence_to_count = collections.Counter()
        self.search = ''

        for sentence, count in zip(sentences, counts):
            self.add(sentence, count)

    def add(self, sentence, count):
        self.sentence_to_count[sentence] = count
        cur = self.trie
        self._add_info(cur, sentence, count)
        for letter in sentence:
            cur = cur[letter]
            self._add_info(cur, sentence, count)
        cur[END] = sentence

    def _add_info(self, node, sentence, count):
        if INFO not in node:
            node[INFO] = ShortList()
        node[INFO].append((-count, sentence))

    def input(self, c):
        if c != '#':
            self.search += c
            if self.curnode is None:
                return []
            if c not in self.curnode:
                self.curnode = None
                return []

            self.curnode = self.curnode[c]
            return [s for nt, s in self.curnode[INFO]]
        else:
            self.sentence_to_count[self.search] += 1
            self.add(self.search, self.sentence_to_count[self.search])
            self.search = ''
            self.curnode = self.trie
            return []


"""
This question is very clear if using Trie. Notice in Python, 
you can simply using dictionary to build trie tree. 
The way to mark the end of sentence in trie try is to store then sentence itself. 
There are multiply place to improve in my solution apparently.
One place to go is instead of always searching for the root of Trie tree, 
store current node. In fact that's why I write my search function 
in a kinda ugly way that combine dfs and prefix search together with a varible cur. 
You can probably try to modify a little to store current search state 
so that we don't need to always search from the root.
In addition, I didn't use priority queue since in Python 
it's a little bit tricky to update priority cuz there is no built-in function in heapq to do that.
"""


class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word):
        cur = self.root
        for l in word:
            if l not in cur:
                cur[l] = {}
            cur = cur[l]
        cur['#'] = word

    def search(self, prefix, cur=None):  # Python cannot set default value to be self.varible cuz it's not a value yet
        if not cur: cur = self.root
        for l in prefix:
            if l not in cur:
                return []
            cur = cur[l]
        # dfs from l to get the word
        ret = []

        for k in cur:
            if k == '#':
                ret.append(cur[k])
            else:
                ret += self.search('', cur[k])
        return ret


class AutocompleteSystem2:

    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        self.lookUp = {}
        for i, s in enumerate(sentences):
            self.lookUp[s] = times[i]
        self.trie = Trie()
        for s in sentences:
            self.trie.insert(s)
        self.keyword = ""

    def input(self, c):

        if c == '#':  # should be saved as a historical sentence in system
            self.lookUp[self.keyword] = self.lookUp.get(self.keyword, 0) + 1
            self.trie.insert(self.keyword)
            self.keyword = ""
            return []

        self.keyword += c
        lst = self.trie.search(self.keyword)
        lst.sort(key=lambda x: (-self.lookUp[x], x))
        return lst[:3]





class TrieNode:
    def __init__(self):
        self.children = dict()
        self.sentences = set()

class AutocompleteSystem(object):

    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        self.buffer = ''
        self.stimes = collections.defaultdict(int)
        self.trie = TrieNode()
        for s, t in zip(sentences, times):
            self.stimes[s] = t
            self.addSentence(s)
        self.tnode = self.trie

    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        ans = []
        if c != '#':
            self.buffer += c
            if self.tnode: self.tnode = self.tnode.children.get(c)
            if self.tnode: ans = sorted(self.tnode.sentences, key=lambda x: (-self.stimes[x], x))[:3]
        else:
            self.stimes[self.buffer] += 1
            self.addSentence(self.buffer)
            self.buffer = ''
            self.tnode = self.trie
        return ans

    def addSentence(self, sentence):
        node = self.trie
        for letter in sentence:
            child = node.children.get(letter)
            if child is None:
                child = TrieNode()
                node.children[letter] = child
            node = child
            child.sentences.add(sentence)


class TrieNode():
    def __init__(self):
        # Initialising one node for trie
        self.children = {}
        self.last = False


class Trie():
    def __init__(self):

        # Initialising the trie structure.
        self.root = TrieNode()
        self.word_list = []

    def formTrie(self, keys):

        # Forms a trie structure with the given set of strings
        # if it does not exists already else it merges the key
        # into it by extending the structure as required
        for key in keys:
            self.insert(key)  # inserting one key to the trie.

    def insert(self, key):

        # Inserts a key into trie if it does not exist already.
        # And if the key is a prefix of the trie node, just
        # marks it as leaf node.
        node = self.root

        for a in list(key):
            if not node.children.get(a):
                node.children[a] = TrieNode()

            node = node.children[a]

        node.last = True

    def search(self, key):

        # Searches the given key in trie for a full match
        # and returns True on success else returns False.
        node = self.root
        found = True

        for a in list(key):
            if not node.children.get(a):
                found = False
                break

            node = node.children[a]

        return node and node.last and found

    def suggestionsRec(self, node, word):

        # Method to recursively traverse the trie
        # and return a whole word.
        if node.last:
            self.word_list.append(word)

        for a, n in node.children.items():
            self.suggestionsRec(n, word + a)

    def printAutoSuggestions(self, key):

        # Returns all the words in the trie whose common
        # prefix is the given key thus listing out all
        # the suggestions for autocomplete.
        node = self.root
        not_found = False
        temp_word = ''

        for a in list(key):
            if not node.children.get(a):
                not_found = True
                break

            temp_word += a
            node = node.children[a]

        if not_found:
            return 0
        elif node.last and not node.children:
            return -1

        self.suggestionsRec(node, temp_word)

        for s in self.word_list:
            print(s)
        return 1


# Driver Code
keys = ["hello", "dog", "hell", "cat", "a",
        "hel", "help", "helps", "helping"]  # keys to form the trie structure.
key = "hel"  # key for autocomplete suggestions.
status = ["Not found", "Found"]

# creating trie object
t = Trie()

# creating the trie structure with the
# given set of strings.
t.formTrie(keys)

# autocompleting the given key using
# our trie structure.
comp = t.printAutoSuggestions(key)

if comp == -1:
    print("No other strings found with this prefix\n")
elif comp == 0:
    print("No string found with this prefix\n")































