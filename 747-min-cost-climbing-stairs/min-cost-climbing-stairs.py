
class Solution:
    def minCostClimbingStairs(self, cost):
        a = 0
        b = 0

        for i in range(2, len(cost) + 1):
            c = min(a + cost[i - 2], b + cost[i - 1])
            a = b
            b = c

        return b
