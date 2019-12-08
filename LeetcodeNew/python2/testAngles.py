

def solution(angles):
    # Type your solution here
    angles = list(angles)
    print(angles)

    stack = []
    i = 0
    while i < len(angles):
        if angles[i] == "<":
            stack.append("<")
        if not stack and angles[i] == '>':
            angles.insert(0, "<")
            i += 1
        if stack and angles[i] == '>':
            stack.pop()
        i += 1

    if len(stack) > 0:
        for i in range(len(stack)):
            angles.append(">")

    res = "".join(angles)
    return res





angles = "<<>>>>><<<>>"
print(solution(angles))




