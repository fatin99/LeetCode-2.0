class TrieNode:
    def __init__(self, children = None, eow = False):
        self.children = {}
        self.is_end_of_word = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        parent = self.root
        for i in range(len(word)):
            curr = TrieNode()
            if word[i] in parent.children:
                curr = parent.children[word[i]]
            else:
                parent.children[word[i]] = curr
            if i == len(word) - 1:
                curr.is_end_of_word = True
            parent = curr

    def search(self, word: str) -> bool:
        curr = self.root
        for i in range(len(word)):
            if word[i] in curr.children:
                curr = curr.children[word[i]]
                if i == len(word) - 1:
                    return curr.is_end_of_word
            else:
                return False
        return True
        
    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for i in range(len(prefix)):
            if prefix[i] in curr.children:
                curr = curr.children[prefix[i]]
            else:
                return False
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)