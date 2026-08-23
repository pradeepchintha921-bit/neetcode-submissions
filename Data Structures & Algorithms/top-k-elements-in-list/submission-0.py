class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        # Count frequency of each number
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # Store [frequency, number]
        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])

        # Sort by frequency
        arr.sort()

        # Get top k frequent numbers
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])

        return res