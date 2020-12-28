
class Solution:
    def averageWaitingTime(self, customers) -> float:

        time = 0
        total = 0
        for customer in customers:

            time = max(time, customer[0])
            time += customer[1]
            total += (time - customer[0])

        return total / len(customers)


