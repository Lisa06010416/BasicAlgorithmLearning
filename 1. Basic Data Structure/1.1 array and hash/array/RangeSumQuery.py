"""307. Range Sum Query - Mutable
method 1 : 區間和
"""
import math
class RangeSumQuery1D:
    def __init__(self, nums):
        self.nums = nums
        self.data_num = len(nums)
        self.block_size = int(math.sqrt(self.data_num))   # 計算每一個block的大小
        self.block_num = math.ceil(self.data_num/self.block_size)   # 計算要幾個block

        # 計算每個block的和
        self.block = [0] * self.block_num
        for i in range(self.data_num):
            self.block[i//self.block_size] += self.nums[i]

    def update(self, i, val):  # O(1)
        block_idx = i//self.block_size
        self.block[block_idx] = self.block[block_idx] - self.nums[i] + val  # 更新block
        self.nums[i] = val # 更新 numx

    def sumRange(self, i, j): # O(self.block_num)
        # 計算開始到結尾的block index(完全包含)
        """
        ex block size = 2
        block:  0   1   2
        index: 0 1 2 3 4 5
        """
        start_block_idx = i//self.block_size if i%self.block_size==0 else i//self.block_size + 1
        end_block_idx = j//self.block_size if  j%self.block_size==self.block_size-1 else j//self.block_size - 1

        sum = 0
        # 前面零散的數字和
        for k in range(i, start_block_idx*self.block_size):
            sum += self.nums[k]
        # 後面零散的數字和
        for k in range(end_block_idx*self.block_size + self.block_size, j+1):
            sum += self.nums[k]
        # 完整的block和
        for k in range(start_block_idx, end_block_idx+1):
            sum += self.block[k]
        return sum

print("\nRange Sum Query - Mutable - 區間和: ")
numarray = RangeSumQuery1D([1, 2, -7, 5, 0, 1])
print(numarray.sumRange(0, 1))
print(numarray.sumRange(1, 3))
numarray.update(1, -10)
print(numarray.sumRange(0, 1))
print(numarray.sumRange(1, 3))


"""307. Range Sum Query - Mutable
method 2 : binary index tree(Fenwiki Tree)"""
class RangeSumQuery1D:
    def __init__(self, nums):
        self.nums = nums
        self.nums_len = len(self.nums)
        self.fenwiki = [0] * (len(self.nums) + 1)

        # build fenwiki
        for i in range(1, self.nums_len+1):  
            self.fenwiki_update(i, self.nums[i-1])
        print(self.fenwiki)

    def fenwiki_get_lowbits(self, x):
        return x & -x
    
    def fenwiki_update(self, i, x):
        while i <= self.nums_len:
            self.fenwiki[i] += x
            i = i + self.fenwiki_get_lowbits(i) # 右父節點

    def fenwiki_getsumi(self, i):
        sum = 0
        while i > 0:
            sum +=  self.fenwiki[i]# 左父節點
            i = i - self.fenwiki_get_lowbits(i)
        return sum


    def update(self, i, val):  # O(1)
        self.fenwiki_update(i+1, val - self.nums[i])
        self.nums[i] = val

    def sumRange(self, i, j): # O(log(n))
        return self.fenwiki_getsumi(j+1) - self.fenwiki_getsumi(i)

print("\nRange Sum Query - Mutable (binary index tree(Fenwiki Tree)): ")
numarray = RangeSumQuery1D([1, 3, 5, 9, 11, 13, 15, 17])
numarray.update(2, 2)
print(numarray.sumRange(0, 2))
print(numarray.sumRange(3, 7))



""" 308. Range Sum Query 2D - Mutable
1. binary index tree(Fenwiki Tree)
"""
class RangeSumQuery2D:
    def __init__(self, matrix):
        self.matrix = matrix
        self.matrix_rows_num, self.matrix_cols_num = len(matrix), len(matrix[0])
        self.fenwiki_rows_num, self.fenwiki_cols_num = len(matrix) + 1, len(matrix[0]) + 1
        self.fenwiki = [[0]*self.fenwiki_cols_num for _ in range(self.fenwiki_rows_num)]
        for i in range(self.matrix_rows_num):
            for j in range(self.matrix_cols_num):
                self.fenwiki_update(i, j, self.matrix[i][j])

    def fenwiki_get_lowbits(self, x):
        return x & -x

    def fenwiki_update(self, row, col, dif):  # O(logn)
        i = row + 1
        while i < self.fenwiki_rows_num:
            j = col + 1
            while j < self.fenwiki_cols_num:
                self.fenwiki[i][j] += dif
                j += self.fenwiki_get_lowbits(j)
            i += self.fenwiki_get_lowbits(i)
    
    def fenwiki_sum(self, row, col):
        sum = 0
        i = row + 1
        while i > 0:
            j = col + 1
            while j > 0:
                sum += self.fenwiki[i][j]
                j -= self.fenwiki_get_lowbits(j)
            i -= self.fenwiki_get_lowbits(i)
        return sum
    
    def update(self, i, j, val): # O(logn)
        dif = val - self.matrix[i][j]
        self.matrix[i][j] = val
        self.fenwiki_update(i, j, dif)

    def sumRange(self, i_1, j_1, i_2, j_2): # O(log(n))
        return self.fenwiki_sum(i_2, j_2) - self.fenwiki_sum(i_1-1, j_2) - self.fenwiki_sum(i_2, j_1-1) + self.fenwiki_sum(i_1-1, j_1-1)


print("\nRange Sum Query 2D - Mutable (binary index tree(Fenwiki Tree)): ")
matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]
adder = RangeSumQuery2D(matrix)
print(adder.sumRange(2, 1, 4, 3))
adder.update(3, 2, 2)
print(adder.sumRange(2, 1, 4, 3))


