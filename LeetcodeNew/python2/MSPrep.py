

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

# nums = [2,3,1,1,4]
# a = Solution045()
# print(a.jump(nums))


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




class Solution200:
    def numIslands(self, grid):
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        self.directions = [(-1, 0) ,(1, 0) ,(0, -1) ,(0, 1)]
        visited = [[False for i in range(n)] for j in range(m)]
        res = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1' and not visited[r][c]:
                    self.dfs(r, c, grid, m, n, visited)
                    res += 1

        return res

    def dfs(self, r, c, grid, m, n, visited):
        if r< 0 or c < 0 or r >= m or c >= n or grid[r][c] != '1' or visited[r][c]:
            return
        visited[r][c] = True
        for direction in self.directions:
            x, y = r + direction[0], c + direction[1]
            self.dfs(x, y, grid, m, n, visited)






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




class Solution107_2:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        queue = collections.deque([beginWord])
        another_queue = collections.deque([endWord])
        words, n, res = set(wordList), len(beginWord), 1
        if endWord not in words:
            return 0

        while queue:
            res += 1
            words -= set(queue)
            for _ in range(len(queue)):
                word = queue.popleft()
                for i in range(n):
                    for char in string.ascii_lowercase:
                        next_word = word[:i] + char + word[i + 1:]
                        if next_word in words:
                            if next_word in another_queue:
                                return res
                            queue.append(next_word)
            if len(queue) > len(another_queue):
                queue, another_queue = another_queue, queue

        return 0





class Solution126:
    def findLadders(self, beginWord: str, endWord: str, wordList):
        wordList = set(wordList)
        res = []
        layer = collections.defaultdict(list)
        layer[beginWord] = [[beginWord]]
        lowercase = string.ascii_lowercase

        while layer:
            newLayer = collections.defaultdict(list)
            for word in layer:
                if word == endWord:
                    for i in layer[word]:
                        res.append(i)
                else:
                    for i in range(len(word)):
                        for char in lowercase:
                            newWord = word[:i] + char + word[i+1:]
                            if newWord in wordList:
                                for valList in layer[word]:
                                    # print(newWord, valList + [newWord])
                                    newLayer[newWord].append(valList + [newWord])

            wordList -= set(newLayer.keys())
            layer = newLayer
        return res




class Solution235:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return

        if root.val > max(p.val, q.val):
            return self.lowestCommonAncestor(root.left, p, q)

        if root.val < min(p.val, q.val):
            return self.lowestCommonAncestor(root.right, p, q)

        return root




class Solution236:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        if not left:
            return right
        if not right:
            return left






