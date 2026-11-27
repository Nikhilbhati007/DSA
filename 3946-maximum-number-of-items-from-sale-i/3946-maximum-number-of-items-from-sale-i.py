class Solution(object):
    def maximumSaleItems(self, items, budget):
        n = len(items)
        minPrice = min(price for factor, price in items)
        bonus = [0] * n

        for i in range(n):
            for j in range(n):
                if i != j and items[j][0] % items[i][0] == 0:
                    bonus[i] += 1
        dp = [-1] * (budget + 1)
        dp[0] = 0

        for i in range(n):
            factor, price = items[i]

            if price > budget:
                continue

            value = 1 + bonus[i]

            for c in range(budget, price - 1, -1):
                if dp[c - price] != -1:
                    dp[c] = max(dp[c], dp[c - price] + value)
        ans = 0

        for c in range(budget + 1):
            if dp[c] != -1:
                extra = (budget - c) // minPrice

                ans = max(ans, dp[c] + extra)

        return ans