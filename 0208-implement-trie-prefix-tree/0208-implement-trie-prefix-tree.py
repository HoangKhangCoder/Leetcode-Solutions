class Trie:
    # Idea: implement a Trie using nested dicts. Each node is a dict
    # mapping character -> child node. When a word ends, mark it with the
    # special key 'end' in that node to distinguish "end of a word" from
    # "just a prefix of another word".

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            node = node.setdefault(c, {})  # create the child node if it doesn't exist yet
        node['end'] = True  # mark the end of a complete word

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c not in node:
                return False
            node = node[c]
        return 'end' in node  # must be a complete word, not just a prefix

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if c not in node:
                return False
            node = node[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)