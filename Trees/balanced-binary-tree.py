class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def pre_order_traversal(self, node):
    #     if node is not None:
    #         left_height = self.pre_order_traversal(node.left)
    #         right_height = self.pre_order_traversal(node.right)
    #         height_diff = left_height - right_height
    #         if height_diff < -1 or height_diff > 1:
    #             raise(Exception)
    #         return 1 + max(left_height, right_height)
    #     return 0

    node_heights = {}

    def pre_order_traversal(self, node):
        stack = [node]
        self.node_heights = {None: 0}

        while stack:
            node = stack[-1]

            if node.left and node.left not in self.node_heights:
                stack.append(node.left)
            elif node.right and node.right not in self.node_heights:
                stack.append(node.right)
            else:
                node = stack.pop()
                print(f"node: {node.val if node else None}")
                leftHeight = self.node_heights[node.left]
                rightHeight = self.node_heights[node.right]
                height_diff = abs(leftHeight - rightHeight)
                if height_diff > 1:
                    return False
                self.node_heights[node] = 1 + max(leftHeight, rightHeight)
        return True

    def isBalanced(self, root: Optional[TreeNode]) -> int:
        # try:
        #     self.pre_order_traversal(root)
        # except (Exception):
        #     return False
        # return True
        return self.pre_order_traversal(root)


def to_binary_tree(items):
    if not items:
        return None

    it = iter(items)
    root = TreeNode(next(it))
    q = [root]
    for node in q:
        val = next(it, None)
        if val is not None:
            node.left = TreeNode(val)
            q.append(node.left)
        val = next(it, None)
        if val is not None:
            node.right = TreeNode(val)
            q.append(node.right)
    return root


root = to_binary_tree([1, 2, 3, 4, 5, 6, None, 8])
print(Solution().isBalanced(root))
#     1
#   2   3
#  4 5 6
# 8
