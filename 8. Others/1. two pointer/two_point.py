from typing import List


"""167. Two Sum II - Input array is sorted"""
class Solution:
    """ 輸入numbers array中哪兩個值和為targetc，numbers有排序過，回傳那兩個值的順序
    Input: numbers = [2,7,11,15], target = 9
    Output: [1,2]

    相似題：
    Two Sum
    """
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        two sum給的是沒有排序過的nums array，因此需要用dict，時間複雜度O(n)空間複雜度O(n)
        這題給了有排序過的nums array，因此可以用two point，時間複雜度O(n)空間複雜度O(1)
        """
        left, right = 0, len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
        return [-1, -1]


"""977. Squares of a Sorted Array"""
class Solution:
    """ 給予一個排序好的nums array，將李片的值取平方後，由小到達排序
    Input: nums = [-4,-1,0,3,10]
    Output: [0,1,9,16,100]
    """

    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        如果單純平方後排序好要O(nlogn)的時間
        使用two point時間為O(n)

        因為平方後的最大值會出現在頭或尾，因此使用two point指著頭尾依序平方並比較
        """
        left, right = 0, len(nums) - 1
        ans = []
        while left <= right:
            if abs(nums[left]) <= abs(nums[right]):
                ans.append(nums[right] ** 2)
                right -= 1
            else:
                ans.append(nums[left] ** 2)
                left += 1
        return reversed(ans)


"""15. 3Sum"""
class Solution:
    """
    給予一個nums array，找出全部的triplet (i,j,k)，確保 i!=j!=k，nums[i]+nums[j]+nums[k]=0

    no duplicate triplet
    input: [0,0,0,0]
    output: [[0,0,0]]

    相似題：
    3Sum Closest
    3Sum Smaller
    Valid Triangle Number
    """
    def threeSum(self, nums: list) -> int:
        """
        問題
        1. if len(nums)<3 => return 0

        解法:
        1. 先fix一個數，之後的兩個數用two sum的方式解 -> time out
        2. 因為要求和為0，因此另外兩數的和要為第一個fix住的數的負數，但在找另
           外兩個數的時候要對組數爬序後用two point來解，且因為要求不重複因此3個指針都要判斷重複
        """
        ans = []
        nums.sort()

        for n1_index in range(len(nums) - 2):
            target = -nums[n1_index]
            # 剪枝，在都大於0的情況，和不可能為0
            if nums[n1_index] > 0:
                break
            # 避免重複 如果數值重複則跳過
            if n1_index > 0 and nums[n1_index - 1] == nums[n1_index]:
                continue
            left, right = n1_index + 1, len(nums) - 1
            while left < right:
                if nums[left] + nums[right] == target:
                    ans.append([nums[n1_index], nums[left], nums[right]])
                    # 避免重複 如果數值重複則跳過
                    while left < len(nums) - 1 and nums[left] == nums[left + 1]:
                        left += 1
                    while right > 0 and nums[right] == nums[right - 1]:
                        right -= 1
                    # 更新 left/right
                    left += 1
                    right -= 1
                # 更新 left/right
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1
        return ans



"""48. Rotate Image"""
class Solution:
    """ Rotate Array 90 degree (clockwise)
     Input: [[1,2,3],
             [4,5,6],
             [7,8,9]]
    Output: [[7,4,1],
             [8,5,2],
             [9,6,3]]
    """

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
           0. 1. 2
        0| 1, 2, 3
        1| 4, 5, 6
        2| 7, 8, 9

        round num = len(matrix)//2

        round 1
        start = 0,0 : 0,2 -> 2,2 -> 2,0 -> 0,0
        start = 0,1 : 1,2 -> 2,1 -> 1,0 -> 0,1

        round 2

        1, 2, 3, 4
        1, 2, 3, 4
        1, 2, 3, 4
        1, 2, 3, 4

        1, 2, 3, 4, 5
        1, 2, 3, 4, 5
        1, 2, 3, 4, 5
        1, 2, 3, 4, 5
        1, 2, 3, 4, 5
        start = 0,0 : 0,4 -> 4,4 -> 4,0 -> 0,0
        start = 0,1 : 1,4 -> 4,3 -> 3,0 -> 0,1

        cur = (row, col)
        row,col = col, len(matric)-1-row
        """
        round_num = len(matrix) // 2
        round_now = 0
        move_len = len(matrix) - 1

        while round_now < round_num:
            for j in range(round_now, len(matrix) - round_now - 1):
                cur = [round_now, j]
                pre_val = matrix[cur[0]][cur[1]]
                for _ in range(4):
                    cur[0], cur[1] = cur[1], move_len - cur[0]
                    matrix[cur[0]][cur[1]], pre_val = pre_val, matrix[cur[0]][cur[1]]
            round_now += 1
        return matrix

