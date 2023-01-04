from typing import List



"""240. Search a 2D Matrix II"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        1. dicing and concqer
        (重點)由down-left/top-right開始(因為這養小跟大都只有一個方向)
        1, down-left開始
        2. 如果point value < target 往上移動  point value > target 往右移動

        2. 每一個row or col用binary search
        """

        x, y = 0, len(matrix[0]) - 1

        while x < len(matrix) and y >= 0:
            if target < matrix[x][y]:
                y = y - 1
            elif target > matrix[x][y]:
                x = x + 1
            else:
                return True
        return False