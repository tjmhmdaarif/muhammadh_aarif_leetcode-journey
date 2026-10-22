class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        duplicate = -1
        missing = -1

        for num in nums:
            val = abs(num)
            if nums [val - 1] < 0:
                duplicate = val
            else:
                nums[val - 1] = -nums[val - 1]
        
        for i in range(len(nums)):
            if nums[i] > 0:
                missing = i + 1
                break
        return [duplicate, missing]