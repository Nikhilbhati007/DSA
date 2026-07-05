class Solution(object):
    def finalPrices(self, prices):
        n = len(prices)
        res = []

        for i in range(n - 1):
            j = i + 1

            while j < n and prices[i] < prices[j]:
                j += 1

            if j == n:
                res.append(prices[i])
            else:
                res.append(prices[i] - prices[j])

        res.append(prices[-1])

        return res