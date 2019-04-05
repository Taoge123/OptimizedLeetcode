
"""
Implement a MapSum class with insert, and sum methods.

For the method insert, you'll be given a pair of (string, integer).
The string represents the key and the integer represents the value.
If the key already existed, then the original key-value pair will be overridden to the new one.

For the method sum, you'll be given a string representing the prefix,
and you need to return the sum of all the pairs' value whose key starts with the prefix.

Example 1:
Input: insert("apple", 3), Output: Null
Input: sum("ap"), Output: 3
Input: insert("app", 2), Output: Null
Input: sum("ap"), Output: 5
"""
import collections

class MapSum1:
    def __init__(self):
        self.map = {}

    def insert(self, key, val):
        self.map[key] = val

    def sum(self, prefix):
        return sum(val for key, val in self.map.items() if key.startswith(prefix))


class MapSum2:
    def __init__(self):
        self.map = {}
        self.score = collections.Counter()

    def insert(self, key, val):
        delta = val - self.map.get(key, 0)
        self.map[key] = val
        for i in xrange(len(key) + 1):
            prefix = key[:i]
            self.score[prefix] += delta

    def sum(self, prefix):
        return self.score[prefix]


class TrieNode:
    __slots__ = 'children', 'score'
    def __init__(self):
        self.children = {}
        self.score = 0

class MapSum(object):
    def __init__(self):
        self.map = {}
        self.root = TrieNode()

    def insert(self, key, val):
        delta = val - self.map.get(key, 0)
        self.map[key] = val
        cur = self.root
        cur.score += delta
        for char in key:
            cur = cur.children.setdefault(char, TrieNode())
            cur.score += delta

    def sum(self, prefix):
        cur = self.root
        for char in prefix:
            if char not in cur.children:
                return 0
            cur = cur.children[char]
        return cur.score


"""
A standard Trie-based solution where each node keeps track of the total count of its children.

For inserting, we first determine if the string already exists in the Trie. 
If it does, we calculate the difference in the previous and new value, 
and update the nodes with the difference as we traverse down the Trie nodes.

Sum is simple because each node already holds the sum of its children 
and we simply have to traverse to the node and obtain its count.

This results in both operations being O(k), where k is the length of the string/prefix.
"""


class TrieNode():
    def __init__(self, count=0):
        self.count = count
        self.children = {}


class MapSum3:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        self.keys = {}

    def insert(self, key, val):
        # Time: O(k)
        curr = self.root
        delta = val - self.keys.get(key, 0)
        self.keys[key] = val

        curr = self.root
        curr.count += delta
        for char in key:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
            curr.count += delta

    def sum(self, prefix):

        # Time: O(k)
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return 0
            curr = curr.children[char]
        return curr.count


class MapSum4:

    def __init__(self):
        self.Dict={}

    def insert(self, key, val):
        print("Null")
        self.Dict[key]=val

    def sum(self, prefix):
        sum=0
        for key, val in self.Dict.items():
            if key.find(prefix)==0:
                sum=sum+val
        return sum

"""
def sum(self, prefix):
    return sum(v for k,v in self.map.items() if k.startswith(prefix))
"""



class MapSumSolutionLee:

    def __init__(self):
        self.d = {}

    def insert(self, key, val):
        self.d[key] = val

    def sum(self, prefix):
        return sum(self.d[i] for i in self.d if i.startswith(prefix))





