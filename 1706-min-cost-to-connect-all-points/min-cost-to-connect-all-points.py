
class Solution:
    def minCostConnectPoints(self, points):
        n = len(points)
        visited = set()
        min_cost = 0
        edges = [(0, 0)]

        while len(visited) < n:
            cost, i = heapq.heappop(edges)

            if i in visited:
                continue

            visited.add(i)
            min_cost += cost

            for j in range(n):
                if j not in visited:
                    x1, y1 = points[i]
                    x2, y2 = points[j]

                    distance = abs(x1 - x2) + abs(y1 - y2)
                    heapq.heappush(edges, (distance, j))

        return min_cost
