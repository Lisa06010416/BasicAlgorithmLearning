from typing import List
from collections import defaultdict



"""49. Group Anagrams"""
class Solution:
    """輸入多個 str 找到 Anagram(相同字母組成的字)
    ["eat","tea","tan","ate","nat","bat"]  => [["bat"],["nat","tan"],["ate","eat","tea"]]
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        record_dict = defaultdict(list)
        for s in strs:
            key = tuple(sorted(list(s)))
            record_dict[key].append(s)
        return record_dict.values()



"""128. Longest Consecutive Sequence"""
class Solution:
    """回傳一個未排序的數字array中最長連續整數的數量
    ex [5,1,3,188,2,90,4] => 5
    """
    def longestConsecutive(self, nums: List[int]) -> int:
        num_dict = {} # 擁hash把出現過的數量紀錄
        for n in nums:
            num_dict[n] = None

        max_len = 0
        # 遍歷每個數字，如果數字還在num_dict里則往上下去找是否有連續，找過的數字由num_dict里刪除
        for n in nums:
            if n in num_dict:
                temp_len = 1
                del num_dict[n]
                left, right = n - 1, n + 1
                while left in num_dict:
                    del num_dict[left]
                    temp_len += 1
                    left -= 1
                while right in num_dict:
                    del num_dict[right]
                    temp_len += 1
                    right += 1
                max_len = max(max_len, temp_len)
        return max_len


s = "123"
s = [1,2,3]
print(s[:0])