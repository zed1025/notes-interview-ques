# https://leetcode.com/problems/binary-tree-preorder-traversal/
# Given the root of a binary tree, return the preorder traversal of its nodes' values.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root):
        l = []
        if root == None:
            return []
        if root.left == None and root.right == None:
            x = []
            x.append(root.val)
            return x
        l.append(root.val)
        temp1 = self.preorderTraversal(root.left)
        temp2 = self.preorderTraversal(root.right)
        l.extend(temp1)
        l.extend(temp2)
        return l