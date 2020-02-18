
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












