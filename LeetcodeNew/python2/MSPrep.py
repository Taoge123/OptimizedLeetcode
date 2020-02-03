

#204
class Solution224:
    def calculate(self, s):
        return self.helper(s, 0)

    def helper(self, s, i):
        sign, num = 1, 0
        res = 0
        while i < len(s):
            char = s[i]
            if char.isdigit():
                num = num * 10 + int(char)
            else:
                if num:
                    res += sign * num
                num = 0
                if char == '+':
                    sign = 1
                elif char == '-':
                    sign = -1
                elif char == '(':
                    nxt, i = self.helper(s, i + 1)
                    res += sign * nxt
                elif char == ')':
                    return res, i
            i += 1
        if num != 0:
            res += sign * num

        return res


# s = "-200-3-3-3"
# a = Solution()
# print(a.calculate(s))


class Solution227:
    def calculate(self, s):
        stack = []
        num, sign = 0, 1

        for i, char in enumerate(s):
            if char.isdigit():
                num = num * 10 + int(char)
            if char in '+-*/' or i == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    stack.append(int(stack.pop() / num))
                num = 0
                sign = char
        return sum(stack)


#
# s = "3+5 / 2"
# a = Solution227()
# print(a.calculate(s))



class Solution772:
    def calculate(self, s):
        s = s + '$'
        return self.helper(s, [], 0)

    def helper(self, s, stack, i):
        num, sign = 0, '+'
        while i < len(s):
            char = s[i]
            if char == " ":
                i += 1
                continue
            if char.isdigit():
                num = 10 + int(char)
            elif char == '(':
                num, i = self.helper(s, stack, i + 1)
            else:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    stack.append(int(stack.pop() / num))
                i += 1
                if char == ')':
                    return sum(stack), i
                sign = char
                num = 0

                num = 0
                sign = char

        return sum(stack)



class Solution036:
    def isValidSudoku(self, board) -> bool:
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == '.':
                    for char in '123456789':
                        board[i][j] = char
                        if self.isValid(board, i, j) and self.isValidSudoku(board):
                            return True
                    return False
        return True

    def isValid(self, board, i, j):
        temp = board[i][j]
        board[i][j] = '.'
        for num in range(9):
            if board[num][j] == temp or board[i][num] == temp:
                return False

        for row in range(3):
            for col in range(3):
                if board[(i//3)*3 + row][(i//3)*3+col] == temp:
                    return False

        board[i][j] = temp
        return True



class Solution041:
    def firstMissingPositive(self, nums):
        n = len(nums)
        for i, num in enumerate(nums):
            if nums[i] <= 0:
                nums[i] = len(nums) + 2
        for i, num in enumerate(nums):
            absolute = abs(num)
            if absolute <= n:
                nums[absolute-1] = -abs(nums[absolute-1])
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        return n + 1

#
# nums = [1,1,4,5]
# a = Solution041()
# print(a.firstMissingPositive(nums))
#

class Solution044:
    def isMatch(self, s, p):
        dp = [[False for i in range(len(p)+1)] for j in range(len(s) + 1)]
        dp[0][0] = True
        for j in range(1, len(p) + 1):
            if [j-1] != '*':
                break
            dp[0][j] = True

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j-1] in [s[i-1], '?']:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]

        return dp[-1][-1]


class Solution044Version2:
    def isMatch(self, s, p):
        i, j = 0, 0
        match, start = 0, -1

        while i < len(s):
            if j < len(p) and (s[i] == p[j] or p[j] == '?'):
                i += 1
                j += 1
            elif j < len(p) and p[j] == '*':
                star = j
                match = i
                j += 1
            elif star != -1:
                j = star + 1
                match += 1
                i = match
            else:
                return False

        while j < len(p) and p[j] == '*':
            j += 1

        return j == len(p)
#
# s = 'bbjbc'
# p = '*c'
# a = Solution044Version2()
# print(a.isMatch(s, p))
#

class Solution045:
    def jump(self, nums):
        if len(nums) <= 1:
            return 0

        start, end = 0, nums[0]
        res = 0
        while end < len(nums):
            res += 1
            nxt = max(i + nums[i] for i in range(start, end+1))
            start, end = end, nxt

        return res

nums = [2,3,1,1,4]
a = Solution045()
print(a.jump(nums))


