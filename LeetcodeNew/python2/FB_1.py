
"""
8. String to Integer (atoi)
"""
class Solution008:
    def myAtoi(self, s):

        ###better to do strip before sanity check (although 8ms slower):
        # ls = list(s.strip())
        if len(s) == 0:
            return 0
        ls = list(s.strip())
        if not ls:
            return 0
        sign = -1 if ls[0] == '-' else 1
        if ls[0] in ['-', '+']:
            del ls[0]
        res, i = 0, 0
        while i < len(ls) and ls[i].isdigit():
            res = res * 10 + ord(ls[i]) - ord('0')
            i += 1
        return max(-2 ** 31, min(sign * res, 2 ** 31 - 1))


"""
29. Divide Two Integers
"""
class Solution029:
    def divide(self, dividend: int, divisor: int) -> int:
        a, b = abs(dividend), abs(divisor)
        res = 0
        while a >= b:
            step, index = b, 1
            while a >= step:
                a -= step
                step += step
                res += index
                index += index

        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            res = -res
        return min(max(res, -pow(2 ,31)), pow(2 ,31) - 1)


"""
151. Reverse Words in a String
"""
class Solution151:
    def reverseWords(self, s):
        print(list(reversed(s.split())))
        return ' '.join(reversed(s.split()))


class SolutionCaikehe151:
    def reverseWords(self, s):
        s = list(" ".join(s.split()))[::-1]
        i = 0
        while i < len(s):
            start = i
            while i < len(s) and not s[i].isspace():
                i += 1
            self.reverse(s, start, i-1)
            i += 1
        return "".join(s)

    def reverse(self, s, i, j):
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1; j -= 1


"""
220. Contains Duplicate III
"""

