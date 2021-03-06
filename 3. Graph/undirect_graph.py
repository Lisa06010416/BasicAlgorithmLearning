from typing import List


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []




"""133. Clone Graph"""
class Solution:
    """ clone a graph
    !! 用hashmap記錄走過的點
    """
    def clone(self, node, visited, val2node):
        if not node or node.val in visited:
            return None

        # 拿到當前的node
        if node.val in val2node:
            new_node = val2node[node.val]
        else:
            new_node = Node(val=node.val)
            val2node[new_node.val] = new_node
        # 把走過的點加到visited
        visited.append(node.val)
        # 新增當前node的鄰居加,並遞迴子節點
        if node.neighbors:
            new_node.neighbors = []
            for n in node.neighbors:
                if n.val not in val2node:
                    val2node[n.val] = Node(val=n.val)
                new_node.neighbors.append(val2node[n.val])
                self.clone(n, visited, val2node)
        return new_node

    def cloneGraph(self, node: 'Node') -> 'Node':
        return self.clone(node, [], {})


"""261. Graph Valid Tree"""
class Solution:
    """ 判斷輸入的圖是否是樹
    1. tree 是一個 min span graph, node_num -1 = edge_num, 且會連到每個點
    """
    def traversal(self, root, connect_list,):
        if not root:
            return connect_list

        connect_list.append(root.val) # 加入自己的val
        for e in root.neighbors: # 遍歷子節點
            if e.val not in connect_list: # 如果子節點沒有訪問過才訪問
                connect_list = self.traversal(e, connect_list)

        return connect_list

    def valid_tree(self, n: int, edges: List[List[int]]):
        edges_num = len(edges)
        if edges_num != n - 1:
            return False

        nodes_list = [Node(i) for i in range(n)]
        for e in edges:
            nodes_list[e[0]].neighbors.append(nodes_list[e[1]])
            nodes_list[e[1]].neighbors.append(nodes_list[e[0]])

        connect_list = self.traversal(nodes_list[0], [])

        if len(connect_list) == n:
            return True

        return False

# s = Solution()
# n = 5
# edges = [[0,1], [0,2], [2,3], [2,4]]
# answer = s.valid_tree(n, edges)
# print(answer)



"""310. Minimum Height Trees"""
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        作法一 ：
        # 1. build a tree
        # 2. traversal - use dfs to get the deep of each node
            # early stop : if the deepth > min deepth
        # 3. return root list

        作法二 ：
        這道題目其實是在考找圖的最中心的部分,用BFS的Topological Ordering
        """

        class node:
            def __init__(self, val, child=None, degree=0):
                self.val = val
                self.child = child if child else []
                self.degree = degree

        # build graph
        node_dict = {i: node(i) for i in range(n)}
        for n1, n2 in edges:
            node1, node2 = node_dict[n1], node_dict[n2]
            node1.child.append(node2)
            node1.degree += 1
            node2.child.append(node1)
            node2.degree += 1

        # del node
        while len(node_dict) > 2:
            # BFS
            queue = Queue()
            for k in node_dict:
                if node_dict[k].degree == 1:
                    queue.put(node_dict[k])

            # del node in queue
            while not queue.empty():
                del_node = queue.get()
                del_node.degree -= 1
                for c in del_node.child:
                    c.degree -= 1
                del node_dict[del_node.val]

        return node_dict.keys()


"""323 Number of Connected Components in an Undirected Graph"""
class Solution:
    """ 找到輸入的圖中有多少的聯通的子圖(connect_component)"""
    def traverse(self, node, visited_list):
        if not node or node.val in visited_list:
            return visited_list

        visited_list.append(node.val)
        for neighbor in node.neighbors:
            visited_list = self.traverse(neighbor, visited_list)

        return visited_list

    def connect_component(self, n: int, edges: List[List[int]]) -> int:
        # build graph
        node_list = [Node(val=i) for i in range(n)]
        for edge in edges:
            node_list[edge[0]].neighbors.append(node_list[edge[1]])
            node_list[edge[1]].neighbors.append(node_list[edge[0]])

        # traverse to find connect_component
        un_visited_list = list(range(n))
        connect_component_num = 0
        while un_visited_list:
            step_visited_list = self.traverse(node_list[un_visited_list[0]], [])
            for node_val in step_visited_list:
                un_visited_list.remove(node_val)
            connect_component_num += 1

        return connect_component_num

# s = Solution()
# n = 5
# edges = []
# answer = s.connect_component(n, edges)
# print(answer)
