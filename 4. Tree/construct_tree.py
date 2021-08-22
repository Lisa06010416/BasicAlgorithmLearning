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
    def construct_binary_tree(self, preorder, inorder):
        if not preorder:
            return None

        root = preorder[0]
        root_index = inorder.index(root)

        # left
        left_node = self.construct_binary_tree(preorder[1:root_index + 1], inorder[0:root_index])
        # right
        right_node = self.construct_binary_tree(preorder[root_index + 1:], inorder[root_index + 1:])

        root_node = TreeNode(val=root)
        root_node.left = left_node
        root_node.right = right_node

        return root_node

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return self.construct_binary_tree(preorder, inorder)




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
