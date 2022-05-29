from typing import List


"""139. Word Break"""
class Solution:
    """ 給予字串s跟單字wordDict，是否可用wordDict內任意的單字組成字串(可重複用)
    s = "leetcode", wordDict = ["leet","code"]
    ourput: True

    有兩種解法 memory + recursive or DP
    """
    def _check(self, target_s):
        if not target_s:
            return True

        for index in range(1, len(target_s) + 1):
            if target_s[:index] in self.worddict: # 找到前面可以被切分的部分
                if self.memo[-len(target_s[index:])] != 0:  # 剩餘的部分沒有檢查過
                    if self._check(target_s[index:]):  # 遞迴處理後面的部分
                        return True

        self.memo[-len(target_s)] = 0 # 紀錄目前字串無法被切分

        return False

    def wordBreak_memoryrecursive(self, s: str, wordlist: List[str]) -> bool:
        """
        1. 遞迴去找後面的字串是否存在 :
            先找到s前面有在字典裡的單字,再把剩下的字串丟到下一個遞迴裡面確認
        2. memory, 當遞迴到後面確定無法切分時，可以記錄起來，避免重複處理
        """
        if not s or not wordlist:
            return False
        self.worddict = {}
        self.memo = [1] * (len(s) + 1)
        for w in wordlist:
            self.worddict[w] = None
        return self._check(s)


class Solution:
    def _dfs(self, heights, r, c, is_connect):
        if (r, c) in self.ans_dict:
            return True
        if sum(is_connect) == 2:
            return True
        if heights[r][c] == -1:
            return False
        if (r < 0 or c < 0) or (r >= len(heights) or c >= len(heights[0])):
            return False

        if r == 0 or c == 0:
            is_connect[0] = 1
        if r == len(heights) - 1 or c == len(heights[0]) - 1:
            is_connect[1] = 1

        temp_h = heights[r][c]
        heights[r][c] = -1
        for i, j in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            if self._dfs(heights, r + i, c + j, is_connect):
                break
        heights[r][c] = temp_h

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.ans_dict = {}
        for r in range(len(heights)):
            for c in range(len(heights[0])):
                is_connect = self._dfs(heights, r, c, [0, 0])
                if is_connect:
                    self.ans_dict[(r, c)] = None
        return [list(i) for i in self.ans_dict.keys()]


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
            for j in range(i, n): # 到 i 的部分不替換
                maxNum = max(maxNum, nums[j])
                totalSum += nums[j]
                wasted = maxNum * (j - i + 1) - totalSum  # 目前會浪費的容量
                ans = min(ans, dp(j + 1, k - 1) + wasted)
                # ans = min(過去的最小值, 下一步會被替換的最小值 + 目前的浪費容量)
            return ans
        return dp(0, k)