class MyStack225:
    def __init__(self):
        self.stack = collections.deque([])

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        for i in range(len(self.stack) - 1):
            self.stack.append(self.stack.popleft())
        return self.stack.popleft()

    def top(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return not self.stack


"""
1-2-3-4-5
pop()
2-3-4-5-1
3-4-5-1-2
4-5-1-2-3
5-1-2-3-4
"""


class Solution025:
    def reverseKGroup(self, head, k):
        count, node = 0, head
        while node and count < k:
            node = node.next
            count += 1
        if count < k: return head
        new_head, prev = self.reverse(head, count)
        print(new_head.val, prev.val)
        head.next = self.reverseKGroup(new_head, k)
        return prev

    def reverse(self, head, count):
        prev, cur, nxt = None, head, head
        while count > 0:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            count -= 1
        return (cur, prev)


#
# head = ListNode(0)
# head.next = ListNode(1)
# head.next.next = ListNode(2)
# head.next.next.next = ListNode(3)
# head.next.next.next.next = ListNode(4)
# head.next.next.next.next.next = ListNode(5)
#
# a = Solution025()
# print(a.reverseKGroup(head, 3))

class Solution836:
    def isRectangleOverlap(self, rec1, rec2) -> bool:
        x1, y1, x2, y2 = rec1[0], rec1[1], rec1[2], rec1[3]
        x3, y3, x4, y4 = rec2[0], rec2[1], rec2[2], rec2[3]
        return (x1 < x4 and x3 < x2 and y1 < y4 and y3 < y2)



class Solution053:
    def maxSubArray(self, nums):
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
        return max(dp)



from heapq import *

class Solution218:
    def getSkyline(self, buildings):
        # 对于一个 building, 他由 (l, r, h) 三元组组成, 我们可以将其分解为两种事件:
        #     1. 在 left position, 高度从 0 增加到 h(并且这个高度将持续到 right position);
        #     2. 在 right position, 高度从 h 降低到 0.
        # 由此引出了 event 的结构: 在某一个 position p, 它引入了一个高度为 h 的 skyline, 将一直持续到另一 end postion

        # 对于在 right position 高度降为 0 的 event, 它的持续长度时无效的
        # 只保留一个 right position event, 就可以同时触发不同的两个 building 在同一 right position 从各自的 h 降为 0 的 event, 所以对 right
        # position events 做集合操作会减少计算量

        # 由于需要从左到右触发 event, 所以按 postion 对 events 进行排序
        # 并且, 对于同一 positon, 我们需要先触发更高 h 的事件, 先触发更高 h 的事件后, 那么高的 h 相比于低的 h 会占据更高的 skyline, 低 h 的 `key point` 就一定不会产生;
        # 相反, 可能会从低到高连续产生冗余的 `key point`
        # 所以, event 不仅需要按第一个元素 position 排序, 在 position 相同时, 第二个元素 h 也是必须有序的
        events = sorted([(l, -h, r) for l, r, h in buildings] + list({(r, 0, 0) for l, r, h in buildings}))

        # res 记录了 `key point` 的结果: [x, h]
        # 同时 res[-1] 处的 `key point` 代表了在下一个 event 触发之前, 一直保持的最高的 skyline

        # hp 记录了对于一条高为 h 的 skyline, 他将持续到什么 position 才结束: [h, endposition]
        # 在同时有多条 skyline 的时候, h 最高的那条 skyline 会掩盖 h 低的 skyline, 因此在 event 触发时, 需要得到当前最高的 skyline
        # 所以利用 heap 结构存储 hp, 它的第一个值永远为列表中的最小值: 因此在 event 中记录的是 -h, heap 结构就会返回最高的 skyline. 同时, h 必须在 endposition 之前,
        # 因为它按第一个元素排序
        res, record = [[0, 0]], [(0, float('inf'))]

        for l, neg_h, r in events:
            # 触发 event 时, 首先要做的就是清除已经到 endposition 的 skyline
            # hp: [h, endposition]
            # 如果当前 position 大于等于了 hp 中的 endposition, 那么该 skyline 会被清除掉
            # 由于在有 high skyline 的情况下, low skyline 不会有影响,
            # 因此, 只需要按从高到低的方式清除 skyline, 直到剩下一个最高的 skyline 并且它的
            # endposition 大于当前 position
            while l >= record[0][1]:
                heapq.heappop(record)

            # 对于高度增加到 h 的时间(neg_h < 0), 我们需要添加一个 skyline, 他将持续到 r 即 endposition
            if neg_h:
                heapq.heappush(record, (neg_h, r))

            # 由于 res[-1][1] 记录了在当前事件触发之前一直保持的 skyline
            # 如果当前事件触发后 skyline 发生了改变
            #     1. 来了一条新的高度大于 h 的 skyline
            #     2. res[-1] 中记录的 skyline 到达了 endposition
            # 这两种事件都会导致刚才持续的 skyline 与现在最高的 skyline 不同; 同时, `key point` 产生了, 他将被记录在 res 中
            if res[-1][1] != -record[0][0]:
                res.append([l, -record[0][0]])

        return res[1:]





class Solution068:
    def fullJustify(self, words, maxWidth: int):
        res = []
        index = 0

        while index < len(words):
            count = len(words[index])
            last = index + 1
            while last < len(words):
                if len(words[last]) + count + 1 > maxWidth:
                    break
                count += 1 + len(words[last])
                last += 1

            builder = []
            builder.append(words[index])
            diff = last - index - 1
            if last == len(words) or diff == 0:
                for i in range(index + 1, last):
                    builder.append(" ")
                    builder.append(words[i])
                start = sum(len(i) for i in builder)
                for i in range(start, maxWidth):
                    builder.append(" ")

            else:
                spaces = (maxWidth - count) // diff
                r = (maxWidth - count) % diff
                for i in range(index + 1, last):
                    for k in range(spaces, 0, -1):
                        builder.append(" ")

                    if r > 0:
                        builder.append(" ")
                        r -= 1
                    builder.append(" ")
                    builder.append(words[i])

            res.append("".join(builder))
            index = last

        return res


class Solution021:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        dummy = ListNode(0)
        curr = dummy
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        curr.next = l1 or l2
        return dummy.next




class Solution139:
    def wordBreak(self, s: str, wordDict):
        wordDict = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True

        return dp[-1]


class Solution540:
    def singleNonDuplicate(self, nums) -> int:
        start = 0
        end = len(nums) // 2
        while start < end:
            mid = (start + end) // 2
            if nums[2 * mid] != nums[2 * mid + 1]:
                end = mid
            else:
                start = mid + 1
        return nums[2 * start]

class Solution540_2:
    def singleNonDuplicate(self, nums) -> int:
        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            halves_are_even = (hi - mid) % 2 == 0
            if nums[mid + 1] == nums[mid]:
                if halves_are_even:
                    lo = mid + 2
                else:
                    hi = mid - 1
            elif nums[mid - 1] == nums[mid]:
                if halves_are_even:
                    hi = mid - 2
                else:
                    lo = mid + 1
            else:
                return nums[mid]
        return nums[lo]




class Solution105:
    def buildTree(self, preorder, inorder):
        if inorder:
            index = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[index])
            root.left = self.buildTree(preorder, inorder[:index])
            root.right = self.buildTree(preorder, inorder[index + 1:])
            return root



