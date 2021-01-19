import functools

class Solution:
    def canMouseWin(self, grid, catJump: int, mouseJump: int) -> bool:
        m, n = len(grid), len(grid[0])
        valid = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != '#': valid += 1
                if grid[i][j] == 'F': food = (i, j)
                if grid[i][j] == 'C': cat = (i, j)
                if grid[i][j] == 'M': mouse = (i, j)

        @functools.lru_cache(None)
        def dfs(mouse, cat, turn):
            # print(mouse, cat)
            if mouse == cat or cat == food or turn > valid * 2:
                return False

            if mouse == food:
                return True

            # mouse turn
            if turn % 2 == 0:
                for nmouse in nextpos(mouse, turn):
                    # print(nmouse)
                    if dfs(nmouse, cat, turn + 1) == True:
                        return True
                return False

            # cat turn
            else:
                for ncat in nextpos(cat, turn):
                    if dfs(mouse, ncat, turn + 1) == False:
                        return False
                return True

        def nextpos(pos, turn):
            res = []
            # jump = mouseJump if turn % 2 == 0 else catJump
            jump = catJump if turn % 2 else mouseJump
            for dx, dy in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                for step in range(jump + 1):
                    x = pos[0] + step * dx
                    y = pos[1] + step * dy
                    # if x<0 or y<0 or x>=m or y>=n or grid[x][y] == '#':
                    #     continue
                    # res.append([x, y])
                    if 0 <= x < m and 0 <= y < n and grid[x][y] != '#':
                        res.append((x, y))
                    else:
                        break
            return res

        return dfs(mouse, cat, 0)



grid = ["####F","#C...","M...."]
catJump = 1
mouseJump = 2

a = Solution()
print(a.canMouseWin(grid, catJump, mouseJump))



