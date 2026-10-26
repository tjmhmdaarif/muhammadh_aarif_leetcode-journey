class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        ans = prices.copy()
        stack = []

        for i, price in enumerate(prices):
            while stack and prices[stack[-1]] >= price:
                idx = stack.pop()
                ans [idx] -= price
            stack.append(i)

        return ans