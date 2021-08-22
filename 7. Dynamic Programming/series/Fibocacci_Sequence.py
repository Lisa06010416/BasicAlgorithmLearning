import math

"""
dp[i] = dp[i-2] + dp[i-1]
* 在排列組合時，可以跟前或後組合
"""


"""70. Climbing Stairs"""
class Solution:
    """有n層階梯，每次可以爬一層或兩層，有幾種爬法"""
    def climbStairs(self, n: int) -> int:
        num_way = 1
        for i in range(1, n // 2 + 1):
            num_way += math.factorial(n - i) / (math.factorial(n - 2 * i) * math.factorial(i))
        return int(num_way)



"""91. Decode Ways"""
class Solution:
    """ 給予一串數列，有幾種可能的解法方式
    1 => A, 2 => B, ..., Z => 26

    input = "12109"  => output = 2
    """
    def numDecodings(self, s: str) -> int:
        dp = [1, 1]
        if not s or s[0] == "0":
            return 0

        for index, char in enumerate(s):
            if index == 0:
                continue

            int_num = int(s[index - 1:index + 1])
            if s[index] == "0":
                if int_num not in [10, 20]:
                    dp.append(0)
                    break
                dp.append(dp[-2])
            elif int_num <= 26 and int_num >= 11:
                dp.append(dp[-2] + dp[-1])
            else:
                dp.append(dp[-1])

            if dp[-1] <= 0:
                break
        return max(dp[-1], 0)