class Solution863:
    def distanceK(self, root, target, K):

        self.dfs(root, None)
        queue = collections.deque([(target, 0)])
        visited = {target}
        while queue:
            if queue[0][1] == K:
                return [node.val for node, dist in queue]
            node, dist = queue.popleft()
            for nei in (node.left, node.right, node.parent):
                if nei and nei not in visited:
                    visited.add(nei)
                    queue.append((nei, dist + 1))

        return []

    def dfs(self, node, parent):
        if node:
            node.parent = parent
            self.dfs(node.left, node)
            self.dfs(node.right, node)





class Solution023:
    def mergeKLists(self, lists):

        queue = []
        dummy = curr = ListNode(0)

        for i, item in enumerate(lists):
            if item:
                heapq.heappush(queue, (item.val, i, item))

        while queue:
            pos, node = heapq.heappop(queue)[1:]
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(queue, (node.next.val, pos, node.next))

        return dummy.next


#Same as next permutation
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




class Solution008:
    def myAtoi(self, s):

        if (len(s) == 0):
            return 0

        s = s.strip()    #去除空格

        if(s[0].isdigit()):         #首字符是数字
            sign = 1
        elif(s[0] == '+'):          #首字符是+-
            sign = 1
            s = s[1:]
        elif(s[0] == '-'):
            sign = -1
            s = s[1:]
        else:
            return 0

        l = len(s)
        val = 0;    i = 0
        while(i < l and s[i].isdigit()):
            val = val * 10 + eval(s[i])
            i += 1

        val = sign * val

        if(val > 2147483647):
            return 2147483647
        elif(val < -2147483648):
            return -2147483648
        else:
            return val



class Solution340:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        start, res = 0, 0
        table = collections.defaultdict(int)

        for i, char in enumerate(s):
            table[char] = i
            if len(table) > k:
                start = min(table.values())
                del table[s[start]]
                start += 1
            res = max(res, i - start + 1)
        return res




class Solution056:
    def merge(self, intervals):
        if len(intervals) == 0:
            return []

        intervals = sorted(intervals, key=lambda x: x.start)
        res = []
        res.append(intervals[0])
        for interval in intervals[1:]:
            #Basically if the new interval is less than last end, then we merge, else its a new interval
            if interval.start <= res[-1].end:
                res[-1].end = max(interval.end, res[-1].end)

            else:
                res.append(interval)

        return res




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




class Solution468:
    def validIPAddress(self, IP: str) -> str:
        def isIPv4(s):
            try:
                return str(int(s)) == s and 0 <= int(s) <= 255
            except:
                return False

        def isIPv6(s):
            if len(s) > 4:
                return False
            try:
                return int(s, 16) >= 0 and s[0] != '-'
            except:
                return False

        if IP.count(".") == 3 and all(isIPv4(i) for i in IP.split(".")):
            return "IPv4"
        if IP.count(":") == 7 and all(isIPv6(i) for i in IP.split(":")):
            return "IPv6"

        return "Neither"





