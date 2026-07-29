# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        if not root:
            return 0
        def countFrom(node, target):
            if not node:
                return 0
            count = 0
            if node.val == target:
                count += 1
            count += countFrom(node.left, target - node.val)
            count += countFrom(node.right, target - node.val)
            return count
            
        return (countFrom(root, targetSum) +
                self.pathSum(root.left, targetSum) +
                self.pathSum(root.right, targetSum))