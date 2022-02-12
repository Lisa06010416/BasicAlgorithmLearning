import math

# ------- log ------------
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        """方法一
        1. 取log
        2. 換底公式
        """
        if n>0 and round(math.log(n, 3), 10) % 1 == 0:
            return True
        return False