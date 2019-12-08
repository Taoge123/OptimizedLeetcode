

def solution(parentheses, index):
    # Type your solution here
    stack = []
    for i in range(index, len(parentheses)):
        if parentheses[i] == "(":
            stack.append((parentheses[i], i))
        else:
            if not stack:
                return -1
            stack.pop()
            if not stack:
                return i

parentheses = "((()())())"
index = 2
print(solution(parentheses, index))


