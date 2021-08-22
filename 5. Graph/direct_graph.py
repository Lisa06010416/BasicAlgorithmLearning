from typing import List


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