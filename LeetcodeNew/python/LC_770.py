
class Helper(collections.Counter):
    def __add__(self, other):
        self.update(other)
        return self

    def __sub__(self, other):
        self.update({k: -v for k, v in other.items()})
        return self

    def __mul__(self, other):
        ans = Helper()
        for k1, v1 in self.items():
            for k2, v2 in other.items():
                ans.update({tuple(sorted(k1 + k2)): v1 * v2})
        return ans

    def evaluate(self, evalmap):
        ans = Helper()
        for k, c in self.items():
            free = []
            for token in k:
                if token in evalmap:
                    c *= evalmap[token]
                else:
                    free.append(token)
            ans[tuple(free)] += c
        return ans

    def to_list(self):
        return ["*".join((str(v),) + k) for k, v in sorted(self.items(), key = lambda x: (-len(x[0]), x[0], x[1])) if v]

class Solution:
    def basicCalculatorIV(self, expression, evalvars, evalints):
        """
        :type expression: str
        :type evalvars: List[str]
        :type evalints: List[int]
        :rtype: List[str]
        """
        evaldict = dict(zip(evalvars, evalints))
        expr_pruned = self.prune(expression)
        expr_eval = expr_pruned.evaluate(evaldict)
        return expr_eval.to_list()

    def operation(self, sign, n1, n2):
        if sign == '+':
            return n1 + n2
        if sign == '-':
            return n1 - n2
        if sign == '*':
            return n1 * n2

    def make(self, expr):
        ans = Helper()
        if expr.isdigit():
            ans.update({(): int(expr)})
        else:
            ans[(expr,)] += 1
        return ans

    def prune(self, expr):
        stack, ops = [], []
        len_expr = len(expr)
        i = 0
        while i < len_expr:
            if expr[i] == '(':
                bal = 0
                for j in range(i, len_expr):
                    if expr[j] == '(':
                        bal += 1
                    elif expr[j] == ')':
                        bal -= 1
                    if bal == 0:
                        break
                stack.append(self.prune(expr[ i +1:j]))
                i = j
            elif expr[i].isalnum():
                flag = True
                for j in range(i, len_expr):
                    if expr[j] == ' ':
                        stack.append(self.make(expr[i:j]))
                        flag = False
                        break
                if flag:
                    stack.append(self.make(expr[i:]))
                i = j
            elif expr[i] in '+-*':
                ops.append(expr[i])
            i += 1

        return self.evaluation(stack, ops)


    def evaluation(self, stack, ops):
        for i in range(len(ops ) -1, -1, -1):
            if ops[i] == '*':
                sign, n1, n2 = ops.pop(i), stack[i], stack.pop( i +1)
                stack[i] = self.operation(sign, n1, n2)

        if not stack:
            return Helper()
        ans = stack[0]
        for i, sign in enumerate(ops, 1):
            ans = self.operation(sign, ans, stack[i])
        return ans
