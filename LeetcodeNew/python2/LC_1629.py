class Solution:
    def slowestKey(self, releaseTimes, keysPressed: str) -> str:

        k = keysPressed[0]
        t = releaseTimes[0]

        for i in range(1, len(keysPressed)):
            time = releaseTimes[i] - releaseTimes[i - 1]
            if time > t or (time == t and keysPressed[i] > k):
                k = keysPressed[i]
                t = time
        return k




