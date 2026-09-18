class Solution:
    def shortestPalindrome(self, s: str) -> str:
        def is_palindrome(text):
            return text == text[::-1]

        for i in range(len(s),0, -1):
            if is_palindrome(s[:i]):
                to_add = s[i:]
                return to_add[::-1] + s
        
        return s