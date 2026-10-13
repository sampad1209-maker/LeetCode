
class Solution:
    def countSmaller(self, nums):
        n = len(nums)
        counts = [0] * n
        values = sorted(set(nums))
        rank = {v: i + 1 for i, v in enumerate(values)}
        tree = [0] * (len(values) + 1)

        def query(i):
            total = 0
            while i > 0:
                total += tree[i]
                i -= i & -i
            return total

        def update(i):
            while i < len(tree):
                tree[i] += 1
                i += i & -i

        for i in range(n - 1, -1, -1):
            r = rank[nums[i]]
            counts[i] = query(r - 1)
            update(r)

        return counts
