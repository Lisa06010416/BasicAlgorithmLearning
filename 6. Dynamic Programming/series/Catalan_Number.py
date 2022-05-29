"""96. Unique Binary Search Trees"""
class Solution:
    """求有n個點的bst有幾種"""
    def numTrees(self, n: int) -> int:
        """
        Catalan Number
        dp[3] =  dp[0]*dp[2]　　　(1為root，左子樹不存在，右子樹可以有兩個數字)
                 + dp[1] * dp[1] (2为根的情况，左右子樹都有一個數字)
                 + dp[2] * dp[0] (3为根的情况，左子樹有兩個數字，右子樹不存在)
        dp[i+1] = dp[0]*dp[i-1] + dp[1]*dp[i-1] + ... + dp[i-1]*dp[0]
        """
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1

        for i in range(1, n):
            for j in range(0, i + 1):
                dp[i + 1] += dp[j] * dp[i - j]
                print(i, j, dp)

        return dp[-1]