# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    preorder_map = {}
    inorder_map = {}
    preorder = []
    s = []

    def traversal(self, preorder_index, left_inorder, right_inorder):
        val = self.preorder[preorder_index]
        inorder_index = self.inorder_map[val]
        
        if inorder_index > left_inorder:
            left = self.traversal(preorder_index + 1, left_inorder, inorder_index - 1)
        else:
            left = None
        
        if inorder_index < right_inorder:
            left_tree_size = inorder_index - left_inorder
            right = self.traversal(preorder_index + 1 + left_tree_size, inorder_index + 1, right_inorder)
        else:
            right = None
        
        root = TreeNode(val, left, right)        
        return root
   
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.preorder = preorder
        self.inorder = inorder
        self.preorder_map = {}
        self.inorder_map = {}
        for i in range(len(preorder)):
            self.preorder_map[preorder[i]] = i
            self.inorder_map[inorder[i]] = i

        return self.traversal(0, 0, len(inorder) - 1)    

preorder = [1,2,3]
inorder = [2,1,3]
Solution().buildTree(preorder, inorder)

preorder = [1,2,4,5,3,6,7]
inorder = [4,2,5,1,6,3,7]
Solution().buildTree(preorder, inorder)

preorder = [1,2,3]
inorder = [2,3,1]
Solution().buildTree(preorder, inorder)

preorder = [1,2,3]
inorder = [3,2,1]
Solution().buildTree(preorder, inorder)

preorder = [1,2,3]
inorder = [1,3,2]
Solution().buildTree(preorder, inorder)

preorder = [1,2,3]
inorder = [1,2,3]
Solution().buildTree(preorder, inorder)
