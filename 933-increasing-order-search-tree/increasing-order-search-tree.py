# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def increasingBST(self, root):
        dummy = TreeNode(0)
        current = [dummy]

        def inorder(node):
            if node is None:
                return

            inorder(node.left)

            node.left = None
            current[0].right = node
            current[0] = node

            inorder(node.right)

        inorder(root)

        return dummy.right