class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        for num in nums:
            val = abs(num)
            if nums[val - 1] > 0:
                nums[val - 1] = -nums[val - 1]

        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)

        return result