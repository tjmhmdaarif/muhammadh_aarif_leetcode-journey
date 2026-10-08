class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        def backtrack(start: int,current_comb: list[int], current_sum: int):
            if current_sum == target:
                res.append(list(current_comb))
                return
            if current_sum > target:
                return

            for i in range(start, len(candidates)):
                current_comb.append(candidates[i])
                backtrack(i, current_comb, current_sum + candidates[i])
                current_comb.pop()

        backtrack(0, [], 0)
        return res