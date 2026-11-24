class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for s in nums:
            counts[s] += 1
        sorted_s = sorted(counts.items(), key=lambda pair:pair[1],reverse=True)

        return [p[0] for p in sorted_s[:k]]
         