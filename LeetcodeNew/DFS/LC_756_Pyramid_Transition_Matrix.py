"""

Example 1:
Input: bottom = "XYZ", allowed = ["XYD", "YZE", "DEA", "FFF"]
Output: true
Explanation:
We can stack the pyramid like this:
    A
   / \
  D   E
 / \ / \
X   Y   Z

This works because ('X', 'Y', 'D'), ('Y', 'Z', 'E'), and ('D', 'E', 'A') are allowed triples.
Example 2:
Input: bottom = "XXYX", allowed = ["XXX", "XXY", "XYX", "XYY", "YXZ"]
Output: false
Explanation:
We can't stack the pyramid to the top.
Note that there could be allowed triples (A, B, C) and (A, B, D) with C != D.

https://blog.csdn.net/fuxuemingzhu/article/details/82469175     --- beautiful
http://massivealgorithms.blogspot.com/2017/07/string-pyramids-transition-matrix-airbnb.html
http://www.cnblogs.com/grandyang/p/8476646.html

"""



import itertools
import collections



class Solution1:
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        table = collections.defaultdict(list)
        for triples in allowed:
            table[triples[:2]].append(triples[-1])
        return self.helper(bottom, "", table)

    def helper(self, curr, above, table):
        if len(curr) == 2 and len(above) == 1:
            return True
        if len(above) == len(curr) - 1:
            return self.helper(above, "", table)
        pos = len(above)
        base = curr[pos: pos + 2]
        if base in table:
            for ch in table[base]:
                if self.helper(curr, above + ch, table):
                    return True
        return False


# ---------------------
# 作者：负雪明烛
# 来源：CSDN
# 原文：https: // blog.csdn.net / fuxuemingzhu / article / details / 82469175
# 版权声明：本文为博主原创文章，转载请附上博文链接！

class Solution:
    def pyramidTransition(self, bottom, allowed):
        d = collections.defaultdict(set)
        for a, b, c in allowed:
            d[a, b].add(c)
        stack = [{b} for b in bottom]
        for _ in range(len(stack) - 1):
            nextStack = [set() for _ in range(len(stack) - 1)]
            for i in range(len(stack) - 1):
                for base in itertools.product(stack[i], stack[i + 1]):
                    nextStack[i] |= d[base]
            if not all(nextStack):
                return False
            stack = nextStack
        return True


class Solution2:
    def pyramidTransition(self, bottom, allowed):
        chars, allowed = {'A', 'B', 'C', 'D', 'E', 'F', 'G'}, set(allowed)
        def dfs(row, q, i):
            if len(row) == 1: return True
            for c in chars:
                if row[i: i + 2] + c in allowed:
                    if i == len(row) - 2 and dfs(q + c, "", 0): return True
                    elif dfs(row, q + c, i + 1): return True
            return False
        return dfs(bottom, "", 0)

class Solution3:
    def pyramidTransition(bottom, allowed):
        hashmap = dict()
        for triplet in allowed:
            if triplet[:2] not in hashmap:
                hashmap[triplet[:2]] = []
            hashmap[triplet[:2]] += [triplet[2]]

        def dfs(bottom):
            if len(bottom) == 2 and bottom in hashmap:
                return True
            options = []
            for i in range(len(bottom) - 1):
                if bottom[i:i + 2] in hashmap:
                    options.append(hashmap[bottom[i:i + 2]])
                else:
                    return False
            for bot in itertools.product(*options):
                if dfs(''.join(bot)):
                    return True
            return False

        return dfs(bottom)




a = Solution2()
print(a.pyramidTransition(bottom = "XYZ", allowed = ["XYD", "YZE", "DEA", "FFF"]))











