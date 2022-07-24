class SolutionTony:
    def differByOne(self, words) -> bool:
        n, m = len(words), len(words[0])
        table = [0] * n
        mod = 2 ** 64 - 1

        for i in range(n):
            for j in range(m):
                table[i] = (26 * table[i] + (ord(words[i][j]) - ord('a'))) % mod

        base = 1
        for j in range(m - 1, -1, -1):
            visited = set()
            for i in range(n):
                new_h = (table[i] - base * (ord(words[i][j]) - ord('a'))) % mod
                if new_h in visited:
                    return True
                visited.add(new_h)
            base = 26 * base % mod
        return False



