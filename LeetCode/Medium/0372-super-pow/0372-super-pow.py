class Solution:
    def superPow(self, a: int, b: list[int]) -> int:
        MOD = 1337
        res = 1
        a %= MOD

        
        for digit in b:
            res = (pow(res, 10, MOD) * pow(a, digit, MOD)) % MOD
        return res