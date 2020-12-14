import collections


class FileSystem:

    def __init__(self):
        self.dirs = collections.defaultdict(list)
        self.files = collections.defaultdict(str)

    def ls(self, path: str):
        if path in self.files:
            return [path.split('/')[-1]]
        else:
            return sorted(self.dirs[path if len(path) > 1 else ""])

    def mkdir(self, path: str) -> None:
        dirs, cur = path.split("/")[1:], ""
        for d in dirs:
            if cur + '/' + d not in self.dirs:
                self.dirs[cur + '/' + d] = []
                self.dirs[cur].append(d)
            cur += '/' + d

    def addContentToFile(self, filePath: str, content: str) -> None:
        if filePath not in self.files: self.dirs[filePath[:-len(filePath.split('/')[-1]) -1]].append(
            filePath.split('/')[-1])
        self.files[filePath] += content

    def readContentFromFile(self, filePath: str) -> str:
        return self.files[filePath]


