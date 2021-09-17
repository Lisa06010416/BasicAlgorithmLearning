from collections import defaultdict

"""76. Minimum Window Substring"""
class Solution:
    """ 給予兩個str s and t, 找到s中完全包含t的字母的最小子字串
    用sliding windows的方式
    """
    def minWindow(self, s: str, t: str) -> str:
        # 紀錄t中每個字母出現的次數
        letter_dict = defaultdict(int)
        for i in t:
            letter_dict[i] += 1

        # sliding windows
        left = 0  # window 的左邊的index
        count = 0  # 目前的 window 內包含幾個t中的字母
        min_len = float("inf")  # 紀錄最小的子字串長度
        min_len_index = (0, 0)  # 最小子字串出現的index
        for right, i in enumerate(s):  # 遍歷 每一個 s 中的字母
            if i in letter_dict:  # 如果該字母有在t中出現,更新 letter_dict
                letter_dict[i] -= 1
                if letter_dict[i] >= 0:  # 如果該字母出現的次數還沒有滿足t,window內包含t的字母數加1
                    count += 1
            while count == len(t): # 當window內已經包含全部t中的字母，開始移動left point所減window
                if right - left + 1 < min_len: # 當前的window size是否是最小
                    min_len = right - left + 1
                    min_len_index = (left, right + 1)
                if s[left] in letter_dict:  # 如果縮減的字母在t中，更新letter_dict
                    if letter_dict[s[left]] == 0: # 如果縮減的字母會導致window不包含全部的t,count-=1
                        count -= 1
                    letter_dict[s[left]] += 1
                left += 1

        return s[min_len_index[0]:min_len_index[1]]




"""424. Longest Repeating Character Replacement"""
class Solution:
    """
    給予一個字串s跟整數k，可以任意替換s中的任意字母為其他字母，求最長的字母完全相同的子字串
    s = "ABAB", k = 2 => 4 (replace both A or B)
    """
    def characterReplacement(self, s: str, k: int) -> int:
        """slinding windows
        求最大的window size
        """
        record_dict = defaultdict(int)
        max_letter_num = 0
        max_letter = ""
        left = 0
        max_window_size = 0
        for right in range(len(s)):
            # move right point
            record_dict[s[right]] += 1
            if record_dict[s[right]] > max_letter_num:
                max_letter_num = record_dict[s[right]]
                max_letter = s[right]

            # move left point
            while (right - left + 1) - k > max_letter_num:
                record_dict[s[left]] -= 1
                if s[left] == max_letter:
                    max_letter_num -= 1
                    for c in record_dict:
                        if record_dict[c] > max_letter_num:
                            max_letter_num = record_dict[c]
                            max_letter = c
                left += 1
            max_window_size = max(max_window_size, right - left + 1)
        return max_window_size




"""713. Subarray Product Less Than K"""
class Solution:
    """ 給予一個nums array，以及一個目標數k，請問nums中有多少個連續的subarray乘績小於k

    input: nums = [1,1,1], k = 2
    output: 6

    input: nums = [10,5,2,6], k = 100
    output: 8
    """
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        """ 使用Slinding Windows解
        題目要問的是有幾個continue sub array符合乘績小於k
        * 給更新一個window size會有幾格continue sub array符合乘績小於k：
        [1] -> 1
        [1, 2] -> 1+2
        [1, 2, 3] -> 1+2+3
        [1, 2, 3, 4] -> 1+2+3+4
        每次更新完，符合條件的window size有 right-left+1個
        """
        left = 0
        ans = 0
        res = 1
        for right in range(len(nums)):
            # 更新目前window size裡的積
            res = res * nums[right]
            # 如果大於k，縮小window size
            while res >= k and left <= right:
                res /= nums[left]
                left += 1
            # 目前合理的windows size有幾個解
            ans += (right - left + 1)
        return ans
