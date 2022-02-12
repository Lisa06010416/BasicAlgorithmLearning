from collections import defaultdict
from typing import List


class Solution:
    """ Group Anagrams
    Input: strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        record_dict = defaultdict(list)
        for s in strs:
            key = str(sorted(s))
            record_dict[key].append(s)
        return list(record_dict.values())
