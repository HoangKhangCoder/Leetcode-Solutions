class Trie:

    def __init__(self):
        self.words = []
        self.wordsSet = set()

    def insert(self, word: str) -> None:
        self.words.append(word)
        self.wordsSet.add(word)

    def search(self, word: str) -> bool:
        return word in self.wordsSet

    def startsWith(self, prefix: str) -> bool:
        for s in self.words:
            if s.startswith(prefix):
                return True
        return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)