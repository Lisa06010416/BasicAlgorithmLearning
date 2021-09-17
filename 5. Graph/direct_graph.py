from typing import List
from queue import Queue

class Node:
    def __init__(self, val=None, neighbor=None):
        self.val = val
        self.neighbor = neighbor if neighbor else []


"""207. Course Schedule"""
class Solution:
    """
    判斷有像圖是否有環
    """
    def has_cycle(self, node, path):
        if node.val in path:  # 當前路徑重複走
            return False
        if node.val in self.visited:  # 之前已經拜訪過確認沒有環
            return True

        path[node.val] = None
        for ner in node.neighbor:
            if not self.has_cycle(ner, path):
                return False
        del path[node.val]
        self.visited[node.val] = True
        return True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        nodelist = [Node(i) for i in range(numCourses)]
        for c1, c2 in prerequisites:
            nodelist[c1].neighbor.append(nodelist[c2])

        self.visited = {}  # 拜訪過確認沒有環的點
        for i in range(numCourses):
            if not self.has_cycle(nodelist[i], {}):
                return False
        return True


"""269. Alien Dictionary"""




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
