class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted(s)
        sorted(t)
        if sorted(s) == sorted(t):
            return(True)
        else:
            return(False)