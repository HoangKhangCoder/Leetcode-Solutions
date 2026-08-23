class WordDictionary:
    # Idea: implement a Trie that supports searching with the wildcard
    # character '.' (matches any character). For a regular character, walk
    # straight down the corresponding branch; for '.', we must try every
    # child branch (DFS) since we don't know exactly which character it
    # represents.

    def __init__(self):
        self.tree = {}

    def addWord(self, word: str) -> None:
        node = self.tree
        for c in word:
            node = node.setdefault(c, {})
        node["#"] = True  # mark the end of a complete word

    def search(self, word: str, node=None) -> bool:
        if not word:
            return "#" in node
        if node is None:
            node = self.tree
        newWord = word[1:]
        c = word[0]
        if c == ".":
            # Wildcard: try matching every child branch (except the end-of-word marker key)
            for key in list(node.keys()):
                if key == "#":
                    continue
                dfs = self.search(newWord, node[key])
                if dfs:
                    return True
        else:
            # Regular character: only follow the matching branch if it exists
            if c not in node:
                return False
            dfs = self.search(newWord, node[c])
            if dfs:
                return True
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)