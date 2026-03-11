# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # def pre_order_traversal(self, root, child):
    #     if root is None:
    #         return []
    #     stack = [(root, [])]  # (node, path_so_far)
    #     while stack:
    #         node, path = stack.pop()
    #         if node == child:
    #             path.append(child)
    #             return path
    #         # Go right and left, add current node to path
    #         if node.right:
    #             stack.append((node.right, path + [node]))
    #         if node.left:
    #             stack.append((node.left, path + [node]))
    #     return []

    # def pre_order_traversal(self, root, child):
        # res = []
        # stack = [(root, [str(root.val)])]

        # while stack:
        #     node, path = stack.pop()

        #     # leaf node
        #     if not any(node.children):
        #         res.append("->".join(path))
        #         continue

        #     for child in node.children:
        #         if child:
        #             stack.append((child, path + [str(child.val)]))

        # return res

    # def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    #     path_p = self.pre_order_traversal(root, p)
    #     path_q = self.pre_order_traversal(root, q)
        
    #     length = min(len(path_p), len(path_q))
    #     curr = None
    #     for i in range(length):
    #         if path_p[i] == path_q[i]:
    #             curr = path_q[i]
    #         else:
    #             return curr
    #     return curr
        

    # def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    #     stack = [(root, [])]  # (node, path_so_far)
    #     seen = False
        
    #     while stack:
    #         node, path = stack.pop()
    #         if node == p or node == q:
                
    #             if seen: 
    #                 path.append(node)
    #                 second_path = path
                    
    #                 curr = None
    #                 for i in range(min(len(first_path), len(second_path))):
    #                     if first_path[i] == second_path[i]:
    #                         curr = first_path[i]
    #                     else:
    #                         return curr
    #                 return curr
                
    #             seen = True
    #             path.append(node)
    #             first_path = path
            
    #         # Go right and left, add current node to path
    #         if node.right:
    #             stack.append((node.right, path + [node]))
    #         if node.left:
    #             stack.append((node.left, path + [node]))

    # If p and q are both greater than the current node -> move right.
    # If p and q are both smaller -> move left.
    # If they split (one on each side) or one equals the current node ->
    # current node is the LCA, because it's the first node where their paths diverge.

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = [(root, [])]  # (node, path_so_far)        
        while stack:
            node, path = stack.pop()
            if p.val > node.val and q.val > node.val:
                if node.right:
                    stack.append((node.right, path + [node]))
            if p.val < node.val and q.val < node.val:
                if node.left:
                    stack.append((node.left, path + [node]))
            if (p.val >= node.val and q.val <= node.val) or (p.val <= node.val and q.val >= node.val):
                return node
        return root

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

root = to_binary_tree([6,2,8,0,4,7,9,None,None,3,5])
print(Solution().lowestCommonAncestor(root, 2, 8))

root = to_binary_tree([6,2,8,0,4,7,9,None,None,3,5])
print(Solution().lowestCommonAncestor(root, 2, 4))


root = to_binary_tree([2, 1])
print(Solution().lowestCommonAncestor(root, 2, 1))

root = to_binary_tree([3,1,4,None,2])
print(Solution().lowestCommonAncestor(root, 2, 4))