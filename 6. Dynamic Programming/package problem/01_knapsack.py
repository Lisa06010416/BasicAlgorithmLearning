from typing import List




def zero_one_knapsack():
    V = 10   #  背包容量
    C = [1, 5, 7, 2, 6]  # 每個物品重量
    W = [20, 5, 1, 4, 7] # 每個物品價值
    
    dp = [False]*(V+1)
    dp[0] = 0
    item = [[] for  i in range(V+1)]
    
    for i in range(len(C)):
        for j in range(V, C[i]-1, -1):  # 倒敘遍歷 V - C[i] (j-C[i] >= 0)
            if dp[j] < dp[j-C[i]] + W[i]: # 紀錄是哪一些item
                item[j] = item[j-C[i]] + [i]
            dp[j] = max(dp[j], dp[j-C[i]] + W[i])
    # dp = [0, 20, 20, 24, 24, 24, 25, 27, 29, 31, 31]
    # item = [[], [0], [0], [0, 3], [0, 3], [0, 3], [0, 1], [0, 4], [0, 1, 3], [0, 3, 4], [0, 3, 4]]
    return dp[-1] 

print(zero_one_knapsack()) # 31  (裝第 0,3,4 個 item)






"""416. Partition Equal Subset Sum"""
class Solution:
    """檢查一個輸入的組數(值都會大於0),是否可以分成兩個值和相等的subset
    0/1 背包問題的變形
    """
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False

        # subset 的和為原本組數和的一半
        target = int(sum(nums) / 2)

        dp = [False] * (target + 1)  # dp[j] : nums可否組成和為j的值
        dp[0] = True
        print(dp)

        for i in range(len(nums)): # 判斷是否放第i個值
            print(f"~~~~~~~~~是否要放第{i}個nums:{nums[i]}~~~~~~~~~~~")

            # 如果放了第i個值那可能的容量會是 target~nums[i]
            for j in reversed(range(nums[i], target + 1)):
                # 轉移函式 :
                 # nums可否組成和為j的值 = (原本就可以組成和為j的值) or (加上i後可以組成和為j的值)
                dp[j] = dp[j] or dp[j - nums[i]]
            print(dp)
        return dp[-1]




"""494. Target Sum"""
class Solution:
    """ 給予一個 nums array, 以及一個目標和 target，每一個在nums裡的數字都要加或減以組成一個算式，求最後算式和為target的有多少種
    """
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # 01 package
        # A(加上加號的數字): pos set, B(加上減號的數字): neg set
        # sum = A + B, target = A - B
        # A = (sum + target)/2
        # 題目等於求 由 nums中選出一些數 和為 (sum + target)/2, 有幾種組合方法

        if (sum(nums) + target) % 2 == 1:
            return 0

        target = int((sum(nums) + target) // 2)
        dp = [1] + [0] * target

        for i in range(len(nums)):
            for j in reversed(range(nums[i], target + 1)):
                dp[j] = dp[j] + dp[j - nums[i]]
                # print(dp)

        return dp[-1]