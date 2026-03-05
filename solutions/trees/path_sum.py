# Path Sum (LC #112)
# URL: https://leetcode.com/problems/path-sum/
# ─────────────────────────────────────────
# DIFFICULTY : Easy
# PATTERN    : DFS
# APPROACH   : The solution employs a recursive Depth-First Search (DFS) strategy. It traverses the tree, decrementing the `targetSum` by the current node's value at each step. A path sum is found if a leaf node is reached and the remaining `targetSum` is exactly zero, indicating a valid path. The search continues recursively in both left and right subtrees.
# TIME       : O(N)
# SPACE      : O(H)
# ─────────────────────────────────────────
# KEY INSIGHT: The key is to recursively propagate a reduced `targetSum` down the tree, checking if the sum becomes zero precisely when a leaf node is reached, signifying a valid path from root to leaf.
# GOTCHAS    : Remember to handle the base case of an empty tree. Crucially, the path sum must end at a *leaf* node, not just any internal node, so the final check `remaining==0` must only occur when `root.left` and `root.right` are both `None`.
# ─────────────────────────────────────────
# RATING     : ⭐⭐⭐⭐☆ (4/5)
# REVISIT    : ✅ No
# DATE       : 2026-03-05
# ─────────────────────────────────────────
# YOUR INSIGHT:
# DFS with targetSum - nodeValue propagated to leaf nodes to check if remaining target sum = 0 to ensure path exist

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # empty tree
        if not root:
            return False
        # leaf node
        if not root.left and not root.right:
            remaining=targetSum-root.val
            return remaining==0
        remaining=targetSum-root.val
        return self.hasPathSum(root.left, remaining) or self.hasPathSum(root.right, remaining)