class Solution051:
    def solveQueens(self, n):
        res = []
        self.dfs([-1] * n, 0, [], res)
        return res

    def dfs(self, nums, index, path, res):
        if index == len(nums):
            res.append(path)
            return
        for i in range(len(nums)):
            nums[index] = i
            if self.isValid(nums, index):
                temp = '.' * len(nums)
                self.dfs(nums, index + 1, path + [temp[:i]+'Q'+temp[i+1:]], res)

    def isValid(self, nums, n):
        for i in range(n):
            if nums[i] == nums[n] or abs(nums[i] - nums[n]) == abs(n - i):
                return False
        return True


# a = Solution051()
# print(a.solveQueens(8))

# ---------------------------------------------------------------------------------


class Solution1239:
    def maxLength(self, arr) -> int:

        dp = [set()]
        for string in arr:
            # if string contains duplicated
            if len(set(string)) < len(string):
                continue
            string = set(string)
            for char in dp[:]:
                if string & char:
                    continue
                dp.append(string | char)

        return max(len(s) for s in dp)



class Solution2:
    def __init__(self):
        self.res = 0

    def maxLength(self, arr) -> int:
        self.backtrack([], 0, arr)
        return self.res

    def backtrack(self, path, pos, arr):
        self.res = max(self.res, len("".join(path)))
        for i in range(pos, len(arr)):
            path.append(arr[i])
            temp = "".join(path)
            if len(set(temp)) == len(temp):
                self.backtrack(path, i + 1, arr)
            path.pop()






class Solution:
    def reverseWords(self, s):
        print(list(reversed(s.split())))
        return ' '.join(reversed(s.split()))


class SolutionCaikehe:
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






class TicTacToe:

    def __init__(self, n: int):
        self.row = [0] * n
        self.col = [0] * n
        self.diag = 0
        self.anti_diag = 0
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        offset = -1 if player == 1 else 1
        self.row[row] += offset
        self.col[col] += offset
        if row == col:
            self.diag += offset
        if row + col == self.n - 1:
            self.anti_diag += offset
        if self.n in [self.row[row], self.col[col], self.diag, self.anti_diag]:
            return 2
        if -self.n in [self.row[row], self.col[col], self.diag, self.anti_diag]:
            return 1
        return 0




import collections
class LRUCache146:
    def __init__(self, capacity: int):
        self.dic = collections.OrderedDict()
        self.remain = capacity

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        node = self.dic.pop(key)
        self.dic[key] = node
        return node

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic.pop(key)
        else:
            if self.remain > 0:
                self.remain -= 1
            else:
                self.dic.popitem(last=False)
        self.dic[key] = value

class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None

class LRUCache:
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






class Node3:
    def __init__(self, k, v):
        self.prev = None
        self.next = None
        self.key = k
        self.val = v
        self.cnt = 1


class DoublyLinkedList:
    def __init__(self):
        self.head = Node3(0, 0)  # head is a dummy head node
        self.tail = Node3(0, 0)  # tail is a dummy tail node
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def addToHead(self, node):
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head
        self.size += 1

    def removeTail(self):
        prevTail = self.tail.prev
        node = self.tail.prev
        node.prev.next = self.tail
        self.tail.prev = node.prev
        self.size -= 1
        return prevTail

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1


class LFUCache460:
    def __init__(self, capacity):
        self.freqTable = collections.defaultdict(DoublyLinkedList)
        self.keyTable = {}
        self.capacity = capacity
        self.size = 0
        self.minFreq = 0

    def get(self, key):
        if key not in self.keyTable:
            return -1
        else:
            node = self.keyTable[key]
            prevCount = node.cnt
            node.cnt += 1
            self.freqTable[prevCount].removeNode(node)
            self.freqTable[node.cnt].addToHead(node)
            if prevCount == self.minFreq and self.freqTable[prevCount].size == 0:
                self.minFreq += 1
            return node.val

    def put(self, key, value):
        if self.capacity <= 0:
            return
        if key not in self.keyTable:
            node = Node3(key, value)
            self.keyTable[key] = node
            if self.size != self.capacity:
                self.freqTable[1].addToHead(node)
                self.size += 1
            else:
                prevTail = self.freqTable[self.minFreq].removeTail()
                self.keyTable.pop(prevTail.key)
                self.freqTable[1].addToHead(node)
            self.minFreq = 1
        else:
            node = self.keyTable[key]
            node.val = value
            prevCount = node.cnt
            node.cnt += 1
            self.freqTable[prevCount].removeNode(node)
            self.freqTable[node.cnt].addToHead(node)
            if prevCount == self.minFreq and self.freqTable[prevCount].size == 0:
                self.minFreq += 1







