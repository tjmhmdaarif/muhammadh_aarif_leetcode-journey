class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            total = 0
            for digit_char in str(n):
                digit = int(digit_char)
                total += digit ** 2
            n = total
        return (n == 1)

