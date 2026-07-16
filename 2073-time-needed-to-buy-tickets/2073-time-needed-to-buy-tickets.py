class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        ans = 0
        x = tickets[k]

        for i in range(len(tickets)):
            if i <= k:
                ans += min(tickets[i], x)
            else:
                ans += min(tickets[i], x - 1)

        return ans