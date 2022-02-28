import collections
"""
1087.Brace-Expansion
因为此题明确没有nested的括号，所以简单的字符串处理就能AC。但是为了能扩展解决1096.Brace Expansion II，这里介绍一下更通用的栈的操作。

首先，为了保证每个字母都能触发入栈操作，我们将所有的字母都用括号包起来，注意到这样做并不改变原义。比如：{a,b}c{d,e}f变成{{a},{b}}{c}{{d},{e}}{f}

我们什么时候入栈？当遇到左括号和逗号的时候都需要。当然，为了区分这两个操作，我们需要两个栈stackOp和stackStr，分别来存放操作符（标记0或者1）和操作数（字符串数组）。
当退栈的时候，如果对应的stackOp栈顶是0，说明手头的元素curStr要与stackStr的栈顶元素做叉乘操作；
如果stackOp栈顶标记是1，说明手头的元素curStr要与stackStr的栈顶元素做并集操作。

有一个特别注意的地方：一旦启动退栈进程，如果stackOp栈顶有连续若干个1，那么这些并集操作要连续地进行。
原因是：连续被压入栈的这些逗号，本质肯定都是平级的，需要一并处理。如果stackOp栈顶是0，那么只需要再进行一次叉乘操作，这是因为叉乘的优先级较高，相邻之间能合并的早就已经合并完了。

"""


class SolutionRika:
    def expand(self, s: str):
        res = []
        self.dfs(s, 0, "", res)
        res = sorted(res)
        return res

    def dfs(self, s, i, path, res):

        if i >= len(s):
            res.append(path)
            return

        if s[i] == '{':
            end = s.find('}', i)
            for j in range(i + 1, end):
                if not s[j].isalpha():
                    continue
                self.dfs(s, end + 1, path + s[j], res)
        else:
            self.dfs(s, i + 1, path + s[i], res)




class SolutionTonnie:
    def expand(self, S: str):

        table = []
        start = None
        # 建一个list of list
        for ch in S:
            if ch == '{':
                start = True
                table.append([])
                continue
            if ch == '}':
                start = False
                continue

            if start:
                if ch == ',':
                    continue
                table[-1].append(ch)
            else:
                table.append(ch)

        n = len(table)
        def dfs(i, path, res):
            if i >= n:
                res.append(path)
                return

            # loop all chars if we see
            if isinstance(table[i], list):
                print(table[i])
                for ch in table[i]:
                    dfs(i + 1, path + ch, res)
            else:
                dfs(i + 1, path + table[i], res)

        res = []
        dfs(0, "", res)
        return sorted(res)




class Solution:
    def expand(self, S: str):
        queue = collections.deque([""])
        arr = S.replace('{', '}').split('}')
        arr = [char for char in arr if char]

        for chars in arr:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                for char in sorted(chars.split(",")):
                    if char.isalpha():
                        newNode = node + char
                        queue.append(newNode)
        return queue



S = "{a,b}c{d,e}f"
a = Solution()
print(a.expand(S))


