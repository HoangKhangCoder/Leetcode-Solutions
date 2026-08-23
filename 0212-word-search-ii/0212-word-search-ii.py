class Trie:
    # Idea: merge all the words we're searching for into a single shared
    # Trie, so that when we DFS over the board we can search for multiple
    # words at once instead of searching for each word separately (this
    # avoids repeating the board traversal work).
    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            node = node.setdefault(c, {})
        node['.'] = True  # mark the end of a complete word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Idea: build a Trie containing the entire list of words to search
        # for, then DFS/backtrack from every cell on the board, following
        # only the branches that still exist in the Trie. Mark the cell
        # being visited with "#" to avoid reusing the same cell within one
        # path, then restore it after backtracking.
        rows, cols = len(board), len(board[0])
        tree = Trie()
        for word in words:
            tree.insert(word)
        found = set()

        def helper(r, c, node, currentWord=""):
            currentWord += board[r][c]
            savedChar, board[r][c] = board[r][c], "#"  # mark the cell as used to avoid revisiting it
            if "." in node:
                found.add(currentWord)
            for newR, newC in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if (newR < 0 or newR >= rows or newC < 0 or newC >= cols
                        or board[newR][newC] == "#" or board[newR][newC] not in node):
                    continue
                helper(newR, newC, node[board[newR][newC]], currentWord)
            board[r][c] = savedChar  # backtrack: restore the cell's original value

        for r in range(rows):
            for c in range(cols):
                if board[r][c] in tree.root:
                    helper(r, c, tree.root[board[r][c]])
        return list(found)