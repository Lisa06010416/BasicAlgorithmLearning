from typing import List, Optional
import functools


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""105. Construct Binary Tree from Preorder and Inorder Traversal"""
class Solution:
    """
    preorder確認root
    inorder確認左右子樹
    """
    class Solution:
        def buildTree(self, preorder, inorder):
            if not preorder:
                return None
            root = TreeNode(val=preorder[0])
            root_idx = inorder.index(preorder[0])
            root.left = self.buildTree(preorder[1:1 + root_idx], inorder[:root_idx])
            root.right = self.buildTree(preorder[1 + root_idx:], inorder[root_idx + 1:])
            return root


"""95. Unique Binary Search Trees II"""
class Solution:
    """give a postive number n, generate all BST which has node id from 1 to n
    backing + memory
    """
    @functools.lru_cache(None)  # memory
    def _build_bst(self, root, left, right):
        left_list = []
        for i in range(left, root):
            left_list.extend(self._build_bst(i, left, root - 1))

        right_list = []
        for i in range(root + 1, right + 1):
            right_list.extend(self._build_bst(i, root + 1, right))

        left_list = left_list if left_list else [None]
        right_list = right_list if right_list else [None]

        tree_list = []
        for l in left_list:
            for r in right_list:
                root_node = TreeNode(root, left=l, right=r)
                tree_list.append(root_node)

        return tree_list

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        tree_list = []
        for i in range(1, n + 1):
            tree_list.extend(self._build_bst(i, 1, n))
        return tree_list


"""108. Convert Sorted Array to Binary Search Tree"""
class Solution:
    """ convert a sorted array to high balance BST
    Input: nums = [-10,-3,0,5,9]
    Output: [0,-3,9,-10,null,5]
    Explanation: [0,-10,5,null,-3,null,9] is also accepted:
    """
    def build_bst(self, nums, left, right):
        if left > right:  # !!
            return None

        mid = left + (right-left)//2
        node = TreeNode(nums[mid])
        node.left = self.build_bst(nums, left, mid - 1)
        node.right = self.build_bst(nums, mid + 1, right)
        return node

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """
        因為要是 high balance，所以要由最中間的點開是建立node
        """
        root = self.build_bst(nums, 0, len(nums) - 1)
        return root