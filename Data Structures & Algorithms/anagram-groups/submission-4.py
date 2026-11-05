class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for s in strs:
            si = tuple(sorted(s))
            if si not in d:
                d[si] = []
            d[si].append(s)
        return list(d.values())