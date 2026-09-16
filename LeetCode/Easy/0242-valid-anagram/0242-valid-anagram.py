class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str1 = sorted(s)
        str2 = sorted(t)
        if sorted(s) == sorted(t):
            return(True)
        else:
            return(False)