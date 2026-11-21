class Solution(object):
    def findSubtreeSizes(self, parent, s):
        n = len(parent)

        # Build the original tree
        children = [[] for _ in range(n)]

        for i in range(1, n):
            children[parent[i]].append(i)

        # Store the latest ancestor for each character
        last_seen = {}

        # Store the modified parent
        new_parent = parent[:]

        def dfs(node):
            ch = s[node]

            # Save previous occurrence
            previous = last_seen.get(ch, -1)

            # CHANGE: Find closest ancestor with same character
            if previous != -1:
                new_parent[node] = previous

            # Update latest occurrence
            last_seen[ch] = node

            # Process children
            for child in children[node]:
                dfs(child)

            # Backtrack to restore previous occurrence
            if previous == -1:
                del last_seen[ch]
            else:
                last_seen[ch] = previous

        dfs(0)

        # Build the modified tree
        new_children = [[] for _ in range(n)]

        for i in range(1, n):
            new_children[new_parent[i]].append(i)

        # Calculate subtree sizes
        answer = [1] * n

        def calculate(node):
            for child in new_children[node]:
                calculate(child)
                answer[node] += answer[child]

        calculate(0)

        return answer
            