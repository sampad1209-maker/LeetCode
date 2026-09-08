class Solution:
    def relativeSortArray(self, arr1, arr2):
        freq = {}

        # Count frequency of elements in arr1
        for num in arr1:
            freq[num] = freq.get(num, 0) + 1

        result = []

        # Follow the order of arr2
        for num in arr2:
            if num in freq:
                result.extend([num] * freq[num])
                del freq[num]

        # Remaining elements in ascending order
        remaining = []

        for num, count in freq.items():
            remaining.extend([num] * count)

        remaining.sort()

        return result + remaining