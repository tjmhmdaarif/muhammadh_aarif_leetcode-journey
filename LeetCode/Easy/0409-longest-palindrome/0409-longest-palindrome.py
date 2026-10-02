class Solution:
    def longestPalindrome(self, s: str) -> int:
        ss = set()
        for char in s:
            if char in ss:
                ss.remove(char)
            else:
                ss.add(char)
            
        return len(s) - len(ss) + 1 if ss else len(s)