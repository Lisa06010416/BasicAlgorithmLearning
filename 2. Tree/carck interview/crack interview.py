from random import randint


class Node:
    def __init__(self, val, left=None, right=None):
        self.val  = val
        self.left = left
        self.right = right

"""
        2
  1           3
0   1.5   2.5   4
"""
Node0 = Node(0, None, None)
Node1_5 = Node(1.5, None, None)
Node2_5 = Node(2.5, None, None)
Node4 = Node(4, None, None)
Node1 = Node(1, Node0, Node1_5)
Node3 = Node(3, Node2_5, Node4)
Node2 = Node(2, Node1, Node3) # root


""" Successor"""
# 方法一： 序列化後找
def get_successor1(root: Node, target: Node):
    def get_inorder(root: Node, ans: list):
        if not root:
            return ans

        get_inorder(root.left, ans)
        ans.append(root.val)
        get_inorder(root.right, ans)

        return ans

    inorder = get_inorder(root, [])
    for v_idx, v in enumerate(inorder):
        if v == target.val:
            if v_idx-1 < 0:
                return None
            return inorder[v_idx-1]

# 方法二： 找BST中小魚target的最大值
def get_successor2(root: Node, target: Node):
    ans_node = None
    while root:
        if root.val >= target.val:
            root = root.left
        else:
            ans_node = root
            root = root.right
    return ans_node.val if ans_node else None


print("successor:")
print(get_successor1(Node2, Node1))
print(get_successor1(Node2, Node2))
print(get_successor1(Node2, Node3))

print(get_successor2(Node2, Node1))
print(get_successor2(Node2, Node2))
print(get_successor2(Node2, Node3))


"""BST Sequences

#         2
#   1           3
# 0   1.5   2.5   4

# 1. 移除2 -> 1,3 可能是下一個
    # 1.1 移除1 -> 0, 1,5, 3 可能是下一個
    
-> 不斷移除一個root,將其子樹的root加入candidate set中，遞迴求全部的解
      0,1.5,3

space: n^2
skew bst tree : 1
balance bst need time: 1*2*3*...*leaf_node_num*...*1 ~= leaf_node_num!^2
"""

def get_all_bst_sequence(root:Node) -> list:
    def get_all_seq(temp_ans, candidate_nodes, ans_list):
        if not candidate_nodes:
            ans_list.append(temp_ans.copy())
            return ans_list

        for cn_idx,  cn in enumerate(candidate_nodes):
            if cn:
                next_candidate_nodes = candidate_nodes[0:cn_idx] + candidate_nodes[cn_idx+1:]
                if cn.left:
                    next_candidate_nodes.append(cn.left)
                if cn.right:
                    next_candidate_nodes.append(cn.right)
                temp_ans.append(cn.val)
                get_all_seq(temp_ans, next_candidate_nodes, ans_list)
                temp_ans.pop(-1)
        return ans_list
    return get_all_seq([], [root], [])

print("\nall_bst_sequence :")
for a in get_all_bst_sequence(Node2):
    print(a)
print(len(get_all_bst_sequence(Node2)))

"""Implement BST"""
class RandomNodeBST():
    def __init__(self):
        self.root = None
        self.node_level_dict = {} # {0:[nodeobject,...,]}

    def insert(self, node_val):
        node = Node(node_val)
        root = self.root
        if not root:
            self.root = node
            return self.root

        while root:
            if root.val < node.val:
                if root.right:
                    root = root.right
                else:
                    root.right = node
                    break
            else:
                if root.left:
                    root = root.left
                else:
                    root.left = node
                    break
        return self.root

    def find(self, target_val):
        root = self.root
        while root:
            if root.val == target_val:
                return root
            elif root.val < target_val:
                root = root.right
            else:
                root = root.left
        return None

    def delete(self, target_val):
        if not self.root:
            return None

        target_node = self.find(target_val)
        if target_node.left: # target_node 有左子樹 -> 找做子樹最大的node替換
            replace_node = target_node.left
            if replace_node.right: # 左子節點還有右子節點
                replace_node_parent = target_node
                while replace_node.right:
                    replace_node_parent = replace_node
                    replace_node = replace_node.right
                replace_node_parent.right = None
                target_node.val = replace_node.val
            else: # 左子節點還沒有右子節點
                target_node.val = replace_node.val
                target_node.left = replace_node.left
        elif target_node.right:  # target_node 只有右子樹 -> 將右子樹替換
            replace_node = target_node.right
            target_node.val = replace_node.val
            target_node.right = replace_node.right
            target_node.left = replace_node.left
        else: # target_node 沒有左右子樹 -> 刪掉node
            if target_node == self.root: # 只剩下root一個點 -> 刪掉整棵樹
                self.root = None
            else: # 移除父節點的連接
                # get parent
                parent = self.root
                while parent:
                    # parent 的左右子樹是target -> 移除該node
                    if parent.left and parent.left.val == target_val:
                        parent.left = None
                    elif parent.right and parent.right.val == target_val:
                        parent.right = None
                    # 移動 parent
                    if parent.val < target_val:
                        parent = parent.right
                    else:
                        parent = parent.left
        return self.root

    def preorder(self):
        def get_preorder(root: Node, ans: list):
            if not root:
                ans.append(None)
                return ans

            ans.append(root.val)
            get_preorder(root.left, ans)
            get_preorder(root.right, ans)

            return ans
        return get_preorder(self.root, [])


print("\nImplement BST:")
"""

       5
     3   7
   1    N  N
 0
N N

del 5:
     3
  1     7
 0  N  N  N
N N

del 7
      3
  1     N
 0  N 
N N

del 1
   3
 0  N 
N N

"""
R_BST = RandomNodeBST()
R_BST.insert(5)
R_BST.insert(3)
R_BST.insert(7)
R_BST.insert(1)
R_BST.insert(0)
print(R_BST.preorder())
R_BST.delete(5)
print(R_BST.preorder())
R_BST.delete(7)
print(R_BST.preorder())
R_BST.delete(1)
print(R_BST.preorder())
R_BST.delete(3)
print(R_BST.preorder())
R_BST.delete(0)
print(R_BST.preorder())


"""Random Node
       10,6
    /        \
  20,2       30,2
 /   \       /   \
40,0 50,0  60,0  70,0
The first value is node and second value is count of children.

"""
class CountNode:
    def __init__(self, data):
        self.data = data
        self.children = 0
        self.left = None
        self.right = None


# Inserts Children count for each node
def insertChildrenCount(root):
    def getElements(root):
        if root == None:
            return 0

        return (getElements(root.left) +
                getElements(root.right) + 1)

    if root == None:
        return
    root.children = getElements(root) - 1
    insertChildrenCount(root.left)
    insertChildrenCount(root.right)


# Returns number of children for root
def children(root):
    if root == None:
        return 0
    return root.children + 1


# Helper Function to return a random node
def randomNodeUtil(root, count):
    if root == None:
        return 0

    if count == children(root.left):
        return root.data

    if count < children(root.left):
        return randomNodeUtil(root.left, count)

    return randomNodeUtil(root.right,
                          count - children(root.left) - 1)


# Returns Random node
def randomNode(root):
    count = randint(0, root.children)
    return randomNodeUtil(root, count)

# Creating Above Tree
root = CountNode(10)
root.left = CountNode(20)
root.right = CountNode(30)
root.left.right = CountNode(40)
root.left.right = CountNode(50)
root.right.left = CountNode(60)
root.right.right = CountNode(70)

# 更新 childrenCount
insertChildrenCount(root)

print("A Random Node From Tree :", randomNode(root))




