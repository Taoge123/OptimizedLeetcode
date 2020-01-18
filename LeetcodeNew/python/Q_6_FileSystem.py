from typing import List
class FileSystem:
    def __init__(self):
        self.paths = {'': 0}

    def createPath(self, path: str, value: int) -> bool:
        if '/'.join(path.split('/')[:-1]) not in self.paths or path in self.paths:
            return False
        self.paths[path] = value
        return True

    def get(self, path: str) -> int:
        return self.paths.get(path, -1)


class TrieNode:
    def __init__(self):
        self.children = {}
        self.content = ''
        self.isfile = False


class FileSystem:
    def __init__(self):
        self.root = TrieNode()

    def ls(self, path: str) -> List[str]:
        node = self.root
        splited_path = path.split('/')
        if path.endswith('/'):
            splited_path = splited_path[:-1]
        for p in splited_path:
            if p not in node.children:
                return []
            node = node.children[p]
        if node.isfile:
            return [p]
        return sorted(node.children.keys())

    def mkdir(self, path: str) -> None:
        node = self.root
        splited_path = path.split('/')
        for p in splited_path:
            if p not in node.children:
                node.children[p] = TrieNode()
            node = node.children[p]
        return

    def addContentToFile(self, filePath: str, content: str) -> None:
        node = self.root
        splited_path = filePath.split('/')
        for p in splited_path:
            if p not in node.children:
                node.children[p] = TrieNode()
            node = node.children[p]
        node.isfile = True
        node.content += content
        return

    def readContentFromFile(self, filePath: str) -> str:
        node = self.root
        splited_path = filePath.split('/')
        for p in splited_path:
            if p not in node.children:
                return ''
            node = node.children[p]

        return node.content


        # Your FileSystem object will be instantiated and called as such:
        # obj = FileSystem()
        # param_1 = obj.ls(path)
        # obj.mkdir(path)
        # obj.addContentToFile(filePath,content)
        # param_4 = obj.readContentFromFile(filePath)