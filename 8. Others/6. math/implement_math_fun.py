"""50. Pow(x, n)"""
class Solution:
    """ 對一個任意正負小數 x 取 n 次方 (n可為正負)
    """
    def _get_power(self, x, n):
        if n == 0:
            return 1
        half = self._get_power(x, n // 2)
        if n % 2 == 1:
            return half * half * x
        else:
            return half * half

    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        return self._get_power(x, n)


"""69. Sqrt(x)"""
class Solution:
    """Implement Sqrt(x)"""
    def mySqrt(self, x: int) -> int:
        """
        [0,1,2,3,4,5,6]
        left, right = 0,6
        mid = 3, 1, 2, break
        left = 0, 2, 3
        right = 2, 2, 2

        [0,1,2,3,4]
        left = 0, 2
        right = 2, 2
        mid = 1, 2 -> euqal

        [0,1,2]
        mid = 1, 2, break
        left = 2, 2
        right = 2, 1

        [0,1,2,3,4,5,6,7,8,9]
        mid = 2, 3, break
        left = 3, 2
        right = 4, 1
        """
        # binary search
        if x <= 1:
            return x

        left, right = 0, x // 2
        while left <= right:
            mid = left + (right - left) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1
        return right