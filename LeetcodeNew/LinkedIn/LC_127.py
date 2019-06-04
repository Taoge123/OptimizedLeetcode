class Solution(object):
    def ladderLength(self, start, end, arr):
        arr = set(arr)  # avoid TLE
        q = collections.deque([(start, 1)])
        visted = set()
        alpha = string.ascii_lowercase  # 'abcd...z'
        while q:
            word, length = q.popleft()
            if word == end:
                return length

            for i in range(len(word)):
                for ch in alpha:
                    new_word = word[:i] + ch + word[i + 1:]
                    if new_word in arr and new_word not in visted:
                        q.append((new_word, length + 1))
                        visted.add(new_word)
        return 0


