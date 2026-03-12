class TrieNode:
    def __init__(self, children = None, eow = False):
        self.children = {}
        self.is_end_of_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        parent = self.root
        for char in word:
            if char in parent.children:
                curr = parent.children[char]
            else:
                curr = TrieNode()
                parent.children[char] = curr                
            parent = curr
        curr.is_end_of_word = True

    def search(self, word: str) -> bool:   
        currNodes = [self.root]
        for char in word:
            newNodes = []
            match = False
            for curr in currNodes:
                # dots can be matched with any letter
                if char == ".":
                    newNodes.extend(list(curr.children.values()))
                    match = True
                elif char in curr.children:
                    newNodes.append(curr.children[char])   
                    match = True            
            if not match:
                return False
            currNodes = newNodes
        for curr in currNodes:
         if curr.is_end_of_word:
            return True
        return False

wordDictionary = WordDictionary()
print(wordDictionary.addWord("at"))
print(wordDictionary.addWord("and"))
print(wordDictionary.addWord("an"))
print(wordDictionary.addWord("add"))
print(wordDictionary.search("a"))
print(wordDictionary.search(".at"))
print(wordDictionary.addWord("bat"))
print(wordDictionary.search(".at"))
print(wordDictionary.search("an."))
print(wordDictionary.search("a.d."))
print(wordDictionary.search("b."))
print(wordDictionary.search("a.d"))
print(wordDictionary.search("."))
      