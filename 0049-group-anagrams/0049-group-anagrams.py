class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        strs.sort()
        for st in strs:
            curr = [0] * 26
            for s in st:
                curr[ord(s)-ord('a')] += 1
            ans[tuple(curr)].append(st)
        return list(ans.values())        
