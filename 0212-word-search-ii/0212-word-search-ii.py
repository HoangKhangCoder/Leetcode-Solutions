class Trie:
    def __init__(self):
        self.root={}

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            node = node.setdefault(c, {})
        node['.']=True


    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c not in node:
                return False
            node = node[c]
        return '.' in node

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if c not in node:
                return False
            node = node[c]
        return True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows, cols = len(board), len(board[0])
        tree = Trie()
        for word in words:
            tree.insert(word)
        found = set()
        def helper(r, c, node, cur = ""):
            cur += board[r][c]
            temp, board[r][c] = board[r][c], "#"
            if "." in node:
                found.add(cur)
            for newR, newC in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if newR < 0 or newR >= rows or newC < 0 or newC >= cols or board[newR][newC] == "#" or board[newR][newC] not in node:
                    continue
                helper(newR, newC, node[board[newR][newC]], cur)
            board[r][c] = temp

        for r in range(rows):
            for c in range(cols):
                if board[r][c] in tree.root:
                    helper(r, c, tree.root[board[r][c]])
        return list(found)