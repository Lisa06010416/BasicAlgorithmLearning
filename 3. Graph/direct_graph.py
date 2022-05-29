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



"""227. Find the celebrity"""
class Solution:
    """找到n個人中哪一個人是所有人都認識但不認識其他人的人"""
    def __init__(self, graph):
        self.graph = graph

    def knows(self, a, b): # if a knows n ?
        return self.graph[a][b]

    def find_celebrity(self, num):
        # 遍歷一次，找到celebrity candidate: 將啲一個人作為candidate，判斷candidate是否認識其他人knows(cand, i)，有的話將i作為新的candidate
        cand = 0
        for i in range(1, num):
            if self.knows(cand, i):
                cand = i

        # 在遍歷一次 確認 celebrity candidate 沒有認識任何人且任何人都認識他
        for i in range(1, num):
            if i == cand:
                continue
            if not self.knows(i, cand) or self.knows(cand, i):
                return -1

        return cand
graph = [
          [1,1,0],
          [0,1,0],
          [1,1,1]
        ]
s = Solution(graph)
print(s.find_celebrity(3))


"""269. Alien Dictionary"""
