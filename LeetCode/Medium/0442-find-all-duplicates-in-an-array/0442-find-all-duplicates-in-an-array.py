class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        duplicates = []

        for num in nums:
            val = abs(num)
            idx = val - 1

            if nums[idx] < 0:
                duplicates.append(val)
            else:
                nums[idx] = -nums[idx]

        return duplicates