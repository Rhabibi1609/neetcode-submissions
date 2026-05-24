class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        res = sorted(counts.keys(), key=lambda x: counts[x], reverse=True)

        return res[:k]