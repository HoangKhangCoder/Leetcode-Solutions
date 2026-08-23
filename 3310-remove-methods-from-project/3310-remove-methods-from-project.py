class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        # Step 1: Build a directed graph where edge u -> v means function u
        # calls function v.
        graph = [[] for _ in range(n)]
        for u, v in invocations:
            graph[u].append(v)

        # Step 2: DFS from the suspicious function (k) to find every function
        # that is "infected" (called directly or indirectly from k) — this is
        # the set of functions intended for removal.
        infected = set()

        def dfs(current):
            infected.add(current)
            for nextNode in graph[current]:
                if nextNode in infected:
                    continue
                dfs(nextNode)

        dfs(k)

        # Step 3: Check safety — if a function that is NOT infected calls a
        # function that IS infected, removing the infected set would break
        # the program's behavior, so we must keep everything (remove nothing).
        for u, v in invocations:
            if u not in infected and v in infected:
                return [i for i in range(n)]

        # Step 4: Safe to remove — return the remaining functions (those not in the infected set)
        return [i for i in range(n) if i not in infected]
