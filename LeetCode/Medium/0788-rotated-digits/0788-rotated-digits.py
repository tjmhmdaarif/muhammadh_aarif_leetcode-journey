class Solution:
    def rotatedDigits(self, n: int) -> int:
        good_count = 0
        invalid = {'3', '4', '7'}
        changing = {'2', '5','6', '9'}

        for x in range (1, n + 1):
            digits = set(str(x))

            if not (digits & invalid) and (digits & changing):
                good_count += 1

        return good_count