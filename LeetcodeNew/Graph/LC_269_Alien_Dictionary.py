
"""

https://leetcode.com/problems/alien-dictionary/discuss/208057/Python-solution
https://www.youtube.com/watch?v=71eHuQvSwc0
https://leetcode.com/problems/alien-dictionary/discuss/70280/Python-DFS-BFS-toposort-solutions
https://segmentfault.com/a/1190000003795463

There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

Example 1:

Input:
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]
There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

Example 1:

Input:
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

Output: "wertf"
Example 2:

Input:
[
  "z",
  "x"
]

Output: "zx"
Example 3:

Input:
[
  "z",
  "x",
  "z"
]

Output: ""

Explanation: The order is invalid, so return "".
Note:

You may assume all letters are in lowercase.
You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return any one of them is fine.

Output: "wertf"
Example 2:

Input:
[
  "z",
  "x"
]

Output: "zx"
Example 3:

Input:
[
  "z",
  "x",
  "z"
]

Output: ""

Explanation: The order is invalid, so return "".
Note:

You may assume all letters are in lowercase.
You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return any one of them is fine.

"""

"""
We do not need a DFS or BFS to detect if there is a cycle, 
because if the graph stop shrinking before all nodes are removed, 
it indicates that solution doesn't exist (a cycle in the graph)
"""

import collections

class Solution3:
    def alienOrder(self, words):
        # a -> b
        adj = collections.defaultdict(set)
        # in-degree
        degree = {char: 0 for word in words for char in word}
        for i, w1 in enumerate(words[:-1]):
            w2 = words[i + 1]
            for c1, c2 in zip(w1, w2):
                if c1 == c2: continue
                if c2 not in adj[c1]:
                    degree[c2] += 1
                adj[c1].add(c2)
                break
        res = ''
        # start w 0 indegree nodes
        queue = collections.deque([char for char in degree if not degree[char]])
        while queue:
            char = queue.popleft()
            res += char
            for nei in adj[char]:
                degree[nei] -= 1
                if not degree[nei]:
                    queue.append(nei)
        return res if len(res) == len(degree) else ''



class Node:
    def __init__(self):
        self.IN = set()
        self.OUT = set()

class Solution:
    def alienOrder(self, words):
        # initialization
        allnodes, graph, res = set("".join(words)), {}, ""
        for i in allnodes:
            graph[i] = Node()

        # build the graph
        for i in range(len(words) - 1):
            for j in zip(words[i], words[i + 1]):
                if j[0] != j[1]:
                    graph[j[0]].OUT.add(j[1])
                    graph[j[1]].IN.add(j[0])
                    break

        # topo-sort
        while allnodes:
            buff = set([i for i in allnodes if graph[i].OUT and not graph[i].IN])
            if not buff:
                # have solution if no connected node
                return res + "".join(allnodes) if not [i for i in allnodes if graph[i].IN] else ""
            res += "".join(buff)
            allnodes -= buff
            for i in allnodes:
                graph[i].IN -= buff
        return res


"""
Topological Sort Based Solution

Synoposis
    The basic idea behind this problem is simple. Build a graph from the dictionary of words. 
    Then do a topological sort of the words. The meat is in the details and corner cases.

Meaning of Lexicographically Smaller
    Understanding what lexicographically smaller really means. 
    Notice that adjacent words in the dictionary dictate the order. 
    Letters within the word do not determine the lexicographic order. 
    https://discuss.leetcode.com/topic/22395/the-description-is-wrong

Building an Input Graph
    - Graph is a dictionary with key as character and edge end points as a set
    - Every adjacent pair of word is extracted. All their characters are added to a graph as keys
    - Now every adjacent character is compared. The first non-matching character determines a relationship u -> v and is added to graph. 
      We break at this point since the remainder mis-matches do not imply any relationship.
    - Notice a pair like ("wrtkj","wrt") - > this indicates no relationship since wrt match 
      and then the smaller word is actually longer length than bigger word. 
      This needs to be reported as an error.
    - build_graph method returns the graph. If an error is found, empty graph is returned.

Topological Sort
    DFS or BFS can be used to implement topological sort. We use DFS.
    We run topological sort on each vertex.
    Topological sort requires a directed acyclic graph. If there is a cycle, we return True.
    How do we detect a cycle? We use the concept of back-edges. We maintain a visiting and visited array.
    Topological sort can be implemented using BFS as well. https://www.youtube.com/watch?v=71eHuQvSwc0
"""
"""
Interesting Examples

["wrtkj","wrt"] # Incorrect input
["a","b","a"] # Cycle
["wnlb"]

"""


class Solution2:
    def add_vertices(self, w, graph):
        for ch in w:
            if ch not in graph:
                graph[ch] = set([])
        return

    def add_words_to_graph(self, graph, w1, w2):
        self.add_vertices(w1, graph)
        self.add_vertices(w2, graph)
        min_length = min(len(w1), len(w2))
        found = False
        for i in range(min_length):
            if w1[i] != w2[i]:
                graph[w1[i]].add(w2[i])
                found = True
                break
        if found == False and len(w1) > len(w2):
            return False  # "abstract", "abs" is an error. But "abs", "abstract" is perfectly fine.
        return True

    def build_graph(self, words):
        graph = {}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            if not self.add_words_to_graph(graph, w1, w2):
                return {}
        self.add_vertices(words[-1], graph)
        return graph

    def topo_dfs(self, x, g, visited, visiting, st):  # Return True if there is a cycle
        visited.add(x)
        visiting.add(x)
        for nbr in g[x]:
            if nbr in visiting:  # Back-Edge!
                return True
            if nbr not in visited:
                if self.topo_dfs(nbr, g, visited, visiting, st):
                    return True
        visiting.remove(x)
        st.append(x)
        return False

    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        if words == []:
            return ""
        graph = self.build_graph(words)
        visited, visiting, st = set([]), set([]), []
        for k in graph.keys():
            if k not in visited:
                if self.topo_dfs(k, graph, visited, visiting, st):
                    return ""
        st.reverse()
        return "".join(st)




"""

The idea is to create a graph of characters and then find topological sorting 
of the created graph. Following are the detailed steps.

1) Create a graph g with number of vertices equal to the size of alphabet 
in the given alien language. For example, if the alphabet size is 5, 
then there can be 5 characters in words. Initially there are no edges in graph.

2) Do following for every pair of adjacent words in given sorted array.
…..a) Let the current pair of words be word1 and word2. 
One by one compare characters of both words and find the first mismatching characters.
…..b) Create an edge in g from mismatching character of word1 to that of word2.

3) Print topological sorting of the above created graph.

Following is the implementation of the above algorithm.

"""
"""
思路: 真是麻烦的一笔的题, 让我想起当年写poj 1001的时候.

使用拓扑排序来解决这题吧. 用两个hash表, 一个来存每个出现过的字符的入度, 
另一个来存一个字符指向的字符集合, 即一个字符应该在另外字符的前面. 
然后就每次找出一个入度为0的字符, 并且更新这个字符指向的字符集入度减1. 如果还没有遍历完所有的字符, 
但是找不到入度为0的字符了,那么说明无法排序, 返回"". 有一些情况就是可能一次会有几个入度为0的字符, 
这样其实是没有严格的顺序的对这些字符, 这种情况就随便哪个都行.

"""








