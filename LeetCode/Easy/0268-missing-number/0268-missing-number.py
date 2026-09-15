class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        full_range = set(range(len(nums) + 1 ))
        result = full_range - set(nums)
        return list(result)[0]
