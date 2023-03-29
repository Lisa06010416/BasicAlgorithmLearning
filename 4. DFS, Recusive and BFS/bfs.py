from typing import List
import queue

"""994. Rotting Oranges"""
class Solution:
    """give a mxn matric, and each cell can be 0(none), 1(fresh orange), 2(rotten orange)
    and if a fresh connect to a rotten orange, it will be a rotten orange next round

    return : how many rounds do we need when all orange rotten
    """
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh_orange_num = 0
        rotten_orange_pos = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh_orange_num += 1
                elif grid[i][j] == 2:
                    rotten_orange_pos.append((i, j))

        change_num = 0
        while rotten_orange_pos and fresh_orange_num > 0:
            next_rotten_orange_pos = []
            for i, j in rotten_orange_pos:
                # !! 可以用 move list 做
                if i - 1 >= 0 and grid[i - 1][j] == 1:
                    grid[i - 1][j] = 2
                    fresh_orange_num -= 1
                    next_rotten_orange_pos.append((i - 1, j))
                if i + 1 < len(grid) and grid[i + 1][j] == 1:
                    grid[i + 1][j] = 2
                    fresh_orange_num -= 1
                    next_rotten_orange_pos.append((i + 1, j))
                if j - 1 >= 0 and grid[i][j - 1] == 1:
                    grid[i][j - 1] = 2
                    fresh_orange_num -= 1
                    next_rotten_orange_pos.append((i, j - 1))
                if j + 1 < len(grid[0]) and grid[i][j + 1] == 1:
                    grid[i][j + 1] = 2
                    fresh_orange_num -= 1
                    next_rotten_orange_pos.append((i, j + 1))

            rotten_orange_pos = set(next_rotten_orange_pos)
            change_num += 1

        if fresh_orange_num == 0:
            return change_num
        else:
            return -1



"""116. Populating Next Right Pointers in Each Node"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        q = queue.Queue()
        q.put([root, 0])
        while not q.empty():
            point_node, point_level = q.get()
            if not point_node:
                break
            if not q.empty() and point_node:
                if q.queue[0][1] == point_level:
                    point_node.next = q.queue[0][0]

            if point_node.left:
                q.put([point_node.left, point_level + 1])
                q.put([point_node.right, point_level + 1])
        return root