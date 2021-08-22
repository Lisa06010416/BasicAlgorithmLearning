class Solution:
    def longestPalindrome(self, input_string: str) -> str:
        # 1. 用特數字元插在中間，不用判斷奇數或偶數長度的回文
        input_string = "%"+"%".join([i for i in input_string]) +"%"
        # 計算最長的回文
        longest_palindrome = ""
        max_len = 0  # 計算長度時 回文的半徑 = 回文時記得長度(沒有擦入特殊符號前的)
        for i,c in enumerate(input_string):
            win_size = 0
            while i-win_size >= 0 and i+win_size < len(input_string):
                if input_string[i-win_size] != input_string[i+win_size]:
                    break
                win_size+=1
            win_size-=1 # !! 因為前面是 先加在判斷 這裡要對win_size-1

            if max_len < win_size:
                max_len = win_size
                longest_palindrome = input_string[i-win_size:i+win_size+1]

        return longest_palindrome.replace("%","")