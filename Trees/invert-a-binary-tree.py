from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Recursive DFS
    def in_order_traversal(self, node):
        if node is None:
            return
        self.in_order_traversal(node.left)
        temp = node.left
        node.left = node.right
        self.in_order_traversal(node.right)
        node.right = temp
    
    # Iterative DFS
    def in_order_traversal(self, node):
        if node is None:
            return
        stack = [root]
        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
    
    # BFS
    def in_order_traversal(self, node):
        if node is None:
            return
        
        # It is also possible to use a list as a queue. However, lists are not 
        # efficient for this purpose. While appends and pops from the end of 
        # list are fast, doing inserts or pops from the beginning of a list is 
        # slow (because all of the other elements have to be shifted by one).
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.in_order_traversal(root)
        return root

def build_tree_pre_order(nodes, f):
    val = next(nodes)
    if val == "x":
        return None
    left = build_tree_pre_order(nodes, f)
    right = build_tree_pre_order(nodes, f)
    return TreeNode(f(val), left, right)

root = build_tree_pre_order(iter("1 2 4 x x 5 x x 3 6 x x 7 x x".split()), int)
print(Solution().invertTree(root))