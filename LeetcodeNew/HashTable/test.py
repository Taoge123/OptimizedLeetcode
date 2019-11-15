class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        c = ord('l') - ord('a')
        res = ""
        cur = (0, 0)

        for char in target:
            realRow = (ord(char) - ord('a')) // len(board[0])
            realCol = (ord(char) - ord('a')) % len(board[0])

            diff1 = ord(char) - ord('a')
            diff2 = ord(board[cur[0]][cur[1]]) - ord('a')
            if diff2 - diff1 == 0:
                res += '!'
                continue
            row1 = diff1 // len(board[0])
            col1 = diff1 % len(board[0])

            row2 = diff2 // len(board[0])
            col2 = diff2 % len(board[0])

            rowDiff = row2 - row1
            colDiff = col2 - col1

            rowSign = 'U' if rowDiff >= 0 else 'D'
            colSign = 'L' if colDiff >= 0 else 'R'

            res += abs(rowDiff) * rowSign
            res += abs(colDiff) * colSign
            res += '!'

            wcur = (realRow, realCol)

        return res

a = Solution()

print(a.alphabetBoardPath('leet'))

