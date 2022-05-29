from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""94. Binary Tree Inorder Traversal"""
class Solution:
    def inorderTraversal_recursive(self, root: Optional[TreeNode]) -> List[int]:
        """give a root of a tree, return the in order traversal of its node's value"""
        def traversal(root, sequence):
            if not root:
                return None

            traversal(root.left, sequence)
            sequence.append(root.val)
            traversal(root.right, sequence)

        sequence = []
        traversal(root, sequence)
        return sequence

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        stack  = [(node, state), ...]
        state:
        -1: no visite
        0 : visited fitst time
        1 : have visited the left child
        """
        stack = [[root, -1]]
        seq = []
        while stack:
            point_node = stack[-1]
            # if a node is None ...
            if not point_node[0]:
                stack.pop()
                continue

            # state translate
            if point_node[1] == -1:
                point_node[1] = 0
                stack.append([point_node[0].left, -1])
            elif point_node[1] == 0:
                point_node[1] = 1
                seq.append(point_node[0].val)
                stack.append([point_node[0].right, -1])
            else:
                stack.pop()

        return seq


""" 98. Validate Binary Search Tree """
class Solution:
    """
    time complexity: O(n)
    space complexity: O(1)
    不用recursive => 用 stack 做 DFS search
    """
    def check_bts(self, root, min, max):
        if not root:
            return True
        if not (root.val > min and root.val < max):
            return False
        return self.check_bts(root.left, min, root.val) and self.check_bts(root.right, root.val, max)

    def isValidBST(self, root: TreeNode) -> bool:
        return self.check_bts(root, float('-inf'), float('inf'))


"""104. Maximum Depth of Binary Tree"""
class Solution:
    def get_max_path(self, root, depth):
        if not root:
            return depth
        depth += 1
        return max(self.get_max_path(root.left, depth),
                   self.get_max_path(root.right, depth))

    def maxDepth(self, root: TreeNode) -> int:
        return self.get_max_path(root, 0)


"""100. Same Tree"""
class Solution:
    "把樹序列化並且要加入null的點(借用full tree)"
    def get_preorder(self, root, inorder):
        if not root:
            inorder.append(None)
            return inorder

        inorder.append(root.val)
        self.get_preorder(root.left, inorder)
        self.get_preorder(root.right, inorder)

        return inorder

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        return self.get_preorder(p, []) == self.get_preorder(q, [])


"""102. Binary Tree Level Order Traversal"""
class Solution:
    """
    BFS
    """
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = []
        queue.append((root,0))
        level_order = []
        while queue:
            point_node, point_level = queue.pop(0)
            if point_node: # 注意 queue 有append None
                queue.append((point_node.left, point_level+1))
                queue.append((point_node.right, point_level+1))

                if len(level_order) <= point_level:
                    level_order.append([])
                level_order[point_level].append(point_node.val)
        return level_order


"""124. Binary Tree Maximum Path Sum"""
class Solution:
    """
    找到bt path中節點和最大的值
    用到divid and conuer
    遞迴找左右子樹的最大值，判斷當前節點的最大值
    回傳 左子樹/右子樹 + 自己的值的最大值
    """
    def get_max_sum_of_treepath(self, root):
        if not root:
            return 0
        # 拿到左右指數的最大值
        left_max_sum = self.get_max_sum_of_treepath(root.left)
        right_max_sum = self.get_max_sum_of_treepath(root.right)
        # 自己的最大值
        max_sum = root.val
        if left_max_sum > 0:
            max_sum += left_max_sum
        if right_max_sum > 0:
            max_sum += right_max_sum
        # 自己的最大值 是否是目前最大的
        if self.total_max_sum < max_sum:
            self.total_max_sum = max_sum

        # 因為path不能分岔, 回傳 左子樹/右子樹 + 自己的值的最大值
        max_subtree_sum = max(max(left_max_sum, right_max_sum), 0)
        return max_subtree_sum + root.val

    def maxPathSum(self, root: TreeNode) -> int:
        self.total_max_sum = float("-inf")
        self.get_max_sum_of_treepath(root)
        return self.total_max_sum


"""226. Invert Binary Tree"""
class Solution:
    def inverse(self, root):
        if not root:
            return None

        self.inverse(root.left)
        self.inverse(root.right)

        temp = root.left
        root.left = root.right
        root.right = temp

    def inverse_tree(self, root: TreeNode):
        self.inverse(root)
        return root



"""235. Lowest Common Ancestor of a Binary Search Tree"""
class Solution:
    """
    給一個ＢＳＴ，跟兩個node，找到這兩個node的最小Ancestor
    自己可以是自己的Ancestor
    """
    def get_ancestor(self, root: TreeNode):
        if not root:
            return None, False, False

        left_ancestor, p_in_left, q_in_left = self.get_ancestor(root.left)
        right_ancestor, p_in_right, q_in_right = self.get_ancestor(root.right)

        if left_ancestor or right_ancestor:
            return left_ancestor if left_ancestor else right_ancestor, True, True

        ancestor = None
        has_p = p_in_left or p_in_right
        has_q = q_in_left or q_in_right

        if root.val == self.p.val:
            has_p = True
        if root.val == self.q.val:
            has_q = True
        if has_p and has_q:
            ancestor = root

        return ancestor, has_p, has_q

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.p = p
        self.q = q
        ancestor, _, _ = self.get_ancestor(root)
        return ancestor


"""572. Subtree of Another Tree"""
class Solution:
    """
    第一種解法
    判斷一個樹是否是另一個樹的Subtree
    轉成preorder比較
    """
    def preorder(self, root, preorder):
        if not root:
            preorder += "#,"
            return preorder

        preorder += f"{root.val},"
        preorder = self.preorder(root.left, preorder)
        preorder = self.preorder(root.right, preorder)
        return preorder

    def isSubtree1(self, root: TreeNode, subRoot: TreeNode) -> bool:
        root_preorder = self.preorder(root, ",") # 開頭加, 因為會有 12,1 跟 2,1 被誤判的問題
        subroot_preorder = self.preorder(subRoot, ",")
        # print(root_preorder)
        # print(subroot_preorder)
        return subroot_preorder in root_preorder

    """~~~~~~~~~~~ 第二種解法 兩個遞迴確認~~~~~~~~~~~~~~"""
    def is_subtree(self, root, subRoot):
        if not root:
            return False

        is_same_tree = False
        if root.val == subRoot.val:
            is_same_tree = self.is_same_tree(root, subRoot)
        if is_same_tree:
            return True

        return (self.is_subtree(root.left, subRoot) or
                self.is_subtree(root.right, subRoot))

    def is_same_tree(self, root, subRoot):
        if not subRoot and not root:
            return True
        elif not subRoot or not root:
            return False

        if subRoot.val != root.val:
            return False

        left_is_same = self.is_same_tree(root.left, subRoot.left)
        right_is_same = self.is_same_tree(root.right, subRoot.right)

        return left_is_same and right_is_same

    def isSubtree2(self, root: TreeNode, subRoot: TreeNode) -> bool:
        return self.is_subtree(root, subRoot)


class Codec:
    """
    序列化(前序、後序、BFS) 反序列化
    """
    def _get_serialize(self, root, sequence):
        if not root:
            sequence += ",!"
            return sequence

        sequence += f",{root.val}"
        sequence = self._get_serialize(root.left, sequence)
        sequence = self._get_serialize(root.right, sequence)
        return sequence

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        return self._get_serialize(root, "")

    def _get_tree_from_sequence(self, sequence_list):
        if not sequence_list:
            return None
        if sequence_list[0] == "!":
            sequence_list.pop(0)
            return None

        val = sequence_list.pop(0)
        node = TreeNode(val)
        node.left = self._get_tree_from_sequence(sequence_list)
        node.right = self._get_tree_from_sequence(sequence_list)

        return node

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        return self._get_tree_from_sequence(data.split(",")[1:])


"""230. Kth Smallest Element in a BST"""
class Solution:
    """找到BST Tree中第k的小的值"""
    def _dfs(self, root, k, val):
        if not root or k <= 0:
            return (k, val)

        k, val = self._dfs(root.left, k, val)

        k -= 1
        if k == 0:
            return (k, root.val)

        k, val = self._dfs(root.right, k, val)

        return (k, val)

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        return self._dfs(root, k, -1)[1]


"""236. Lowest Common Ancestor of a Binary Tree"""
class Solution:
    """給一棵樹，找出樹上兩個點的最低共同父節點LCA(lowest common ancestor)"""
    def _dfs(self, root, p, q):
        is_find_p, is_find_q = False, False

        if not root:
            return None, is_find_p, is_find_q

        if root.val == p.val:
            is_find_p = True
        elif root.val == q.val:
            is_find_q = True

        ans_l, is_find_p_l, is_find_q_l = self._dfs(root.left, p, q)
        ans_r, is_find_p_r, is_find_q_r = self._dfs(root.right, p, q)

        if ans_l or ans_r:
            return ans_l or ans_r, True, True

        is_find_p = is_find_p_l or is_find_p_r or is_find_p
        is_find_q = is_find_q_l or is_find_q_r or is_find_q

        if is_find_p and is_find_q:
            return root, is_find_p, is_find_q
        return None, is_find_p, is_find_q

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = self._dfs(root, p, q)
        return ans[0]
