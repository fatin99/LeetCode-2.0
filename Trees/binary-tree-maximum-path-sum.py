# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Recursive post-order traversal
    # O(n) time and O(h) space (recursion stack only)
    # def post_order_traversal(self, node: Optional[TreeNode]) -> int:
    #     if not node:
    #         return 0

    #     left_height = max(self.post_order_traversal(node.left), 0)
    #     right_height = max(self.post_order_traversal(node.right), 0)

    #     diameter = node.val + left_height + right_height
    #     if self.max_diameter == None:
    #         self.max_diameter = diameter
    #     self.max_diameter = max(diameter, self.max_diameter)

    #     return node.val + max(left_height, right_height)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # self.max_diameter = None
        # self.post_order_traversal(root)

        # Iterative post-order traversal
        # O(n) time and O(n) space for node_heights
        # O(h) space if we remove entries of child nodes
        stack = [root]
        max_diameter = None
        node_heights = {None: 0}
        while stack:
            node = stack[-1]

            if node.left and node.left not in node_heights:
                stack.append(node.left)
            elif node.right and node.right not in node_heights:
                stack.append(node.right)

            else:
                stack.pop()
                left_height = max(node_heights[node.left], 0)
                right_height = max(node_heights[node.right], 0)
                node_heights[node] = node.val + max(left_height, right_height)

                # children's heights are now consumed
                # we can free them to save space and get to O(h)
                if node.left:
                    del node_heights[node.left]
                if node.right:
                    del node_heights[node.right]

                diameter = node.val + left_height + right_height
                if max_diameter == None:
                    max_diameter = diameter
                max_diameter = max(diameter, max_diameter)

        return max_diameter


from collections import deque


def to_binary_tree(data):
    if not data:
        return None
    root = TreeNode(data[0])
    queue = deque([root])

    count = 0
    while queue and count < len(data):
        node = queue.popleft()
        for child in ("left", "right"):
            count += 1
            if count >= len(data):
                return root
            if data[count] is not None:
                child_node = TreeNode(data[count])
                setattr(node, child, child_node)
                queue.append(child_node)
    return root


root = to_binary_tree([1, 2, 3])
print(Solution().maxPathSum(root))
root = to_binary_tree([-10, 9, 20, None, None, 15, 7])
print(Solution().maxPathSum(root))
root = to_binary_tree([2, -1])
print(Solution().maxPathSum(root))
root = to_binary_tree([1, -2, 3])
print(Solution().maxPathSum(root))
root = to_binary_tree([9, 6, -3, None, None, -6, 2, None, None, 2, None, -6, -6, -6])
print(Solution().maxPathSum(root))
root = to_binary_tree([-2, 0, 0])
print(Solution().maxPathSum(root))
