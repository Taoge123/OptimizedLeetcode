
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
import collections

class Solution:
    def alienOrder(self, words) -> str:
        graph = collections.defaultdict(set)
        degree = {char: 0 for word in words for char in word}
        for i, word1 in enumerate(words[:-1]):
            word2 = words[i + 1]
            for c1, c2 in zip(word1, word2):
                if c1 == c2:
                    continue
                if c2 not in graph[c1]:
                    degree[c2] += 1
                graph[c1].add(c2)
                break
        res = ''
        queue = collections.deque([char for char in degree if not degree[char]])
        while queue:
            char = queue.popleft()
            res += char
            for nei in graph[char]:
                degree[nei] -= 1
                if not degree[nei]:
                    queue.append(nei)
        return res if len(res) == len(degree) else ''






