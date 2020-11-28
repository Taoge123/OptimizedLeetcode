import heapq
from sortedcontainers import SortedSet

class FileSharing:
    def __init__(self, m: int):
        self.table = {i: set() for i in range(1, m + 1)}
        self.heap = []
        self.own = {}

    def join(self, ownedChunks) -> int:
        if not self.heap:
            heapq.heappush(self.heap, len(self.own) + 1)
        cur = heapq.heappop(self.heap)
        for c in ownedChunks:
            self.table[c].add(cur)
        self.own[cur] = set(ownedChunks)
        return cur

    def leave(self, userID: int) -> None:
        heapq.heappush(self.heap, userID)
        for c in self.own[userID]:
            self.table[c].remove(userID)
        self.own[userID] = set()

    def request(self, userID: int, chunkID: int) -> List[int]:
        res = sorted(self.table[chunkID])
        if res:
            self.table[chunkID].add(userID)
            self.own[userID].add(chunkID)
        return res




class FileSharing2:
    def __init__(self, m: int):
        self.users = {}
        self.chunks = {}
        self.cur_id = 1
        self.used_ids = []
        heapq.heapify(self.used_ids)

    def join(self, ownedChunks) -> int:
        if len(self.used_ids) != 0:
            user_id = heapq.heappop(self.used_ids)
        else:
            user_id = self.cur_id
            self.cur_id += 1
        self.users[user_id] = ownedChunks
        for chuck in ownedChunks:
            if not chuck in self.chunks:
                self.chunks[chuck] = SortedSet()
            self.chunks[chuck].add(user_id)
        return user_id

    def leave(self, userID: int) -> None:
        for chunk in self.users[userID]:
            if chunk in self.chunks and userID in self.chunks[chunk]:
                self.chunks[chunk].remove(userID)
        del self.users[userID]
        heapq.heappush(self.used_ids, userID)

    def request(self, userID: int, chunkID: int):
        res = []
        if chunkID in self.chunks and len(self.chunks[chunkID]) > 0:
            res = list(self.chunks[chunkID])
            self.chunks[chunkID].add(userID)
            self.users[userID].append(chunkID)
        return res

