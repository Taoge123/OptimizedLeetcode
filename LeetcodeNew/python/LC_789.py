
"""
target遇到鬼算输, 鬼可以直接去target等你,半路拦截不可能
"""


class Solution:
    def escapeGhosts(self, ghosts, target) -> bool:

        dis = abs(target[0]) + abs(target[1])
        for ghost in ghosts:
            d = abs(target[0 ] -ghost[0]) + abs(target[1 ] -ghost[1])
            if dis >= d:
                return False
        return True




