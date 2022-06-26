
"""
In English, we have a concept called root, which can be followed by some other words to form another longer word -
let's call this word successor. For example, the root an, followed by other, which can form another word another.

Now, given a dictionary consisting of many roots and a sentence.
You need to replace all the successor in the sentence with the root forming it.
If a successor has many roots can form it, replace it with the root with the shortest length.

You need to output the sentence after the replacement.

Example 1:

Input: dict = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"


Note:

The input will only have lower-case letters.
1 <= dict words number <= 1000
1 <= sentence words number <= 1000
1 <= root length <= 100
1 <= sentence words length <= 1000
"""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.isWord = True

    def search(self, word):
        node = self.root
        for ch in word:
            node = node.children.get(ch)
            if node is None:
                return False
        return node.isWord


class SolutionTony:
    def replaceWords(self, dictionary, sentence: str) -> str:
        s = sentence.split()
        trie = Trie()
        for word in dictionary:
            trie.insert(word)
        res = []
        for word in s:
            flag = False
            for i in range(len(word)):
                # if we found one, flad turns to True
                if trie.search(word[:i]):
                    res.append(word[:i])
                    flag = True
                    break
            # if we never found one, add the original word
            if not flag:
                res.append(word)
        return " ".join(res)


