

# brute-force solution
def findCelebrity(self, n):
    for i in xrange(n):
        tmp = range(i) + range(i+1, n)
        ind = 0
        while ind < len(tmp) and not knows(i, tmp[ind]) and knows(tmp[ind], i):
            ind += 1
        if ind == len(tmp):
            return i
    return -1

# In first iteration, we start with 0 and iterate if it is a proper candidate till the end or update candidate.
# In second iteration, we go back to previous indexes to check if candidate is in celebrity position for all left and right indexes.

class Solution(object):
    def findCelebrity(self, n):
        i = 0
        while i < n:
            person = i
            i += 1
            while i < n and not knows(person, i) and knows(i, person):
                i += 1
        j = person - 1
        while j >= 0 and not knows(person, j) and knows(j, person):
            j -= 1
        return person if j < 0 else -1



