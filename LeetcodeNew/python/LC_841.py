
class SolutionTony:
    def canVisitAllRooms(self, rooms):

        n = len(rooms)
        def dfs(node, visited):
            visited.add(node)
            for nei in rooms[node]:
                if nei not in visited:
                    dfs(nei, visited)

        visited = set()
        dfs(0, visited)
        return len(visited) == n



class Solution:
    def canVisitAllRooms(self, rooms) -> bool:
        visited = set()
        self.helper(rooms, 0, visited)
        return len(visited) == len(rooms)

    def helper(self, rooms, room, visited):
        visited.add(room)
        for nei in rooms[room]:
            if nei not in visited:
                self.helper(rooms, nei, visited)
        return



class Solution2:
    def canVisitAllRooms(self, rooms) -> bool:
        visited = set()
        visited.add(0)
        stack = []
        stack.append(0)

        while stack:
            node = stack.pop()
            for nei in rooms[node]:
                if nei not in visited:
                    visited.add(nei)
                    stack.append(nei)
        return len(visited) == len(rooms)