class Solution134:
    def canCompleteCircuit(self, gas, cost):
        if sum(gas) < sum(cost):
            return -1

        res = 0
        summ = 0
        for i in range(len(gas)):
            summ += gas[i] - cost[i]
            if summ < 0:
                summ = 0
                res = (i + 1) % len(gas)
        return res





class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


class Solution138:
    def copyRandomList(self, head: 'Node') -> 'Node':
        cache = dict()
        m = n = head

        while m:
            cache[m] = Node(m.val, m.next, m.random)
            m = m.next

        while n:
            cache[n].next = cache.get(n.next)
            cache[n].random = cache.get(n.random)
            n = n.next
        return cache.get(head)




class Solution042:
    def trap(self, height):

        left, right = 0, len(height) - 1
        leftMax, rightMax = 0, 0
        res = 0

        while left < right:
            if height[left] < height[right]:
                leftMax = max(height[left], leftMax)
                res += leftMax - height[left]
                left += 1

            else:
                rightMax = max(height[right], rightMax)
                res += rightMax - height[right]
                right -= 1

        return res


class Solution273:
    def __init__(self):
        self.lessThan20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven",
                           "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        self.tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        self.thousands = ["", "Thousand", "Million", "Billion"]

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'

        res = ""
        for i in range(len(self.thousands)):
            if num % 1000 != 0:
                res = self.helper(num % 1000) + self.thousands[i] + " " + res
            num //= 1000

        return res.strip()

    def helper(self, num):
        if num == 0:
            return ""
        elif num < 20:
            return self.lessThan20[num] + " "
        elif num < 100:
            return self.tens[num // 10] + " " + self.helper(num % 10)
        else:
            return self.lessThan20[num // 100] + " Hundred " + self.helper(num % 100)


# num = 45678345676543
# a = Solution273()
# print(a.numberToWords(num))
#


class Solution768_1:
    def maxChunksToSorted(self, arr) -> int:
        n = len(arr)
        maxOfLeft = [0] * n
        minOfRight = [0] * n

        maxOfLeft[0] = arr[0]
        for i in range(1, n):
            maxOfLeft[i] = max(maxOfLeft[i - 1], arr[i])

        minOfRight[n - 1] = arr[n - 1]
        for i in range(n - 2, -1, -1):
            minOfRight[i] = min(minOfRight[i + 1], arr[i])

        res = 0
        for i in range(n - 1):
            if maxOfLeft[i] <= minOfRight[i + 1]:
                res += 1

        return res + 1




class Solution768_2:
    def maxChunksToSorted(self, arr) -> int:

        res = 0

        counter1 = collections.Counter()
        counter2 = collections.Counter()

        for a, b in zip(arr, sorted(arr)):
            counter1[a] += 1
            counter2[b] += 1
            if counter1 == counter2:
                res += 1

        return res



class Solution909:
    def snakesAndLadders(self, board) -> int:
        n = len(board)
        visited = set()
        queue = collections.deque()
        queue.append((1, 0))
        while queue:
            spot, step = queue.popleft()
            i, j = self.convert(spot, n)
            if board[i][j] != -1:
                spot = board[i][j]
            if spot == n * n:
                return step
            for x in range(1, 7):
                newNode = spot + x
                if newNode <= n * n and newNode not in visited:
                    visited.add(newNode)
                    queue.append((newNode, step + 1))
        return -1


    def convert(self, node, n):
        row, col = divmod(node - 1, n)
        if row % 2 == 0:
            return n - 1 - row, col
        else:
            return n - 1 - row, n - 1 - col




class Solution557:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        for i in range(len(s)):
            s[i] = s[i][::-1]

        return " ".join(s)





class Solution443:
    def compress(self, chars):
        left = 0 # start replacing from left
        i = 0 # iterator
        while i < len(chars): #iterate through array
            char = chars[i] # current character
            count = 1 # current characters count
            while i+1 < len(chars) and char == chars[i+1]: # the last char
                count += 1 # increase current chars count
                i += 1  # increment pointer/iterator
            chars[left] = char # replace the character at poisition with current char
            if count > 1: # only replace if current char is seen more than once
                chars[left+1:left + 1 + len(str(count))] = str(count) # left to there = count = repeat count of current char
                left += len(str(count)) # if count > 10, replace it as "1", "0" so "there" value changes
            left += 1 # if no repetitions, move on to the next char
            i += 1 # incrementing the iterator
        return left




class Solution022:
    def generateParenthesis(self, n):
        res = []
        self.backtrack(n, n, "", res)
        return res

    def backtrack(self, left, right, path, res):
        if right < left:
            return
        if not right and not left:
            res.append(path)
        if left:
            self.backtrack(left - 1, right, path + '(', res)
        if right:
            self.backtrack(left, right - 1, path + ')', res)

from datetime import datetime

class Solution1185:
    def dayOfTheWeek(self, d, m, y):
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        print(datetime(y, m, d).weekday())
        return days[datetime(y, m, d).weekday()]

# d, m, y = 4, 7, 1993
# a = Solution1185()
# print(a.dayOfTheWeek(d, m, y))


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



def rand7():
    pass

class Solution470:
    def rand10(self):
        rand40 = 40
        while rand40 >= 40:
            rand40 = (rand7() - 1) * 7 + rand7() - 1
        return rand40 % 10 + 1



class Solution679:
    def judgePoint24(self, nums):
        n = len(nums)
        if n == 1 and abs(nums[0] - 24) < 0.001:
            return True
        for i in range(n):
            for j in range(n):
                if i != j:
                    newNums = [nums[k] for k in range(n) if k != i and k != j]
                    a, b = nums[i], nums[j]
                    if self.judgePoint24(newNums + [a + b]):
                        return True
                    if self.judgePoint24(newNums + [a * b]):
                        return True
                    if self.judgePoint24(newNums + [a - b]):
                        return True
                    if nums[j] != 0 and self.judgePoint24(newNums + [a / b]):
                        return True
        return False


import sys

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



class Solution001:
    def twoSum(self, nums, target):

        dic = dict()
        for i, val in enumerate(nums):
            if target - val in dic:
                return [dic[target - val], i]
            dic[val] = i








class Codec431:
    def encode(self, root: 'Node') -> TreeNode:
        if not root:
            return None

        res = TreeNode(root.val)
        if len(root.children) > 0:
            res.left = self.encode(root.children[0])

        cur = res.left
        for i in range(1, len(root.children)):
            cur.right = self.encode(root.children[i])
            cur = cur.right

        return res

    def decode(self, data: TreeNode) -> 'Node':
        if not data:
            return None

        res =Node(data.val, [])
        cur = data.left

        while cur:
            res.children.append(self.decode(cur))
            cur = cur.right

        return res



class Solution093:
    def restoreIpAddresses(self, s: str):
        res = []
        self.helper(res, s, 0, "", 0)
        return res

    def helper(self, res, s, index, path, count):
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
                self.helper(res, s, index + i, path + temp + "", count + 1)
            else:
                self.helper(res, s, index + i, path + temp + ".", count + 1)



class Solution1044:
    def longestDupSubstring(self, S):
        left, right = 0, len(S) - 1
        res = ''

        while left < right:
            mid = (left + right) // 2
            temp = self.check(mid, S)
            if not temp:
                right = mid
            else:
                left = mid + 1
                res = temp
        return res

    def check(self, num, S):
        visited = set()
        for i in range(len(S) - num + 1):
            if S[i:i+num] in visited:
                return S[i: i+num]
            visited.add(S[i: i+num])
        return None





class Solution206:
    def reverseList(self, head):
        prev = None
        curr = head

        while curr:
            newNode = curr.next
            curr.next = prev
            prev = curr
            curr = newNode

        return prev




class Solution103:
    def zigzagLevelOrder(self, root: TreeNode):
        if not root:
            return []

        res = []
        queue = collections.deque([root])
        reverse = False

        while queue:
            size, cur_level = len(queue), []

            for i in range(size):
                node = queue.popleft()
                # print(queue)
                if reverse:
                    # becuz we append from left to right, when reverse is True, we will need to insert 9, then insert 20 the the 0 position so 20 is at the left of 9
                    cur_level.insert(0, node.val)
                else:
                    cur_level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(cur_level)
            reverse = not reverse
        return res


import random
import string


class Codec535:
    def __init__(self):
        self.table = {}

    def encode(self, longUrl):
        # Get a set of characters that will make up the suffix
        mapping = string.ascii_letters + string.digits
        # Make a tinyurl template
        res = "http://tinyurl.com/".join(random.choice(mapping) for _ in range(6))
        # Store the pair in the dictionary
        self.table[res] = longUrl
        print(res)
        return res

    def decode(self, shortUrl):
        return self.table.get(shortUrl)




class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution445:
    def addTwoNumbers(self, l1, l2):
        if not l1.val:
            return l2
        if not l2.val:
            return l1

        stack1, stack2 = [], []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        head, val = ListNode(0), 0
        while stack1 or stack2:
            if stack1 and stack2:
                val = stack1.pop() + stack2.pop() + head.val
            else:
                n = max(stack1, stack2)  # None is smaller than anything
                val = n.pop() + head.val

            node = ListNode(val // 10)
            head.val = val % 10
            node.next = head
            head = node

        if head.val == 0:
            head = head.next
        return head






class Solution044_1:
    def isMatch(self, s, p):
        i = 0
        j = 0
        match = 0
        star = -1
        while i < len(s):
            ## first case compare ? or whether they are exactly the same
            if j < len(p) and (s[i] == p[j] or p[j] == '?'):
                i += 1
                j += 1
            ## if there is a * in p we mark current j and i
            elif j < len(p) and p[j] == '*':
                star = j
                j += 1
                match = i
            ## if current p[j] is not * we check whether prior state has *
            elif star != -1:
                j = star + 1
                match += 1
                i = match
            else:
                return False

        while j < len(p) and p[j] == '*':
            j += 1

        if j == len(p):
            return True
        return False


class Solution044_2:
    def isMatch(self, s: str, p: str) -> bool:

        dp = [[False for _ in range(len(p) + 1)] for i in range(len(s) + 1)]
        dp[0][0] = True
        for j in range(1, len(p) + 1):
            if p[j - 1] != '*':
                break
            dp[0][j] = True

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] in {s[i - 1], '?'}:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
        return dp[-1][-1]


import heapq

class Solution253:
    def minMeetingRooms(self, intervals):
        intervals.sort(key=lambda x: x[0])
        heap = []  # stores the end time of intervals
        for i in intervals:
            if heap and i[0] >= heapq.nsmallest(1, heap)[0]:
                # means two intervals can use the same room
                heapq.heapreplace(heap, i[1])
            else:
                # a new room is allocated
                heapq.heappush(heap, i[1])
        return len(heap)





class Solution033:
    def search(self, nums, target):

        return self.binarySearch(nums, target, 0, len(nums) - 1)

    def binarySearch(self, nums, target, start, end):
        if end < start:
            return -1
        mid = (start + end) // 2

        if nums[mid] == target:
            return mid

        if nums[start] <= target < nums[mid]:  # left side is sorted and has target
            return self.binarySearch(nums, target, start, mid - 1)

        elif nums[mid] < target <= nums[end]:  # right side is sorted and has target
            return self.binarySearch(nums, target, mid + 1, end)

        elif nums[mid] > nums[end]:  # right side is pivoted
            return self.binarySearch(nums, target, mid + 1, end)

        else:  # left side is pivoted
            return self.binarySearch(nums, target, start, mid - 1)

        return -1




class Solution240:
    def searchMatrix(self, matrix, target):

        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])

        i, j = m- 1, 0
        while i >= 0 and j < n:
            if matrix[i][j] == target:
                return True
            if matrix[i][j] < target:
                j += 1
            else:
                i -= 1
        return False







class Solution722:
    def removeComments(self, source):
        res, buffer, isOpen = [], '', False
        for line in source:
            i = 0
            while i < len(line):
                char = line[i]
                # "//" -> Line comment.
                if (i + 1) < len(line) and line[i:i + 2] == '//' and not isOpen:
                    break  # Advance pointer to end of current line.
                # "/*" -> Start of block comment.
                elif (i + 1) < len(line) and line[i:i + 2] == '/*' and not isOpen:
                    isOpen = True
                    i += 1
                # "*/" -> End of block comment.
                elif (i + 1) < len(line) and line[i:i + 2] == '*/' and isOpen:
                    isOpen = False
                    i += 1
                # Normal character. Append to buffer if not in block comment.
                elif not isOpen:
                    buffer += char
                i += 1
            if buffer and not isOpen:
                res.append(buffer)
                buffer = ''
        return res