"""
解法II：“滑动窗口” + TreeSet
参考LeetCode Discuss：https://leetcode.com/discuss/38177/java-o-n-lg-k-solution

TreeSet数据结构（Java）使用红黑树实现，是平衡二叉树的一种。

该数据结构支持如下操作：

1. floor()方法返set中≤给定元素的最大元素；如果不存在这样的元素，则返回 null。

2. ceiling()方法返回set中≥给定元素的最小元素；如果不存在这样的元素，则返回 null。

Java代码：
public class Solution {
    public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
        if(k < 1 || t < 0)
            return false;
        TreeSet<Integer> set = new TreeSet<Integer>();
        for(int i = 0; i < nums.length; i++){
            int n = nums[i];
            if(set.floor(n) != null && n <= t + set.floor(n) || 
                    set.ceiling(n) != null && set.ceiling(n) <= t + n)
                return true;
            set.add(n);
            if (i >= k)
                set.remove(nums[i - k]);
        }
        return false;
    }
}
"""
"""
题目大意：
给定一个整数数组，判断其中是否存在两个不同的下标i和j满足：| nums[i] - nums[j] | <= t 并且 | i - j | <= k

解题思路：
解法I：“滑动窗口” + 字典（桶）
如果： | nums[i] - nums[j] | <= t   式a

等价： | nums[i] / t - nums[j] / t | <= 1   式b

推出： | floor(nums[i] / t) - floor(nums[j] / t) | <= 1   式c

​等价： floor(nums[j] / t) ∈ {floor(nums[i] / t) - 1, floor(nums[i] / t), floor(nums[i] / t) + 1} 式d
其中式b是式c的充分非必要条件，因为逆否命题与原命题等价，所以：

如果： floor(nums[j] / t) ∉ {floor(nums[i] / t) - 1, floor(nums[i] / t), floor(nums[i] / t) + 1} 非d

推出： | nums[i] - nums[j] | > t   非a
因此只需要维护一个大小为k的窗口（字典）numDict，其中键为nums[i] / t，值为nums[i]。

遍历数组nums时，检查nums[i]与键集{floor(nums[i] / t) - 1, floor(nums[i] / t), floor(nums[i] / t) + 1}对应的值的差值即可。
"""
class Solution220:
    def containsNearbyAlmostDuplicate(self, nums, k: int, t: int) -> bool:

        if t < 0:
            return False
        n = len(nums)
        table = {}
        bucket = t + 1
        for i in range(n):
            val = nums[i] // bucket
            if val in table:
                return True
            if val - 1 in table and abs(nums[i] - table[val - 1]) < bucket:
                return True
            if val + 1 in table and abs(nums[i] - table[val + 1]) < bucket:
                return True
            table[val] = nums[i]
            if i >= k:
                del table[nums[i - k] // bucket]
        return False





import collections
class Solution166:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        res = ""
        res += "-" if (numerator > 0) ^ (denominator > 0) else ""
        num, den = abs(numerator), abs(denominator)

        res += str(num // den)
        num %= den
        if num == 0:
            return res
        res += "."
        table = collections.defaultdict(int)
        table[num] = len(res)

        while num != 0:
            num *= 10
            res += str(num // den)
            num %= den

            if num in table:
                index = table[num]
                res = res[:index] + "(" + res[index:] + ")"
                break
            else:
                table[num] = len(res)
        return res




"""
468. Validate IP Address
"""


class Solution468:
    def validIPAddress(self, IP: str) -> str:
        if IP.count(".") == 3 and all(self.isIPv4(i) for i in IP.split(".")):
            return "IPv4"
        if IP.count(":") == 7 and all(self.isIPv6(i) for i in IP.split(":")):
            return "IPv6"

        return "Neither"

    def isIPv4(self, s):
        try:
            return str(int(s)) == s and 0 <= int(s) <= 255
        except:
            return False

    def isIPv6(self, s):
        if len(s) > 4:
            return False
        try:
            # print(int(s, 16), '---')
            return int(s, 16) >= 0 and s[0] != '-'
        except:
            return False


# s = "0201:0db8:85a3:0000:0000:8a2e:0370:7334"
# a = Solution468()
# for item in s.split(':'):
#     print(a.isIPv6(item))


"""
91. Decode Ways
"""

class Solution091:
    def numDecodings(self, s: str) -> int:
        if s == "":
            return 0
        n = len(s)
        dp = [0 for x in range(n +1)]
        dp[0] = 1

        for i in range(1, n + 1):
            if s[i -1] != '0':
                dp[i] += dp[i-1]
            if i != 1 and s[i-2:i] >= "10" and s[i-2:i] <= "26":
                dp[i] += dp[i-2]

        return dp[-1]

s = "12"
a = Solution091()
print(a.numDecodings(s))

"""
163. Missing Ranges
"""

class Solution:
    def findMissingRanges(self, nums, lower, upper):
        res = []
        n = len(nums)
        pre = cur = lower - 1

        for i in range(n + 1):
            if i == n:
                cur = upper + 1
            else:
                cur = nums[i]
            if cur - pre >= 2:
                res.append(self.getRange(pre + 1, cur - 1))
            pre = cur
        return res

    def getRange(self, lower, upper):
        if lower == upper:
            return "{}".format(lower)
        else:
            return "{}->{}".format(lower, upper)


"""
523. Continuous Subarray Sum
"""

class Solution523:
    def checkSubarraySum(self, nums, k: int) -> bool:
        summ = 0
        table = {}
        table[0] = -1
        for i in range(len(nums)):
            summ += nums[i]
            if k != 0:
                summ = summ % k

            if summ in table:
                if i - table[summ] > 1:
                    return True
            else:
                table[summ] = i

        return False



"""
130. Surrounded Regions
"""


class Solution130:
    def solve(self, board) -> None:
        if len(board) == 0:
            return
        m, n = len(board), len(board[0])
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for i in range(m):
            self.dfs(board, i, 0, m, n)
            self.dfs(board, i, n - 1, m, n)

        for j in range(n):
            self.dfs(board, 0, j, m, n)
            self.dfs(board, m - 1, j, m, n)

        for i in range(m):
            for j in range(n):
                if board[i][j] == '#':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'

    def dfs(self, board, i, j, m, n):
        if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != 'O':
            return
        board[i][j] = '#'
        for direction in self.directions:
            x = i + direction[0]
            y = j + direction[1]
            self.dfs(board, x, y, m, n)


"""
15. 3Sum
"""
class Solution015:
    def threeSum(self, nums):
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if i == 0 or i > 0 and nums[i - 1] != nums[i]:
                left = i + 1
                right = len(nums) - 1

                while left < right:
                    s = nums[i] + nums[left] + nums[right]
                    if s == 0:
                        res.append([nums[i], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

                    elif s < 0:
                        left += 1
                    else:
                        right -= 1
        return res


"""
98. Validate Binary Search Tree
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution098:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.helper(root, float('-inf'), float('inf'))

    def helper(self, root, low, high):
        if not root:
            return True

        if not root.left and not root.right:
            return low < root.val < high

        return low < root.val < high and self.helper(root.left, low, root.val) and self.helper(root.right, root.val, high)




"""
402. Remove K Digits
"""

class Solution402:
    def removeKdigits(self, num, k):
        stack = []
        if k >= len(num):
            return "0"
        for item in num:
            while stack and k and stack[-1] > item:
                stack.pop()
                k -= 1
            stack.append(item)
        while k:
            stack.pop()
            k -= 1
        return str(int("".join(stack)))


"""
179. Largest Number
"""
from functools import cmp_to_key

class Solution179:
    def largestNumber(self, nums):
        nums = [str(num) for num in nums]
        nums = sorted(nums, key=cmp_to_key(lambda x, y: int(y + x) - int(x + y)))

        res = ''.join(nums).lstrip('0')
        return res or '0'


"""
127. Word Ladder
"""
import string
class Solution127:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        wordList = set(wordList)
        visited = set()
        queue = collections.deque([(beginWord, 1)])
        lowercase = string.ascii_lowercase
        while queue:
            word, dist = queue.popleft()
            if word == endWord:
                return dist
            for i in range(len(word)):
                for j in lowercase:
                    if j != word[i]:
                        newWord = word[:i] + j + word[ i +1:]
                        if newWord not in visited and newWord in wordList:
                            queue.append((newWord, dist + 1))
                            visited.add(newWord)

        return 0


"""
5. Longest Palindromic Substring
"""
class Solution005:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) < 1:
            return ""
        res = ""
        for i in range(len(s)):
            tmp = self.helper(s, i, i)
            res = tmp if len(tmp) > len(res) else res
            tmp = self.helper(s, i, i + 1)
            res = tmp if len(tmp) > len(res) else res
        return res

    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r]


"""
50. Pow(x, n)
"""
class Solution050:
    def myPow(self, x: float, n: int) -> float:
        if n > 0:
            return self.power(x, n)
        else:
            return 1 / self.power(x, -n)

    def power(self, x, n):
        if n == 0:
            return 1
        mid = self.power(x, n // 2)
        if n % 2 == 0:
            return mid * mid
        else:
            return mid * mid * x



"""
324. Wiggle Sort II
"""
class Solution324:
    def wiggleSort(self, nums):
        arr = sorted(nums)
        for i in range(1, len(nums), 2):
            nums[i] = arr.pop()
        for i in range(0, len(nums), 2):
            nums[i] = arr.pop()



"""
3. Longest Substring Without Repeating Characters
"""
class Solution003:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, res = 0, 0
        table = {}
        n = len(s)
        for i in range(n):
            if s[i] in table and start <= table[s[i]]:
                start = table[s[i]] + 1
            else:
                res = max(res, i - start + 1)
            table[s[i]] = i
        return res



"""
146. LRU Cache
"""

class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None

class LRUCache146:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key in self.dic:
            node = self.dic[key]
            self._remove(node)
            self._add(node)
            return node.val
        return -1

    def put(self, key, value):
        if key in self.dic:
            self._remove(self.dic[key])
        node = Node(key, value)
        self._add(node)
        self.dic[key] = node
        if len(self.dic) > self.capacity:
            node = self.head.next
            self._remove(node)
            del self.dic[node.key]


    def _add(self, node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail

    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p


"""
152. Maximum Product Subarray
"""
class Solution152:
    def maxProduct(self, nums):
        mini = maxi = res = nums[0]

        for num in nums[1:]:
            temp = maxi
            maxi = max(max(maxi * num, mini * num), num)
            mini = min(min(mini * num, temp * num), num)
            res = max(res, maxi)
        return res



"""
71. Simplify Path
"""

class Solution071:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        stack = []
        for item in path:
            if item not in ["", "..", "."]:
                stack.append(item)
            elif item == ".." and stack:
                stack.pop()
        return "/" + "/".join(stack)



"""
556. Next Greater Element III
similar to next permutation
这道题让我们求下一个排列顺序，由题目中给的例子可以看出来，如果给定数组是降序，则说明是全排列的最后一种情况，
则下一个排列就是最初始情况，可以参见之前的博客 Permutations。我们再来看下面一个例子，有如下的一个数组
1　　2　　7　　4　　3　　1
下一个排列为：
1　　3　　1　　2　　4　　7
那么是如何得到的呢，我们通过观察原数组可以发现，
1. 如果从末尾往前看，数字逐渐变大，到了2时才减小的，
2. 然后我们再从后往前找第一个比2大的数字，是3，
3. 那么我们交换2和3，
4. 再把此时3后面的所有数字转置一下

1　　2　　7　　4　　3　　1
1　　2　　7　　4　　3　　1
1　　3　　7　　4　　2　　1
1　　3　　1　　2　　4　　7
"""

class Solution556:
    def nextGreaterElement(self, n: int) -> int:
        nums = list(str(n))
        length = len(nums)
        i, j = length - 2, length - 1
        while i >= 0 and nums[i + 1] <= nums[i]:
            i -= 1
        if i < 0:
            return -1
        while nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
        res = int("".join(nums[:i + 1] + nums[i + 1:][::-1]))
        if res >= 2 ** 31 or res == n:
            return -1
        return res


class Solution031:
    def nextPermutation(self, nums):
        small, large = -1, -1
        n = len(nums)
        for i in range(n - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                small = i - 1
                break

        if small == -1:
            nums[:] = nums[::-1]
            return

        for i in range(n - 1, small, -1):
            if nums[i] > nums[small]:
                nums[i], nums[small] = nums[small], nums[i]
                break
        nums[:] = nums[:small+1] + nums[small+1:][::-1]
        return nums


"""
708. Insert into a Sorted Circular Linked List
"""

class Node708:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class Solution708:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':

        if head == None:
            newNode = Node708(insertVal, None)
            newNode.next = newNode
            return newNode

        prev, curr = head, head.next
        toInsert = False

        while True:
            if prev.val <= insertVal <= curr.val:
                # Case #1.
                toInsert = True
            elif prev.val > curr.val:
                # Case #2. where we locate the tail element
                # 'prev' points to the tail, i.e. the largest element!
                if insertVal >= prev.val or insertVal <= curr.val:
                    toInsert = True

            if toInsert:
                prev.next = Node(insertVal, curr)
                # mission accomplished
                return head

            prev, curr = curr, curr.next
            # loop condition
            if prev == head:
                break
        # Case #3.
        # did not insert the node in the loop
        prev.next = Node(insertVal, curr)
        return head



"""
133. Clone Graph
"""


class Node133:
    def __init__(self, val=0, neighbors=[]):
        self.val = val
        self.neighbors = neighbors

class Solution133:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        graph = collections.defaultdict(list)
        return self.dfs(node, graph)

    def dfs(self, node, graph):
        if node in graph:
            return graph[node]
        newNode = Node133(node.val, [])
        graph[node] = newNode
        for nei in node.neighbors:
            newNode.neighbors.append(self.dfs(nei, graph))
        return newNode


"""
310. Minimum Height Trees
"""

class Solution310:
    def findMinHeightTrees(self, n: int, edges):
        if n == 1:
            return [0]

        graph = collections.defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        leaves = [i for i in range(n) if len(graph[i]) == 1]
        while n > 2:
            n -= len(leaves)
            newLeaves = []
            for leaf in leaves:
                #remove from both direction
                j = graph[leaf].pop()
                graph[j].remove(leaf)
                if len(graph[j]) == 1:
                    newLeaves.append(j)
            leaves = newLeaves
        return leaves


"""
这道题让我们求下一个排列顺序，由题目中给的例子可以看出来，如果给定数组是降序，则说明是全排列的最后一种情况，
则下一个排列就是最初始情况，可以参见之前的博客 Permutations。我们再来看下面一个例子，有如下的一个数组
1　　2　　7　　4　　3　　1
下一个排列为：
1　　3　　1　　2　　4　　7
那么是如何得到的呢，我们通过观察原数组可以发现，
1. 如果从末尾往前看，数字逐渐变大，到了2时才减小的，
2. 然后我们再从后往前找第一个比2大的数字，是3，
3. 那么我们交换2和3，
4. 再把此时3后面的所有数字转置一下

    1　　2　　7　　4　　3　　1
      small
    1　　2　　7　　4　　3　　1
    1　　3　　7　　4　　2　　1
    1　　3　　1　　2　　4　　7

"""


class Solution031_:
    def nextPermutation(self, nums):
        small, n = -1, len(nums)
        for i in range(n-1, 0, -1):
            if nums[i-1] < nums[i]:
                small = i-1
                break
        #654321 -> 123456
        if small == -1:
            nums[:] = nums[::-1]
            return

        for i in range(n - 1, small - 1, -1):
            if nums[i] > nums[small]:
                nums[small], nums[i] = nums[i], nums[small]
                break

        nums[:] = nums[:small + 1] + nums[small + 1:][::-1]

"""
307. Range Sum Query - Mutable
"""
class BinaryIndexTree:
    def __init__(self, nums):
        n = len(nums)
        self.nums = [0 for _ in range(n + 1)]
        self.tree = [0 for _ in range(n + 1)]
        for i, num in enumerate(nums):
            self.set(i + 1, num)

    def _lowbit(self, a):
        return a & -a

    def set(self, i, val):
        diff = val - self.nums[i]
        self.nums[i] = val
        while i < len(self.tree):
            self.tree[i] += diff
            i += self._lowbit(i)

    def get(self, i):
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= self._lowbit(i)
        return res


class NumArray:
    def __init__(self, nums):
        self.bit = BinaryIndexTree(nums)

    def update(self, i, val):
        self.bit.set(i + 1, val)

    def sumRange(self, i, j):
        return self.bit.get(j + 1) - self.bit.get(i)


"""
794. Valid Tic-Tac-Toe State
"""

"""
# if the first player wins, the 'X' count number(c1) should be one more than 'O'(c2).
# if the second player wins, the 'X' count number should be equal to 'O'.
# they cannot both win, no need to check. bcoz otherwise c1==c2-1==c2, which is never true.
"""

class Solution794:
    def isWin(self, board, char):
        for i in range(3):  # Row check
            if board[i] == char * 3:
                return True
        for i in range(3):  # Column check
            if board[0][i] == char and board[1][i] == char and board[2][i] == char:
                return True
        if board[0][0] == char and board[1][1] == char and board[2][2] == char or \
                board[0][2] == char and board[1][1] == char and board[2][0] == char:  # Diagonal check
            return True
        return False

    def validTicTacToe(self, board):
        countX = countO = 0
        for i in range(3):
            for j in range(3):
                countX += 1 if board[i][j] == 'X' else 0
                countO += 1 if board[i][j] == 'O' else 0
        if countO > countX or countX > countO + 1:
            return False
        if countO == countX and self.isWin(board, 'X') or countX == countO + 1 and self.isWin(board, 'O'):
            return False
        return True


"""
161. One Edit Distance
"""
class Solution161:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if (abs(len(s) - len(t))) > 1:
            return False
        if s == t:
            return False
        for i in range(min(len(s), len(t))):
            if s[i] != t[i]:
                return s[i + 1:] == t[i + 1:] or s[i:] == t[i + 1:] or s[i + 1:] == t[i:]
        return True

"""
138. Copy List with Random Pointer
"""

class Node138:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


class Solution138:
    def copyRandomList(self, head: 'Node') -> 'Node':
        cache = dict()
        m = n = head

        while m:
            cache[m] = Node138(m.val, m.next, m.random)
            m = m.next

        while n:
            cache[n].next = cache.get(n.next)
            cache[n].random = cache.get(n.random)
            n = n.next
        return cache.get(head)


"""
18. 4Sum
"""

class Solution018:
    def fourSum(self, nums, target):
        dic = collections.defaultdict(set)
        n = len(nums)
        nums.sort()
        if n < 4:
            return []

        res = set()

        for i in range(n - 1):
            for j in range(i + 1, n):
                sum = nums[i] + nums[j]

                for sub in dic[target - sum]:
                    res.add(tuple(list(sub) + [nums[j], nums[i]]))

            for j in range(i):
                dic[nums[i] + nums[j]].add((nums[j], nums[i]))
        return list(res)



"""
43. Multiply Strings
"""
class Solution043:
    def multiply(self, num1: str, num2: str) -> str:

        res = [0] * (len(num1) + len(num2))

        for i, n1 in enumerate(reversed(num1)):
            for j, n2 in enumerate(reversed(num2)):
                res[i + j] += int(n1) * int(n2)
                res[i + j +1] += res[ i +j] // 10
                res[i + j] %= 10

        # res = str(int("".join([str(i) for i in res][::-1])))
        return str(int("".join([str(i) for i in res][::-1])))


"""
54. Spiral Matrix
"""

class Solution054:
    def spiralOrder(self, matrix):
        res = []
        while matrix:
            res.extend(matrix.pop(0))
            if matrix and matrix[0]:
                for row in matrix:
                    res.append(row.pop())
            if matrix and matrix[0]:
                res.extend(matrix.pop()[::-1])
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    res.append(row.pop(0))
        return res


"""
353. Design Snake Game
"""
class SnakeGame353:
    def __init__(self, width: int, height: int, food):
        # E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        self.snake = collections.deque([[0 ,0]])    # snake head is at the front
        self.width = width
        self.height = height
        self.food = collections.deque(food)
        self.direct = {'U': [-1, 0], 'L': [0, -1], 'R': [0, 1], 'D': [1, 0]}

    def move(self, direction: str) -> int:
        newHead = [self.snake[0][0 ] +self.direct[direction][0], self.snake[0][1 ] +self.direct[direction][1]]
        # notice that the newHead can be equal to self.snake[-1]
        if (newHead[0] < 0 or newHead[0] >= self.height) or (newHead[1] < 0 or newHead[1] >= self.width) \
                or (newHead in self.snake and newHead != self.snake[-1]): return -1

        if self.food and self.food[0] == newHead:  # eat food
            self.snake.appendleft(newHead)   # just make the food be part of snake
            self.food.popleft()   # delete the food that's already eaten
        else:    # not eating food: append head and delete tail
            self.snake.appendleft(newHead)
            self.snake.pop()

        return len(self.snake) -1



"""
2. Add Two Numbers
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution002:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = cur = ListNode(0)
        carry = 0

        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            cur.next = ListNode(carry % 10)
            cur = cur.next
            carry //= 10

        return dummy.next


"""
81. Search in Rotated Sorted Array II
"""

class Solution081:
    def search(self, nums, target):
        if not nums:
            return False

        left, right = 0, len(nums) - 1
        while left < right:
            mid = (right - left)//2 + left
            if nums[mid] == target:
                return True

            if nums[mid] < nums[right]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

            elif nums[mid] > nums[right]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                right -= 1

        return nums[left] == target


"""
1197. Minimum Knight Moves
"""


class Solution1197:
    def minKnightMoves(self, x: int, y: int) -> int:
        if x == 0 and y == 0:
            return 0
        return self.bfs(abs(x), abs(y))


    def bfs(self, x, y):
        directions = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
        queue = collections.deque([(0, 0, 0)])
        visited = set()
        visited.add((0, 0))
        while queue:
            i, j, dis = queue.popleft()
            for move in directions:
                a, b = i + move[0], j + move[1]
                if (a,b) not in visited and a >= -5 and b >= -5:
                    if a == x and b == y:
                        return dis + 1
                    queue.append((a, b, dis+1))
                    visited.add((a, b))


"""
55. Jump Game
"""

class Solution055:
    def canJump(self, nums) -> bool:
        maxi = 0
        n = len(nums)

        for i, num in enumerate(nums):
            if maxi < i:
                return False
            if maxi >= n - 1:
                return True
            maxi = max(i + num, maxi)


"""
322. Coin Change
"""

class Solution322:
    def coinChange(self, coins, amount):
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for i in range(coin, amount + 1):
                if dp[i - coin] != float('inf'):
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return -1 if dp[amount] == float('inf') else dp[amount]



class Solution322_:
    def coinChange(self, coins, amount: int) -> int:

        cache = {}
        cache[0] = 0
        return self.helper(coins, amount, cache)

    def helper(self, coins, amount, cache):
        if amount in cache:
            return cache[amount]
        mini = amount + 1
        for coin in coins:
            if amount >= coin:
                count = 1
                left = self.helper(coins, amount - coin, cache)
                if left != -1:
                    count += left
                    mini = min(mini, count)
        cache[amount] = mini if mini != amount + 1 else -1
        return cache[amount]


"""
33. Search in Rotated Sorted Array
"""

class Solution033:
    def search(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]:  # here should include "==" case
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1


"""
79. Word Search
"""


class Solution079:
    def exist(self, board, word):
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if self.search(board, word, i, j, m, n):
                    return True
        return False

    def search(self, board, word, i, j, m, n):
        if len(word) == 0:
            return True
        if i < 0 or j < 0 or i >= m or j >= n or board[i][j] != word[0]:
            return False
        temp = board[i][j]
        board[i][j] = '#'
        result = self.search(board, word[1:], i + 1, j, m, n) \
                 or self.search(board, word[1:], i - 1, j, m, n) \
                 or self.search(board, word[1:], i, j + 1, m, n) \
                 or self.search(board, word[1:], i, j - 1, m, n)
        board[i][j] = temp
        return result


"""
93. Restore IP Addresses
"""

class Solution093:
    def restoreIpAddresses(self, s: str):
        res = []
        self.helper(s, 0, 0, "", res)
        return res

    def helper(self, s, index, count, path, res):
        if count > 4:
            return

        if count == 4 and index == len(s):
            res.append(path)
            return

        for i in range(1, 4):
            if index + i > len(s):
                break
            temp = s[index:index + i]
            if temp.startswith("0") and len(temp) > 1 or (i == 3 and int(temp) >= 256):
                continue
            if count == 3:
                self.helper(s, index + i, count + 1, path + temp + "", res)
            else:
                self.helper(s, index + i, count + 1, path + temp + ".", res)






class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False


class WordDictionary211:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.isWord = True

    def search(self, word):
        node = self.root
        self.res = False
        self.dfs(node, word)
        return self.res

    def dfs(self, node, word):
        if not word:
            if node.isWord:
                self.res = True
            return
        if word[0] == ".":
            for n in node.children.values():
                self.dfs(n, word[1:])
        else:
            node = node.children.get(word[0])
            if not node:
                return
            self.dfs(node, word[1:])






