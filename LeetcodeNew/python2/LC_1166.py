
class FileSystem:
    def __init__(self):
        self.table = {}

    def createPath(self, path: str, value: int) -> bool:
        if path in self.table:
            return False
        if len(path) == 1:
            return False
        idx = len(path) - 1
        while path[idx] != '/':
            idx -= 1
        if idx == 0 or path[:idx] in self.table:
            self.table[path] = value
            return True
        return False

    def get(self, path: str) -> int:
        return self.table.get(path, -1)

