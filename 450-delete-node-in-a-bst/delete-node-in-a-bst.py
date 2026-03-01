# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def helper(node):
            # If left child is None, return right child
            if node.left is None:
                return node.right
            # If right child is None, return left child
            if node.right is None:
                return node.left
            
            # Both children exist: find inorder successor
            # (rightmost node in left subtree)
            curr = node
            left = node.left
            right = node.right
            
            while left.right:
                left = left.right
            
            left.right = right
            return curr.left
        
        if not root:
            return None
        
        # If root is the node to delete
        if root.val == key:
            return helper(root)
        
        # Search for the node to delete
        curr = root
        while curr:
            if key < curr.val:
                if curr.left and curr.left.val == key:
                    curr.left = helper(curr.left)
                    break
                curr = curr.left
            else:
                if curr.right and curr.right.val == key:
                    curr.right = helper(curr.right)
                    break
                curr = curr.right
        
        return root
        
