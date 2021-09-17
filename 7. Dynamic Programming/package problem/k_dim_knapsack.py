from typing import List


"""474. Ones and Zeroes"""
class Solution:
    """給一一個binary str的list: strs, 找出最大的subset,整個subset的1的數量<=m,0的數量小於等於n"""
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # 01 背包問題 ＋ 二維背包問題
        # 每一個 binary str 視為一個商品，有兩個重量分別為1的數量與0的數量
        # 有兩個背包 :
        # dp1[j][k] => 當有j個0,k個1時可以放幾件商品

        nums = []
        for i in strs:
            nums.append([i.count('0'), i.count('1')])

        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(len(strs)):
            for j in reversed(range(nums[i][0], len(dp))):
                for k in reversed(range(nums[i][1], len(dp[0]))):
                    dp[j][k] = max(dp[j][k], dp[j - nums[i][0]][k - nums[i][1]] + 1)
        return dp[m][n]
