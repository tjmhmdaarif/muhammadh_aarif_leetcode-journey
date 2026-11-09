class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        nums_str = [str(num) for num in nums]

        def compare(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1
            elif n1 + n2 < n2 + n1:
                return 1
            else:
                return 0
        nums_str.sort (key=cmp_to_key(compare))

        if nums_str[0] == "0":
            return "0"

        return "".join(nums_str)