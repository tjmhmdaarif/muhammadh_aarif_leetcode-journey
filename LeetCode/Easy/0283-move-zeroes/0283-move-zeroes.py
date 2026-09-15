class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        insert_pos = 0
        for i,num in enumerate(nums):
            if num != 0:
                nums[insert_pos] = num
                insert_pos += 1
        for j in range (insert_pos, len(nums)):
            nums[j] = 0
            
        
        