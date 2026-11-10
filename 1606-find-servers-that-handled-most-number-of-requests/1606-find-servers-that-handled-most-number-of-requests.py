import heapq

class Solution(object):
    def busiestServers(self, k, arrival, load):

        n = len(arrival)

        # Segment tree
        size = 1
        while size < k:
            size *= 2

        tree = [0] * (2 * size)

        # Initially, all servers are available
        for i in range(k):
            tree[size + i] = 1

        for i in range(size - 1, 0, -1):
            tree[i] = tree[2*i] + tree[2*i+1]

        # Update server availability
        def update(pos, val):
            pos += size
            tree[pos] = val

            pos //= 2

            while pos:
                tree[pos] = tree[2*pos] + tree[2*pos+1]
                pos //= 2

        # Find first available server in [ql, qr]
        def find(node, l, r, ql, qr):

            if r < ql or l > qr or tree[node] == 0:
                return -1

            if l == r:
                return l

            mid = (l + r) // 2

            ans = find(2*node, l, mid, ql, qr)

            if ans != -1:
                return ans

            return find(2*node+1, mid+1, r, ql, qr)

        # Busy servers: (completion time, server ID)
        busy = []

        # Number of requests handled by each server
        count = [0] * k

        for i in range(n):

            # Free completed servers
            while busy and busy[0][0] <= arrival[i]:

                end, server = heapq.heappop(busy)

                update(server, 1)

            start = i % k

            # Search from start to k-1
            server = find(1, 0, size-1, start, k-1)

            # Wrap around and search from 0
            if server == -1:
                server = find(1, 0, size-1, 0, start-1)

            # All servers are busy
            if server == -1:
                continue

            # Assign request
            count[server] += 1

            update(server, 0)

            heapq.heappush(
                busy,
                (arrival[i] + load[i], server)
            )

        # Find busiest servers
        maxi = max(count)

        return [i for i in range(k) if count[i] == maxi]