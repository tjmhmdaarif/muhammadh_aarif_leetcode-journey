class Solution:
    def primePalindrome(self, n: int) -> int:
        if n <= 2:
            return 2
        if n <= 3:
            return 3
        if n <= 5:
            return 5
        if n <= 7:
            return 7
        if n <= 11:
            return 11

        def is_prime(x:int) -> bool:
            if x < 2 or x % 2 == 0:
                return x == 2
            for d in range(3, int(x**0.5)+ 1, 2):
                if x % d == 0:
                    return False
            return True


        for length in range (1, 6):
            start = 10 ** (length - 1)
            end = 10 ** length
            for root in range(start, end):
                s = str(root)

                candidate = int(s + s[-2:: -1])
                if candidate >= n and is_prime(candidate):
                    return candidate

        return -1