class Solution099:
    def recoverTree(self, root: TreeNode) -> None:
        if not root:
            return

        self.prev, self.first, self.second = None, None, None
        self.helper(root)
        self.first.val, self.second.val = self.second.val, self.first.val,

    def helper(self, root):
        if not root:
            return

        self.helper(root.left)
        if self.prev and self.prev.val >= root.val:
            if not self.first:
                self.first = self.prev
            self.second = root
        self.prev = root
        self.helper(root.right)




class HitCounter362:
    def __init__(self):
        self.res = 0
        self.hits = collections.deque()

    def hit(self, timestamp: int) -> None:
        if not self.hits or self.hits[-1][0] != timestamp:
            self.hits.append([timestamp, 1])
        else:
            self.hits[-1][1] += 1
        self.res += 1

    def getHits(self, timestamp: int) -> int:
        while self.hits and self.hits[0][0] <= timestamp - 300:
            self.res -= self.hits.popleft()[1]
        return self.res




class Solution688_1:
    def knightProbability(self, N, K, r, c):
        dp = [[0] * N for _ in range(N)]
        dp[r][c] = 1
        for _ in range(K):
            temp = [[0] * N for _ in range(N)]
            for r, row in enumerate(dp):
                for c, val in enumerate(row):
                    for dr, dc in ((2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)):
                        if 0 <= r + dr < N and 0 <= c + dc < N:
                            temp[r+dr][c+dc] += val / 8.0
            dp = temp
        return sum(map(sum, dp))





class Solution688_2:
    def knightProbability(self, N, K, r, c):
        memo = {}
        return self.dfs(r, c, 1, 0, N, K, memo)

    def dfs(self, i, j, p, k, N, K, memo):
        if 0 <= i < N and 0 <= j < N and k < K:
            sm = 0
            for x, y in ((-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)):
                if (i + x, j + y, k) not in memo:
                    memo[(i + x, j + y, k)] = self.dfs(i + x, j + y, p / 8, k + 1, N, K, memo)
                sm += memo[(i + x, j + y, k)]
            return sm
        else:
            return 0 <= i < N and 0 <= j < N and p or 0




class Solution450:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None

        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if root.left and root.right:
                tmp = self.finMin(root.right)
                root.val = tmp.val
                root.right = self.deleteNode(root.right, tmp.val)
            else:
                if not root.left:
                    return root.right
                if not root.right:
                    return root.left
        return root

    def finMin(self, node):
        while node.left:
            node = node.left
        return node




class Solution135:
    def candy(self, ratings):

        res = len(ratings) * [1]

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[ i -1]:
                res[i] = res[i-1] + 1

        for i in range(len(ratings ) -1, 0, -1):
            if ratings[ i -1] > ratings[i]:
                res[i -1] = max(res[ i -1], res[i] + 1)

        return sum(res)


class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = collections.defaultdict(TrieNode)

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            node = node.children[char]
        node.isWord = True

class Solution212:
    def findWords(self, board, words):
        m, n = len(board), len(board[0])
        res = []
        trie = Trie()
        node = trie.root
        for word in words:
            trie.insert(word)

        for i in range(m):
            for j in range(n):
                self.dfs(board, words, node,  i, j, m, n, "", res)
        return res

    def dfs(self, board, words, node, i, j, m, n, path, res):

        if node.isWord:
            res.append(path)
            node.isWord = False

        if i< 0 or j < 0 or i >= m or j >= n:
            return
        node = node.children.get(board[i][j])
        if not node:
            return
        temp = board[i][j]
        board[i][j] = "#"
        self.dfs(board, words, node, i - 1, j, m, n, path + temp, res)
        self.dfs(board, words, node, i + 1, j, m, n, path + temp, res)
        self.dfs(board, words, node, i, j - 1, m, n, path + temp, res)
        self.dfs(board, words, node, i, j + 1, m, n, path + temp, res)
        board[i][j] = temp





