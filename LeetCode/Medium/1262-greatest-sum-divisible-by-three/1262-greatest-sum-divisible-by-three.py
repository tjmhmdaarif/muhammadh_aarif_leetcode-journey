class Solution:
    def maxSumDivThree(self, nums: list[int]) -> int:
        
        dp =[0, 0, 0]

        for num in nums:
            for s in dp[:]:
                new_sum = s + num
                dp[new_sum % 3] = max(dp[new_sum % 3], new_sum)

        return dp[0]