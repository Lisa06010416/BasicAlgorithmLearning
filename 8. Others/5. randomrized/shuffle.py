import random
from typing import List

"""384. Shuffle an Array"""
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        nums = self.nums.copy()
        for i in range(len(self.nums)):
            j = random.randint(0, i)
            nums[i], nums[j] = nums[j], nums[i]
        return nums