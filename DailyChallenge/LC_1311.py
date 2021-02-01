

"""
1311.Get-Watched-Videos-by-Your-Friends
假设某人是自己的好友的好友，同时也是自己的直接好友，那么只能记做是level为1的好友。因此此题注定用BFS的效率更高。

我们先用BFS找到level为k的好友，然后取出他们所看过的视频。再统计这些视频的观看次数。最后排序。

"""


import collections

class Solution:
    def watchedVideosByFriends(self, watchedVideos, friends, id: int, level: int):
        n = len(watchedVideos)
        visited = [0] * n
        visited[id] = 1
        queue = collections.deque()
        queue.append(id)
        persons = []
        step = 0
        while queue:
            size = len(queue)
            step += 1
            for _ in range(size):
                node = queue.popleft()
                for nei in friends[node]:
                    if visited[nei] == 1:
                        continue
                    visited[nei] = 1
                    queue.append(nei)
                    if step == level:
                        persons.append(nei)
            if step == level:
                break

        VideoSet = set()
        freq = collections.defaultdict(int)
        for person in persons:
            for v in watchedVideos[person]:
                VideoSet.add(v)
                freq[v] += 1

        temp = []
        for v in VideoSet:
            temp.append([freq[v], v])

        temp.sort()

        res = []
        for freq, video in temp:
            res.append(video)
        return res



