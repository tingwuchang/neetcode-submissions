class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for s in strs:
            sort_s = "".join(sorted(s))
            if sort_s not in result:
                result[sort_s] = []
            result[sort_s].append(s)
        return list(result.values())
            

