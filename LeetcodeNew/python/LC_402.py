
"""
解决原题的直观思路是寻找一个尽可能小的递增序列，但要满足位数的要求。

这是栈的典型应用。利用栈维护一个递增序列。当遍历的元素小于栈顶元素时，就不断退栈直至 Stack.top()<num[i]，这样继续加入元素后仍然是一个递增序列。

需要注意的几点：

需要一个计数器count来记录退栈的数目。只有当count<k时，才进行退栈操作（即模拟删除）。
都把所有元素都遍历结束后，如果发现仍然count<k，那么就把Stack末尾的弹出，直至count==k
需要去除结果里的前导零。

"""


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:

        stack = []
        if k >= len(num):
            return "0"

        for item in num:
            # we will pop when node decrease
            while stack and k and stack[-1] > item:
                stack.pop()
                k -= 1
            stack.append(item)
        # if we there are still k remains, we continue to pop
        while k:
            stack.pop()
            k -= 1
        return str(int("".join(stack)))




