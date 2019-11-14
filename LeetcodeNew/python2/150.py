class Solution:
    def evalRPN(self, tokens):

        stack = []
        for item in tokens:
            if item not in ["+", "-", "*", "/"]:
                stack.append(int(item))
            else:
                b, a = stack.pop(), stack.pop()
                if item == "+":
                    stack.append(a + b)
                elif item == "-":
                    stack.append(a - b)
                elif item == "*":
                    stack.append(a * b)
                elif item == "/":
                    stack.append(int(float(a) / b))
            print(stack)
        return stack.pop()




