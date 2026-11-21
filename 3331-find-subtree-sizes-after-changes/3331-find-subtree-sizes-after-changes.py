class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        ch = [[] for _ in range(n)]
        for i in range(1, n):
            ch[parent[i]].append(i)
        b = s.encode()
        last = [-1] * 123
        last[b[0]] = 0
        size = [1] * n
        np = parent[:]
        save = [0] * n
        stack = ch[0][:]
        while stack:
            x = stack.pop()
            if x < 0:
                x = ~x
                last[b[x]] = save[x]
                size[np[x]] += size[x]
                continue
            c = b[x]
            p = last[c]
            if p < 0:
                p = parent[x]
            kids = ch[x]
            if kids:
                np[x] = p
                save[x] = last[c]
                last[c] = x
                stack.append(~x)
                stack += kids
            else:
                size[p] += 1
        return size