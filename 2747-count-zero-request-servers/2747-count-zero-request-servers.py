class Solution(object):
    def countServers(self, n, logs, x, queries):
        '''
        arr = []
        for i in range(len(queries)):
            a = queries[i] - x
            b = queries[i]
            cnt = 0
            freq = set() 
            for j in range(len(logs)):
                if a <= logs[j][1] <= b:
                    freq.add(logs[j][0])
            cnt = len(freq)
            arr.append(n - cnt)
        return arr
        '''
        logs.sort(key=lambda a: a[1])

        q = sorted((queries[i], i) for i in range(len(queries)))

        arr = [0] * len(queries)

        freq = {}
        left = 0
        right = 0
        cnt = 0

        for time, idx in q:

            a = time - x
            b = time
            while right < len(logs) and logs[right][1] <= b:
                server = logs[right][0]

                freq[server] = freq.get(server, 0) + 1

                if freq[server] == 1:
                    cnt += 1

                right += 1

            # CHANGE: Remove logs whose time < a
            while left < right and logs[left][1] < a:
                server = logs[left][0]

                freq[server] -= 1

                if freq[server] == 0:
                    cnt -= 1

                left += 1

            arr[idx] = n - cnt

        return arr
        