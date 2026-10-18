class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        result = []
        for num in range(left, right + 1):
            is_self_driving = True

            for char in str (num):
                digit = int(char)

                if digit == 0 or num % digit  != 0:
                    is_self_driving = False
                    break
            if is_self_driving:
                result.append(num)
        return result