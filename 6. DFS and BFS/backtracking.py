from typing import List


"""39. Combination Sum"""
class Solution:
    """找到給予的 candidates list 中,任選element(可重複選)，讓選出的element和為target
    返回全部可能的組合
    """
    def get_combine(self, candidates, target, ans):
        if target < 0:
            return
        if target == 0:
            temp_ans = ans.copy()
            temp_ans.sort()
            if temp_ans not in self.combination:
                self.combination.append(temp_ans)
            return

        for c in candidates:
            ans.append(c)
            self.get_combine(candidates, target - c, ans)
            ans.pop(-1)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.combination = []
        self.get_combine(candidates, target, [])
        return self.combination

