class Solution(object):
    def maxWeight(self, pizzas):
        n = len(pizzas)
        weight_gain = 0
        pizzas.sort()
        total_days = n // 4
        odd_days = (total_days + 1) // 2
        even_days = total_days // 2
        r = n - 1
        for i in range(odd_days):
            weight_gain += pizzas[r]
            r -= 1
        for i in range(even_days):
            weight_gain += pizzas[r - 1]
            r -= 2
        return weight_gain