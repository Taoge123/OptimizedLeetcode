"""
1096.Brace-Expansion-II
解法1：递归
我们先考虑一个乘法和加法的组合问题。例如计算a+b*c+b*d*e+f+g+h*u。

这是一个比较典型的用栈可以解决的问题。遇到所有的单项式（也就是发现被加号所分割），就把当前的变量cur推入栈中，并把cur重置为空。如果遇到的是多项式（也就是被乘号所分割），就新得到的这部分乘数next与手头的cur相乘并更新为cur。这样最终遍历完之后，栈里面是有若干个单项式，求它们的和就行了。

本题类似的思想，只不过把加号变成了逗号（对应的是取并集的运算），把乘号变成了双目的大括号（对应的是点乘的运算）。我们一旦遇到了左括号，就会向右寻找与它对应的右括号，这中间的部分就可以用递归处理（记作next）。默认情况下，我们都会将cur和next做点乘操作。

解法2：栈
如果不用递归，也可以强行只用栈处理。规则如下：

遇到逗号，就将当前的cur推入栈中，同时标记这个入栈的操作为1.然后将cur重置为空。
遇到左括号，就将当前的cur推入栈中，同时标记这个入栈的操作为2.然后将cur重置为空。
遇到右括号，就不停地将stack顶端连续标记为1操作的那些元素退栈，不停地与cur做并集操作。然后再将stack顶端标记为2操作的一个元素退栈，再与cur做点乘。得到的就是更新后的cur。（也就是说，遇到一个右括号，预示着要完成这个括号内的所有并集操作，再加上一次与这个括号之前元素的点乘操作）
遇到任何其他字母，就将cur的值置为这个字符串。
需要注意的是，我们最好对所有的字母提前包裹上"{}"，这样会带来处理上的便利。比如"{a,b}c{d,e}f"，因为c不包裹大括号的话，就无法判断它与前面是否是点乘的关系进而无法使之前的cur入栈。

"""


class Solution:
    def braceExpansionII(self, S: str):
        s = []
        for i in range(len(S)):
            if S[i].isalpha():
                s.append('{')
                s.append(S[i])
                s.append('}')
            else:
                s.append(S[i])
        stackStr = []
        stackOp = []
        cur = set()
        for i in range(len(s)):
            if s[i] == '{':
                stackStr.append(cur)
                stackOp.append(0)
                cur = set()
            elif s[i] == ',':
                stackStr.append(cur)
                stackOp.append(1)
                cur = set()
            elif s[i] == '}':
                while stackOp[-1] == 1:
                    cur = self.combine(stackStr.pop(), cur)
                    stackOp.pop()
                if stackOp[-1] == 0:
                    cur = self.crossProduct(stackStr.pop(), cur)
                    stackOp.pop()
            else:
                j = i + 1
                while j < len(s) and s[j].isalpha():
                    j += 1
                cur = {"".join(s[i:j])}
        print(cur)
        res = sorted(list(cur))
        return res

    def combine(self, s, t):
        res = set()
        for x in s:
            res.add(x)
        for y in t:
            res.add(y)
        return res

    def crossProduct(self, s, t):
        if not s:
            s.add("")

        if not t:
            t.add("")

        res = set()
        for x in list(s):
            for y in list(t):
                res.add(x + y)
        return res



