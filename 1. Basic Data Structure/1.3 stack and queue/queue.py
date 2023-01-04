from collections import deque

"""239. Sliding Window Maximum"""
class Solution:
    def maxSlidingWindow_monotonic_queue(self, nums: List[int], k: int) -> List[int]:
        """
        1. use deque
        2. only store need value (max and new)
        3. if the top value if the index is out of windows remove it

        nums = [1,3,-1,-3,5,3,6,7], k = 3
        que = []
        que = [1]
        que = [1,3]  1 < 3 移除 -> que = [3]
        que = [3, -1]  3 > -1 不移除
        ...

        遍歷nums把值加入queue中，如果que中第一個元素在windows外則移除
        如果新加入的值比queue中尾端的值還大則一直移除queue尾端的值
        加queue中top的值加到ans中
        """
        if not nums or k <= 0:
            return []
        if len(nums) < k:
            return []

        que = deque([])
        ans = []

        for n_idx, n in enumerate(nums):
            while que and que[0][0] <= n_idx - k:
                que.popleft()
            while que and que[-1][1] <= n:
                que.pop()
            que.append((n_idx, n))
            if n_idx >= k - 1:
                ans.append(que[0][1])
        return ans