class Codec428:
    def serialize(self, root: 'Node') -> str:
        res = []
        self.preorder(root, res)
        return "".join(res)

    def preorder(self, node, res):
        if not node:
            return
        res.append(str(node.val))
        for child in node.children:
            self.preorder(child, res)
        res.append("#")

    def deserialize(self, data: str) -> 'Node':
        if not data:
            return

        tokens = collections.deque(data.split())
        root = Node(int(tokens.popleft()), [])
        self.helper(root, tokens)
        return root

    def helper(self, node, tokens):
        if not tokens:
            return

        while tokens[0] != "#":
            value = tokens.popleft()
            child = Node(int(value), [])
            node.children.append(child)
            self.helper(child, tokens)
        tokens.popleft()



#
# class Solution179:
#     def largestNumber(self, nums):
#         nums = [str(num) for num in nums]
#         nums = sorted(nums, key=cmp_to_key(lambda x, y: int(y + x) - int(x + y)))
#
#         res = ''.join(nums).lstrip('0')
#         return res or '0'



class Solution116:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return

        queue = collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if node.left and node.right:
                node.left.next = node.right
                if node.next:
                    node.right.next = node.next.left

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root





class MinStack155:
    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append([x, x if not self.stack else min(x, self.getMin())])

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]



class Solution457:
    def circularArrayLoop(self, nums) -> bool:
        for i, num in enumerate(nums):
            if num == 0:
                continue
            slow = i
            fast = self.nextPos(i, nums)
            while nums[fast] * nums[i] > 0 and nums[self.nextPos(fast, nums)] * nums[i] > 0:
                if slow == fast:
                    # This will become self loop
                    if slow == self.nextPos(slow, nums):
                        break
                    return True
                slow = self.nextPos(slow, nums)
                fast = self.nextPos(self.nextPos(fast, nums), nums)

            slow = i
            while nums[slow] * num > 0:
                nxt = self.nextPos(slow, nums)
                nums[slow] = 0
                slow = nxt

        return False

    def nextPos(self, i, nums):
        length = len(nums)
        return (i + nums[i]) % length




class Solution076:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        left = 0
        minLen = float('inf')
        total = 0
        count = collections.Counter(t)
        for i, char in enumerate(s):
            count[char] -= 1
            if count[char] >= 0:
                total += 1
            while total == len(t):
                if minLen > i - left + 1:
                    minLen = i - left + 1
                    res = s[left: i + 1]
                count[s[left]] += 1
                if count[s[left]] > 0:
                    total -= 1
                left += 1
        return res




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

num = '123456321'
k = 3
a = Solution402()
print(a.removeKdigits(num, k))
import bisect

class Solution528:
    def __init__(self, w):
        for i in range(1, len(w)):
            w[i] += w[i - 1]
        self.w = w

    def pickIndex(self):
        seed = random.randint(1, self.w[-1])
        return bisect.bisect_left(self.w, seed)



class Solution046:
    def permute(self, nums):
        res = []
        self.backtrack(nums, [], res)
        return res

    def backtrack(self, nums, path, res):
        if not nums:
            res.append(path)

        for i in range(len(nums)):
            self.backtrack(nums[:i] + nums[i+1:], path + [nums[i]], res)




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




class MyCircularQueue622:
    def __init__(self, k):
        self.size = k
        self.curSize = 0
        self.head = self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.pre = self.head

    def enQueue(self, value):
        if self.curSize < self.size:
            node = Node(value)
            node.pre = self.tail.pre
            node.next = self.tail
            node.pre.next = node.next.pre = node
            self.curSize += 1
            return True
        return False

    def deQueue(self):
        if self.curSize > 0:
            node = self.head.next
            node.pre.next = node.next
            node.next.pre = node.pre
            self.curSize -= 1
            return True
        return False

    def Front(self):
        return self.head.next.val

    def Rear(self):
        return self.tail.pre.val

    def isEmpty(self):
        return self.curSize == 0

    def isFull(self):
        return self.curSize == self.size


class Solution969:
    def pancakeSort(self, A):
        res = []
        for x in range(len(A), 1, -1):
            i = A.index(x)
            res.extend([i+1, x])
            rightReverse = A[:i:-1]
            left = A[:i]
            print(left, rightReverse)
            # reversed(A[i+1:]) + A[:i], exclude k or A[i] after each iteration
            A = A[:i:-1] + A[:i]
            print(A)

        return res




