class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    max_depth = 0
    # def in_order_traversal(self, node):
    #     if node is None:
    #         return
    #     self.in_order_traversal(node.left)
    #     temp = node.left
    #     node.left = node.right
    #     self.in_order_traversal(node.right)
    #     node.right = temp

    # Recursive DFS
    def pre_order_traversal(self, node, depth):
        if node is not None:
            depth += 1
            self.max_depth = max(depth, self.max_depth)
            self.pre_order_traversal(node.left, depth)
            self.pre_order_traversal(node.right, depth)
            depth -= 1

    # One line Solution
    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     if not root:
    #         return 0
    #     return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    # Iterative DFS
    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     stack = [[root, 1]]
    #     res = 0
    #     while stack:
    #         node, depth = stack.pop()
    #         if node:
    #             res = max(res, depth)
    #             stack.append([node.left, depth + 1])
    #             stack.append([node.right, depth + 1])
    #     return res

    # BFS
    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     q = deque()
    #     if root:
    #         q.append(root)

    #     level = 0
    #     while q:
    #         for i in range(len(q)):
    #             node = q.popleft()
    #             if node.left:
    #                 q.append(node.left)
    #             if node.right:
    #                 q.append(node.right)
    #         level += 1
    #     return level

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.pre_order_traversal(root, 0)
        return self.max_depth

    # def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    #     self.in_order_traversal(root)
    #     return root


def build_tree_pre_order(nodes, f):
    val = next(nodes)
    if val == "x":
        return None
    left = build_tree_pre_order(nodes, f)
    right = build_tree_pre_order(nodes, f)
    return TreeNode(f(val), left, right)


root = build_tree_pre_order(iter("1 2 4 x x 5 x x 3 6 x x 7 x x".split()), int)
print(Solution().maxDepth(root))
