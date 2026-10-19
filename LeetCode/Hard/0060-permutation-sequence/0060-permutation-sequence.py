class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fact = [1] * n
        for i in range (1,n):
            fact [i] = fact[i - 1] * i

        numbers =[str (i) for i in range (1, n + 1)]
        k -= 1

        result = []

        for i in range (n, 0, -1):

            block_size = fact[i - 1]
            idx = k // block_size
            result.append(numbers[idx])

            numbers.pop(idx)

            k %= block_size
        return "".join(result)