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

    def dfs(self, x, y, curr):
        char = self.board[x][y]
        if (x, y) in self.seen or char not in curr.children:
            return

        curr = curr.children[char]
        if curr.is_end_of_word:
            self.res.add(curr.path)

        if not curr.children:
            return
        self.seen.add((x, y))

        if x > 0:
            self.dfs(x - 1, y, curr)
        if x < len(self.board) - 1:
            self.dfs(x + 1, y, curr)
        if y > 0:
            self.dfs(x, y - 1, curr)
        if y < len(self.board[x]) - 1:
            self.dfs(x, y + 1, curr)

        self.seen.discard((x, y))

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.board = board
        self.seen = set()
        self.res = set()
        trie = Trie()
        for word in words:
            trie.insert(word)

        for i in range(len(board)):
            for j in range(len(board[i])):
                self.dfs(i, j, trie.root)

        # need to use recursive dfs
        # seen | {(x,y)} copies the whole set on every push
        # (O(t) per step), adding a t factor to time complexity
        # carrying seen set of size up to t → O(3^t · t) space
        # for i in range(len(board)):
        #     for j in range(len(board[i])):
        #         cells = [(i,j,set(),trie.root)]
        #         while len(cells) > 0:
        #             cell = cells.pop()
        #             x = cell[0]
        #             y = cell[1]
        #             seen = cell[2]
        #             curr = cell[3]
        #             if (not curr.children) or ((x,y) in seen):
        #                 continue
        #             char = board[x][y]
        #             if char in curr.children:
        #                 curr = curr.children[char]
        #                 if x > 0:
        #                     cells.append((x-1, y, seen | {(x,y)}, curr))
        #                 if x < len(board)-1:
        #                     cells.append((x+1, y , seen | {(x,y)}, curr))
        #                 if y > 0:
        #                     cells.append((x, y-1 , seen | {(x,y)}, curr))
        #                 if y < len(board[i])-1:
        #                     cells.append((x, y+1 , seen | {(x,y)}, curr))
        #             if curr.is_end_of_word:
        #                 res.add(curr.path)
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
