class Excel(object):

    def __init__(self, H, W):
        self.height = H
        self.width = ord(W) - ord('A') + 2
        self.grid = [[0] * self.width for i in range(self.height+1)]
        self.formulas = {}

    def set(self, r, c, v):
        char = ord(c) - ord('A') + 1
        self.grid[r][char] = v
        if (r, char) in self.formulas:
            del self.formulas[(r, char)]

    def get(self, r, c):
        return self.process(r, c)


    def sum(self, r, c, strs):
        char = ord(c) - ord('A') + 1
        self.formulas[(r, char)] = strs
        return self.get(r, c)

    def process(self, r, c):
        total = 0
        c = ord(c) - ord('A') + 1
        if (r, c) not in self.formulas:
            return self.grid[r][c]

        formula = self.formulas[(r, c)]
        for fragment in formula:
            if ':' in fragment:
                start, end = fragment.split(':')
                start_row, start_col = int(start[1:]), ord(start[0])
                end_row, end_col = int(end[1:]), ord(end[0])
                for i in range(start_row, end_row+1):
                    for j in range(start_col, end_col+1):
                        total += self.get(i, chr(j))
            else:
                total += self.get(int(fragment[1]), fragment[0])
        return total