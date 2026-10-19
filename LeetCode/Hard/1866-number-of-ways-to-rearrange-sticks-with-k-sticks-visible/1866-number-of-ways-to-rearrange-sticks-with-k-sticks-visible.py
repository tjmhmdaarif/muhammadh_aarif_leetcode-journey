class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        
        # dp[j] stores ways to arrange current number of sticks with j visible
        dp = [0] * (k + 1)
        dp[1] = 1  # Base case for n = 1, k = 1
        
        for i in range(2, n + 1):
            # Iterate backwards to avoid overwriting values needed in the current row
            for j in range(min(i, k), 0, -1):
                dp[j] = (dp[j - 1] + (i - 1) * dp[j]) % MOD
                
        return dp[k]