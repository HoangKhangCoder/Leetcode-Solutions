class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for u, v in invocations:
            graph[u].append(v)

        sick = set()

        def dfs(cur):
            sick.add(cur)
            for nextVal in graph[cur]:
                if nextVal in sick:
                    continue
                dfs(nextVal)
        
        dfs(k)
        for u, v in invocations:
            if u not in sick and v in sick:
                return [i for i in range(n)]
        return [i for i in range(n) if i not in sick]