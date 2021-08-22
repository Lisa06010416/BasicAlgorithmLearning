from typing import List



"""322. Coin Change"""
class Solution:
    """給予一組硬幣的面額，硬幣可以重複選，回傳可以組到目標amount的最少硬幣數"""
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[j] => fewest num of coins (sum is j)
        # dp[j] = min(dp[j], dp[j-coins[i]]+1)

        dp = [0] + [float('inf')] * amount
        for i in range(len(coins)):
            for j in range(coins[i], amount + 1):
                dp[j] = min(dp[j], dp[j - coins[i]] + 1)

        if dp[-1] == float('inf'):
            return -1
        else:
            return dp[-1]



"""518. Coin Change 2"""
class Solution:
    """ 給予一組硬幣的面額，硬幣可以重複選，回傳可以組到目標amount的組合數"""
    def change(self, amount: int, coins: List[int]) -> int:
        # dp[i][j] = dp[i][j] or dp[i][j-coins[i]]
        # dp[j] = dp[j] + dp[j-coins[i]]  -> 可以組到j的金額的組合數

        dp = [1] + [0] * amount
        for i in range(len(coins)):
            for j in range(coins[i], amount + 1):
                dp[j] = dp[j] + dp[j - coins[i]]
        return dp[-1]