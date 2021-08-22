from typing import List


"""312. Burst Balloons"""
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        """
        dp 定義 ：
        dp[i][j] => 戳破第i-j個氣球的最高分
        轉移函數：
        dp[i][j] = max(dp[i][j], nums[k]*nums[k-1]*nums[k+1]+dp[i][k-1]+dp[k+1][j]), j<=k<=i
        戳破第i-j個氣球的最高分 = max(原本的分數, (搓破第Ｋ個氣球的時候的分數) + (i~k-1顆氣球的最高分) + (k+1~j顆氣球的最高分))
        遍歷方法：
        [3,1,5,8] => [3] -> [1] -> [5] -> [8] -> [3,1] -> [1,5] -> [5,8] -> [3,1,5]
        """

        def print_dp(dp):
            print("~~~~~~~~~")
            for i in dp:
                print(i)

        nums = [1] + nums + [1]
        nums_len = len(nums)
        dp = [[0] * nums_len for _ in range(nums_len)]

        for win_size in range(nums_len - 2):
            left_point = 1
            while left_point + win_size < nums_len - 1:
                right_point = left_point + win_size
                for k in range(left_point, right_point + 1):
                    dp[left_point][right_point] = max(dp[left_point][right_point],
                                                      nums[k] * nums[left_point - 1] * nums[right_point + 1] + \
                                                      dp[left_point][k - 1] + \
                                                      dp[k + 1][right_point]
                                                      )
                print_dp(dp)
                left_point += 1
        return dp[1][-2]


"""198. House Robber"""
class Solution:
    """ 有一排連續的房子，每一個房子內都有一定的錢，用array nums表示，現有一個小偷不可以連續偷兩家的錢，最多可以偷到多少錢
    https://www.cnblogs.com/grandyang/p/4518674.html
    可用range 0~1 解
    或是在用空間壓縮，用兩個變數來解
    """
    def rob(self, nums: List[int]) -> int:
        """
        dp[i][j] => max amount from hourse i to j
        dp[i][j] = max(1., 2., 3.), i<=k<=j
            1. dp[i,j] => 之前有最大值
            2. dp[i][k-2] + nums[k] + dp[k+2][j] => 偷目前這一家
            3. dp[i][k-1] + dp[k+1][j]] => 不偷目前這一家
        traverse:
            [0, 0, 1, 4, 10, 30, 5, 0, 0]
            [1] -> [4] ... [1,4]
        """
        nums = [0, 0] + nums + [0, 0]
        dp = [[0] * len(nums) for _ in range(len(nums))]

        for i in range(2, len(nums) - 2):
            dp[i][i] = nums[i]

        for win_size in range(1, len(nums) - 4):
            for i in range(2, len(nums) - 2):
                j = i + win_size
                if j >= len(nums) - 2:
                    break
                for k in range(i, j + 1):
                    dp[i][j] = max([dp[i][j],
                                    dp[i][k - 2] + nums[k] + dp[k + 2][j],
                                    dp[i][k - 1] + dp[k + 1][j]])
                # print("~~~~~~~~")
                # for i in dp:
                #     print(i)
        return dp[2][-3]

"""213. House Robber II"""
class Solution:
    """ 有一排環狀的房子，每一個房子內都有一定的錢，用array nums表示，現有一個小偷不可以連續偷兩家的錢，最多可以偷到多少錢
    跟 House Robber I 解法一樣，只是要分別排除頭或尾，取最大值
    """
    def _get_max_amount(self, nums):
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[-1]

    def rob(self, nums: List[int]) -> int:
        """
        dp[i] : the max aount from hourse 0 ~ i
        dp[i] = max(dp[i-2]+dp[i], dp[i-1])
        """

        if len(nums) < 3:
            return max(nums)

        return (max(self._get_max_amount(nums[1:]),
                    self._get_max_amount(nums[:-1])))


"""647. Palindromic Substrings"""
class Solution:
    """給一段字串，判斷裡面為回文的子字串數量"""
    def is_palindormic(self, s):
        s_len = len(s)
        if s_len == 1:
            return 1

        if s[0:s_len // 2] == s[s_len // 2 + 1:s_len][::-1]:
            return 1
        return 0

    def countSubstrings(self, s: str) -> int:
        """
        dp :
        dp[j] : palindrome num from s[0] to s[j]
        dp[j] = is_palindormic(0, j) + ... + is_palindormic(j, j)
        """
        s = "%".join([i for i in s])
        dp = [0] + [0] * len(s)
        for j in range(1, len(s) + 1, 2):
            for k in range(j):
                dp[j] += self.is_palindormic(s[k:j])

        return sum(dp)


import functools

"""1959. Minimum Total Space Wasted With K Resizing Operations"""
class Solution:
    """ 給予 一個array nums判斷可以改變k次size大小，判斷會浪費多少空間
     nums = [10,20], k = 0 (size = [20, 20])
     nums = [10,20,30], k = 1 (size = [10, 30, 30])
    """
    def minSpaceWastedKResizing(self, nums: List[int], k: int) -> int:
        """ dp
        dp[i][k] : the minimum wasted size from nums i to len(nums) when has k change times
        """
        n, INF = len(nums), 200 * 1e6

        @functools.lru_cache(None)
        def dp(i, k):
            if i == n: return 0 #當已經遍歷完nums時回傳
            if k == -1: return INF #不能夠在change回傳ＩＮＦ
            ans = INF
            maxNum = nums[i]
            totalSum = 0
            for j in range(i, n):
                maxNum = max(maxNum, nums[j])
                totalSum += nums[j]
                wasted = maxNum * (j - i + 1) - totalSum  # 目前會浪費的容量
                ans = min(ans, dp(j + 1, k - 1) + wasted)
                # ans = min(過去的最小值, 下一步會被替換的最小值 + 目前的浪費容量)
            return ans
        return dp(0, k)


"""97. Interleaving String"""


class Solution:
    """ 求 s3是否是由s1跟s3的片段循環組成的
    Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
    Output: true
    """
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        dp[i][j] => s1的前i個字符與s2的前j個字符是匹配s3前i+j個字符
        dp[i][j] = (dp[i-1][j] and s1[i-1]==s3[i+j-1]) or (dp[i][j-1] and s2[j-1]==s3[i+j-1])

        ex s1="aabcc", s2="dbbca", s3="aadbbcbcac"
          N d b b c a
        N T F F F F F
        a T F F F F F
        a T T T T T F
        b F T T F T F
        c F F F F T T
        c F F F F F T
        """
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        dp[0][0] = True

        for i in range(0, len(s1) + 1):
            for j in range(0, len(s2) + 1):
                if i == 0 and j == 0:
                    continue

                condition1 = False
                if i - 1 >= 0:
                    condition1 = dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]

                condition2 = False
                if j - 1 >= 0:
                    condition2 = dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]

                dp[i][j] = condition1 or condition2

                # print(i,j)
                # for l in dp:
                #     print(l)
                # print()
        return dp[-1][-1]