class Solution572:
    def sameTree(self, tree1, tree2):

        if not (tree1 and tree2):
            return tree1 is tree2

        return (tree1.val == tree2.val
                and self.sameTree(tree1.left, tree2.left)
                and self.sameTree(tree1.right, tree2.right))

    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:

        if self.sameTree(s, t):
            return True
        if not s:
            return False
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)


class Solution384:
    def __init__(self, nums):
        self.nums = nums
        self.output = nums[:]

    def reset(self):
        self.output = self.nums[:]
        return self.nums

    def shuffle(self):
        n = len(self.output)
        for i in range(n):
            _id = random.randint(i, n - 1)
            self.output[i], self.output[_id] = self.output[_id], self.output[i]
        return self.output



class MovingAverage346:
    def __init__(self, size):

        self.queue = collections.deque(maxlen=size)

    def next(self, val):
        queue = self.queue
        queue.append(val)
        return float(sum(queue)) / len(queue)






class Solution322_2:
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



import collections

class Solution269:
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






class Solution004:
    def findMedianSortedArrays(self, nums1, nums2):
        l = len(nums1) + len(nums2)
        if l % 2 == 1:
            return self.kth(nums1, nums2, l // 2)
        else:
            return (self.kth(nums1, nums2, l // 2) + self.kth(nums1, nums2, l // 2 - 1)) / 2

    def kth(self, a, b, k):
        if not a:
            return b[k]

        if not b:
            return a[k]

        ia, ib = len(a) // 2, len(b) // 2
        ma, mb = a[ia], b[ib]
        #we wanna search on the right becuz the k is larger and we are searching the smallest k
        if ia + ib < k:
            if ma < mb:
                #since we search on the right, and a < b, then we remove a's left, else b's left
                return self.kth(a[ia + 1:], b, k - ia - 1)
            else:
                return self.kth(a, b[ib + 1:], k - ib - 1)
        else:
            #Now k is less than the search, then we will search on the left, then we delete the larger part since we search on the left
            if ma < mb:  # now k is <= middle number index
                return self.kth(a, b[:ib], k)
            else:
                return self.kth(a[:ia], b, k)





class Solution403:
    def canCross(self, stones):
        table = {}
        for stone in stones:
            table[stone] = set()
        table.get(0).add(0)

        for i in range(len(stones)):
            for k in table.get(stones[i]):
                for step in range(k - 1, k + 2):
                    if step > 0 and step + stones[i] in table:
                        table[step + stones[i]].add(step)

        return len(table[stones[-1]]) > 0



class Solution636:
    def exclusiveTime(self, n, logs):
        res = [0] * n
        stack = []
        prev = 0

        for log in logs:
            ID, typ, time = log.split(':')
            ID, time = int(ID), int(time)

            if typ == 'start':
                if stack:
                    res[stack[-1]] += time - prev
                stack.append(ID)
                prev = time
            else:
                res[stack.pop()] += time - prev + 1
                prev = time + 1

        return res



class Solution694:
    def numDistinctIslands(self, grid):
        steps = []
        distinctIslands = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    # 'o' for origin
                    self.dfs(grid, i, j, 'o', steps)
                    distinctIslands.add(''.join(steps))
                    steps = []
        print(distinctIslands)
        return len(distinctIslands)

    def dfs(self, grid, i, j, direct, steps):
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1:
            steps.append(direct)
            grid[i][j] = 0
            self.dfs(grid, i + 1, j, 'd', steps)  # down
            self.dfs(grid, i - 1, j, 'u', steps)  # upper
            self.dfs(grid, i, j + 1, 'r', steps)  # right
            self.dfs(grid, i, j - 1, 'l', steps)  # left
            steps.append('b')  # back



class Solution:
    def largestRectangleArea(self, heights):

        res = 0
        stack = [-1]
        heights.append(0)

        for i, height in enumerate(heights):
            while height < heights[stack[-1]]:
                high = heights[stack.pop()]
                width = i - stack[-1] - 1
                res = max(res, high * width)
            stack.append(i)
        return res



class Solution013:
    def romanToInt(self, s):
        map = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}

        result = 0
        for i in range(len(s)):
            if i > 0 and map[s[i]] > map[s[i - 1]]:
                result += map[s[i]]
                result -= 2 * map[s[i - 1]]
            else:
                result += map[s[i]]

        return result






class BSTIterator173:
    def __init__(self, root: TreeNode):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        node = self.stack.pop()
        next = node.right
        while next:
            self.stack.append(next)
            next = next.left
        return node.val

    def hasNext(self) -> bool:
        return self.stack



class Solution314:
    def verticalOrder(self, root: TreeNode):
        res = collections.defaultdict(list)
        queue = collections.deque([(root, 0)])

        while queue:
            node, pos = queue.popleft()
            if not node:
                continue
            res[pos].append(node.val)
            queue.append((node.left, pos - 1))
            queue.append((node.right, pos + 1))
        return [res[i] for i in sorted(res)]


class Solution322_1:
    def coinChange(self, coins, amount):
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for i in range(coin, amount + 1):
                if dp[i - coin] != float('inf'):
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return -1 if dp[amount] == float('inf') else dp[amount]



class Solution518:
    def change(self, amount: int, coins) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for j in range(1, amount + 1):
                if j >= coin:
                    dp[j] += dp[j - coin]

        return dp[amount]



class Solution315:
    def countSmaller(self, nums):
        arr = []
        res = []
        for num in nums[::-1]:
            idx = bisect.bisect_left(arr, num)
            res.append(idx)
            arr.insert(idx, num)
        return res[::-1]



class MyHashMap706:
    def __init__(self):
        self.numBuckets = 1000
        self.buckets = [-1] * self.numBuckets

    def put(self, key: int, value: int) -> None:
        index = key % self.numBuckets
        if self.buckets[index] == -1:
            self.buckets[index] = []

        for i, kvPair in enumerate(self.buckets[index]):
            if kvPair[0] == key:
                self.buckets[index][i] = (key, value)
                return

        self.buckets[index].append((key, value))


    def get(self, key: int) -> int:
        index = key % self.numBuckets
        if self.buckets[index] == -1:
            return -1

        for kvPair in self.buckets[index]:
            if kvPair[0] == key:
                return kvPair[1]
        return -1

    def remove(self, key: int) -> None:
        index = key % self.numBuckets
        indexToRemove = -1

        if self.buckets[index] == -1:
            return

        for i, kvPair in enumerate(self.buckets[index]):
            if kvPair[0] == key:
                indexToRemove = i
                break

        if indexToRemove == -1:
            return

        else:
            del self.buckets[index][indexToRemove]



class Solution785:
    def isBipartite(self, graph) -> bool:
        color = {}
        for i in range(len(graph)):
            if i not in color:
                color[i] = 0
                if not self.dfs(graph, color, i):
                    return False

        return True


    def dfs(self, graph, color, pos):
        for i in graph[pos]:
            if i in color:
                if color[i] == color[pos]:
                    return False
            else:
                color[i] = 1 - color[pos]
                if not self.dfs(graph, color, i):
                    return False
        return True




class Solution430:
    def flatten(self, head):
        if not head:
            return

        dummy = Node(0,None,head,None)
        stack = []
        stack.append(head)
        prev = dummy

        while stack:
            root = stack.pop()

            root.prev = prev
            prev.next = root

            if root.next:
                stack.append(root.next)
                root.next = None
            if root.child:
                stack.append(root.child)
                root.child = None
            prev = root

        dummy.next.prev = None
        return dummy.next



class Solution332:
    def findItinerary(self, tickets):

        graph = collections.defaultdict(list)
        for u, v in tickets:
            heapq.heappush(graph[u], v)
        start = 'JFK'
        res = []
        self.dfs(graph, start, res)
        return res[::-1]

    def dfs(self, graph, start, res):
        while graph[start]:
            node = heapq.heappop(graph[start])
            self.dfs(graph, node, res)
        res.append(start)



class Solution140:
    def wordBreak(self, s: str, wordDict):

        return self.helper(s, wordDict, {})

    def helper(self, s, wordDict, memo):
        if not s:
            return []
        if s in memo:
            return memo[s]

        res = []
        for word in wordDict:
            if not s.startswith(word):
                continue
            if len(word) == len(s):
                print(word)
                res.append(word)
            else:
                rest = self.helper(s[len(word):], wordDict, memo)
                for item in rest:
                    item = word + ' ' + item
                    print(item, '---')
                    res.append(item)
        memo[s] = res
        return res









