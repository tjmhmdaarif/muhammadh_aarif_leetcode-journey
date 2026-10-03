class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ans = defaultdict(list)

        for s in strs:
            sorted_str = "".join(sorted(s))
            ans[sorted_str].append(s)
        
        return list(ans.values())