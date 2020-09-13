"""
abc abc
1. each round, pick two letters of highest frequency
2. output 1 b, output as many a as possible
    a a b | a b | c a

"""

import heapq

"""
abc abc
1. each round, pick two letters of highest frequency
2. output 1 b, output as many a as possible
    a a b | a b | c a

"""


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        for count, char in (-a, 'a'), (-b, 'b'), (-c, 'c'):
            if count:
                heapq.heappush(heap, (count, char))
        res = []
        while heap:
            count, char = heapq.heappop(heap)
            if len(res) > 1 and res[-2] == res[-1] == char:
                if not heap:
                    break
                else:
                    # find the second frequent char
                    count, char = heapq.heapreplace(heap, (count, char))
            res.append(char)
            if count + 1:
                heapq.heappush(heap, (count + 1, char))
        return ''.join(res)



class Solution2:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        if a != 0:
            heapq.heappush(heap, (-a, 'a'))
        if b != 0:
            heapq.heappush(heap, (-b, 'b'))
        if c != 0:
            heapq.heappush(heap, (-c, 'c'))
        res = []
        while heap:
            first, char1 = heapq.heappop(heap)  # char with most rest numbers
            if len(res) >= 2 and res[-1] == res[-2] == char1:  # check whether this char is the same with previous two
                if not heap:  # if there is no other choice, just return
                    return ''.join(res)
                second, char2 = heapq.heappop(heap)  # char with second most rest numbers
                res.append(char2)
                second += 1  # count minus one, because the second here is negative, thus add 1
                if second != 0:  # only if there is rest number count, add it back to heap
                    heapq.heappush(heap, (second, char2))
                heapq.heappush(heap, (first, char1))  # also need to put this part back to heap
                continue

            #  situation that this char can be directly added to answer
            res.append(char1)
            first += 1
            if first != 0:
                heapq.heappush(heap, (first, char1))
        return ''.join(res)
