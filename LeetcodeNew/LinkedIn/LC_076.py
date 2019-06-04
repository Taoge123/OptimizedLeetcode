class Solution(object):
    def minWindow(self, s, t):
        if len(s) < len(t):
            return ""

        l, r = 0, 0
        c = collections.Counter(t)  # original counter
        w = collections.Counter()  # window   counter
        missing = len(t)  # number of characters missing from the window
        best = ""

        while True:
            # go right until we have all characters needed
            while missing:
                if r == len(s):
                    return best

                if s[r] in c:
                    w[s[r]] += 1
                    if w[s[r]] <= c[s[r]]:
                        missing -= 1
                r += 1

            # remove characters from the left until we don't have enough characters anymore
            while not missing:
                # skip the bullshit
                while s[l] not in c:
                    l += 1
                # compare to and save best solution
                if r - l < len(best) or not best:
                    best = s[l:r]
                w[s[l]] -= 1
                if w[s[l]] < c[s[l]]:
                    missing += 1
                l += 1

