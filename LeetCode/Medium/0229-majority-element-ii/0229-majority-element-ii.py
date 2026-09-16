class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        seen = {}
        n = len(nums)
        threshold = n // 3

        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1

        result = []
        for num in seen :
            if seen[num] > threshold:
                result.append(num)
        
        return result