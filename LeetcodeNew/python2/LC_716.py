class MaxStack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.insert(0, x)

    def pop(self):
        return self.stack.pop(0)

    def top(self):
        return self.stack[0]

    def peekMax(self):
        return max(self.stack)

    def popMax(self):
        res = max(self.stack)
        self.stack.remove(res)
        return res


class MaxStack2:
    def __init__(self):
        self.stack = []
        self.maxStack = []

    def push(self, x):
        self.stack.append(x)
        if len(self.maxStack) == 0:
            self.maxStack.append(x)
        elif self.maxStack[-1] > x:
            self.maxStack.append(self.maxStack[-1])
        else:
            self.maxStack.append(x)

    def pop(self):
        if len(self.stack) != 0:
            self.maxStack.pop()
            return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def peekMax(self):
        if len(self.maxStack) != 0:
            return self.maxStack[-1]

    def popMax(self):
        val = self.peekMax()
        buff = []
        while self.top() != val:
            buff.append(self.pop())
        self.pop()
        while len(buff) != 0:
            self.push(buff.pop())
        return val




