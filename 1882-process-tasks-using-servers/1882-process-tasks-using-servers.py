import heapq

class Solution(object):
    def assignTasks(self, servers, tasks):

        n = len(servers)
        m = len(tasks)

        free = []
        busy = []

        ans = [0] * m

        # Initially, all servers are free
        for i in range(n):
            heapq.heappush(free, (servers[i], i))

        time = 0

        for j in range(m):

            # Current time cannot be earlier than task arrival
            time = max(time, j)

            # Move all available servers from busy to free
            while busy and busy[0][0] <= time:
                finish, weight, idx = heapq.heappop(busy)
                heapq.heappush(free, (weight, idx))

            # If no server is free, jump to the next available time
            if not free:
                time = busy[0][0]

                # Release all servers available at this time
                while busy and busy[0][0] <= time:
                    finish, weight, idx = heapq.heappop(busy)
                    heapq.heappush(free, (weight, idx))

            # Select the best available server
            weight, idx = heapq.heappop(free)

            ans[j] = idx

            # Assign the task and calculate when server becomes free
            finish_time = time + tasks[j]

            heapq.heappush(busy, (finish_time, weight, idx))

        return ans