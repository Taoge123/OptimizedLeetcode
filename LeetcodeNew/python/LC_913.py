
"""
m,  c,  t  (t==1) status = cat win
m2, c2, t2 (t==2) status = cat win


                # mouse move and cat win
#                 if t==1 and status==2:
#                     color[m2][c2][t2] = 2
#                     queue.append([m2, c2, t2])

#                 elif t==2 and status==1:
#                     color[m2][c2][t2] = 1
#                     queue.append([m2, c2, t2])


"""


class Solution:
    def catMouseGame(self, graph):

        n = len(graph)
        color = [[[0] * 3 for _ in range(n)] for _ in range(n)]
        queue = collections.deque()
        for i in range(1, n):
            for t in range(1, 3):
                color[0][i][t] = 1
                queue.append((0 ,i ,t))
                color[i][i][t] = 2
                queue.append((i ,i ,t))

        while queue:
            curStatus = queue.popleft()
            cat, mouse, turn = curStatus

            for prevStatus in self.findAllPrevStatus(graph, curStatus):

                if color[prevStatus[0]][prevStatus[1]][prevStatus[2] ]! =0: continue

                # immediate win for prevStatus
                if color[cat][mouse][turn ]= = 3 -turn:
                    color[prevStatus[0]][prevStatus[1]][prevStatus[2]] = prevStatus[2]
                    queue.append(prevStatus)

                # forced to lose for prevStatus
                elif self.allNeighboursWin(color ,graph ,prevStatus):
                    color[prevStatus[0]][prevStatus[1]][prevStatus[2]] = 3- prevStatus[2]
                    queue.append(prevStatus)

        return color[1][2][1]

    def findAllPrevStatus(self, graph, curStatus):
        res = []
        mouse, cat, turn = curStatus
        if turn == 1:
            for prevCat in graph[cat]:
                if prevCat == 0: continue
                res.append((mouse, prevCat, 2))
        else:
            for prevMouse in graph[mouse]:
                res.append((prevMouse, cat, 1))
        return res

    def allNeighboursWin(self, color, graph, status):
        mouse, cat, turn = status
        if turn == 1:
            for nextMouse in graph[mouse]:
                if color[nextMouse][cat][2] != 2:
                    return False
        elif turn == 2:
            for nextCat in graph[cat]:
                if nextCat == 0: continue
                if color[mouse][nextCat][1] != 1:
                    return False
        return True





