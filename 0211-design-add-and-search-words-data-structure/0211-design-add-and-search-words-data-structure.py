class WordDictionary:

    def __init__(self):
        self.tree = {}

    def addWord(self, word: str) -> None:
        node = self.tree
        for c in word:
            node = node.setdefault(c, {})
        node["#"] = True

    def search(self, word: str, node = None) -> bool:
        if not word:
            return "#" in node
        if node == None:
            node = self.tree
        newWord = word[1:]
        c = word[0]
        if c == ".":
            for key in list(node.keys()):
                if key == "#":
                    continue
                dfs = self.search(newWord, node[key])
                if dfs:
                    return True
        else:
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