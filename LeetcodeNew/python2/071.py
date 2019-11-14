
class Solution:
    def simplifyPath(self, path: str) -> str:

        path = path.split("/")
        stack = []
        for item in path:
            if item not in ["", "..", "."]:
                stack.append(item)
            elif item == ".." and stack:
                stack.pop()
        return "/" + "/".join(stack)






