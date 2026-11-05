class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            d[i] = d.get(i,0) + 1
        n1 = list(d.values())
        d = sorted(d, key=d.get) [::-1]
        return d[:k]