class TrieNode:
    def __init__(self, children=None, eow=False):
        self.children = {}
        self.is_end_of_word = False
        self.path = None


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        parent = self.root
        for char in word:
            if char in parent.children:
                curr = parent.children[char]
            else:
                curr = TrieNode()
                parent.children[char] = curr
            parent = curr
        curr.is_end_of_word = True
        curr.path = word


class Solution:
    seen = set()
    res = set()
    board = None

    # Recurive
    # def dfs(self, x, y, curr):
    #     char = self.board[x][y]
    #     if (x, y) in self.seen or char not in curr.children:
    #         return

    #     curr = curr.children[char]
    #     if curr.is_end_of_word:
    #         self.res.add(curr.path)
    #     if not curr.children:
    #         return

    #     self.seen.add((x, y))

    #     if x > 0:
    #         self.dfs(x - 1, y, curr)
    #     if x < len(self.board) - 1:
    #         self.dfs(x + 1, y, curr)
    #     if y > 0:
    #         self.dfs(x, y - 1, curr)
    #     if y < len(self.board[x]) - 1:
    #         self.dfs(x, y + 1, curr)

    #     self.seen.discard((x, y))

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.board = board
        self.seen = set()
        self.res = set()
        trie = Trie()
        for word in words:
            trie.insert(word)

        # for i in range(len(board)):
        #     for j in range(len(board[i])):
        #         self.dfs(i, j, trie.root)

        # Iterative
        for i in range(len(board)):
            for j in range(len(board[i])):
                cells = [(i, j, trie.root)]
                while len(cells) > 0:
                    cell = cells.pop()
                    x = cell[0]
                    y = cell[1]
                    curr = cell[2]
                    if curr is None:  # backtrack
                        self.seen.discard((x, y))
                        continue

                    char = board[x][y]
                    if (x, y) in self.seen or char not in curr.children:
                        continue
                    curr = curr.children[char]
                    if curr.is_end_of_word:
                        self.res.add(curr.path)
                    if not curr.children:
                        continue

                    self.seen.add((x, y))
                    cells.append((x, y, None))  # exit marker
                    # it will backtrack to here after exploring all surrounding
                    # cells that are pushed onto the stack after it
                    if x > 0:
                        cells.append((x - 1, y, curr))
                    if x < len(board) - 1:
                        cells.append((x + 1, y, curr))
                    if y > 0:
                        cells.append((x, y - 1, curr))
                    if y < len(board[x]) - 1:
                        cells.append((x, y + 1, curr))
        return list(self.res)


board = [
    ["o", "a", "a", "n"],
    ["e", "t", "a", "e"],
    ["i", "h", "k", "r"],
    ["i", "f", "l", "v"],
]
words = ["oath", "pea", "eat", "rain", "oaoa"]
print(Solution().findWords(board, words))
board = [
    ["o", "a", "a", "n"],
    ["e", "t", "a", "e"],
    ["i", "h", "k", "r"],
    ["i", "f", "l", "v"],
]
words = ["oath", "pea", "eat", "rain", "hklf", "hf"]
print(Solution().findWords(board, words))
