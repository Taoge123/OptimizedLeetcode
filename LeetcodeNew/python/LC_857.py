
import heapq

class Solution:
    def mincostToHireWorkers(self, quality, wage, K):
        workers = sorted((w / q, q, w) for q, w in zip(quality, wage))

        res = float('inf')
        heap = []
        qualitySum = 0

        for ratio, quality, wage in workers:
            heapq.heappush(heap, -quality)
            qualitySum += quality

            if len(heap) > K:
                qualitySum += heapq.heappop(heap)

            if len(heap) == K:
                res = min(res, ratio * qualitySum)

        return float(res)



class SolutionTLE:
    def mincostToHireWorkers(self, quality, wage, K):
        res = float('inf')
        n = len(quality)
        for captain in range(n):
            # Must pay at least wage[captain] / quality[captain] per qual
            factor = wage[captain] / quality[captain]
            prices = []
            for worker in range(n):
                price = factor * quality[worker]
                if price < wage[worker]:
                    continue
                prices.append(price)

            if len(prices) < K:
                continue
            prices.sort()
            res = min(res, sum(prices[:K]))

        return float(res)




