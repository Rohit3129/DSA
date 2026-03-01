# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        res = [0]
        def check(node):
            if not node: return 0, True, -inf, inf
            s1, bst1, maxx1, minn1 = check(node.left)
            s2, bst2, maxx2, minn2 = check(node.right)
            if bst1 and bst2 and maxx1 < node.val < minn2:
                v= node.val +s1 + s2
                res[0] = max(res[0], v)
                return v, True, max(maxx2, node.val), min(node.val, minn1)
            return 0, False, -inf, inf
        check(root)
        return res[0]
