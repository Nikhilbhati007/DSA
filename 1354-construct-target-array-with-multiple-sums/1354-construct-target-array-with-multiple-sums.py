import heapq

class Solution(object):
    def isPossible(self, target):
        if len(target) == 1:
            return target[0] == 1

        total = sum(target)

        heap = [-x for x in target]
        heapq.heapify(heap)

        while True:
            mx = -heapq.heappop(heap)
            rest = total - mx

            if mx == 1 or rest == 1:
                return True

            if rest == 0 or rest >= mx:
                return False

            prev = mx % rest

            if prev == 0:
                return False

            total = rest + prev
            heapq.heappush(heap, -prev)