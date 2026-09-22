class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        first_half = nums[:n]
        second_half = nums[n:]

        result = []
        for i in range(n):
            result.append(first_half[i])
            result.append(second_half[i])

        return result
