class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution:
    # def isValidBST(self, root: Optional[TreeNode]) -> bool:
    #     queue = deque()
    #     if root:
    #         queue.append((root, []))
    #     while queue:
    #         for _ in range(len(queue)):
    #             node, path = queue.popleft()
    #             if node.left:
    #                 if node.val <= node.left.val:
    #                     return False
    #                 queue.append((node.left, path + [(node, True, False)]))
    #             if node.right:
    #                 if node.val >= node.right.val:
    #                     return False
    #                 queue.append((node.right, path + [(node, False, True)])) 
    #             for ancestor in path:
    #                 parent = ancestor[0]
    #                 left = ancestor[1]
    #                 right = ancestor[2]
    #                 if left:
    #                     if node.val >= parent.val:
    #                         return False
    #                 if right:
    #                     if node.val <= parent.val:
    #                         return False
    #     return True

    # DFS
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        if root:
            stack.append((root, None, None))
        while stack:
            node, minimum, maximum = stack.pop()
            if minimum:
                if node.val <= minimum:
                    return False
            if maximum:
                if node.val >= maximum:
                    return False
            if node.left:
                if node.val <= node.left.val:
                    return False
                if maximum:
                    stack.append((node.left, minimum, min(maximum, node.val)))
                else:
                    stack.append((node.left, minimum, node.val))
            if node.right:
                if node.val >= node.right.val:
                    return False
                if minimum:
                    stack.append((node.right, max(minimum, node.val), maximum)) 
                else:
                    stack.append((node.right, node.val, maximum)) 
        return True

    # BFS
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        queue = deque()
        if root:
            queue.append((root, None, None))
        while queue:
            node, minimum, maximum = queue.popleft()
            if minimum:
                if node.val <= minimum:
                    return False
            if maximum:
                if node.val >= maximum:
                    return False
            if node.left:
                if node.val <= node.left.val:
                    return False
                if maximum:
                    queue.append((node.left, minimum, min(maximum, node.val)))
                else:
                    queue.append((node.left, minimum, node.val))
            if node.right:
                if node.val >= node.right.val:
                    return False
                if minimum:
                    queue.append((node.right, max(minimum, node.val), maximum)) 
                else:
                    queue.append((node.right, node.val, maximum)) 
        return True

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

root = to_binary_tree([5,4,6,None,None,3,7])
print(Solution().isValidBST(root))

root = to_binary_tree([3,1,5,0,2,4,6])
print(Solution().isValidBST(root))

root = to_binary_tree([32,26,47,19,None,None,56,None,27])
print(Solution().isValidBST(root))