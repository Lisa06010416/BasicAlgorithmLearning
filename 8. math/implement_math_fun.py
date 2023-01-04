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


"""372. Super Pow"""


"""166. Fraction to Recurring Decimal"""
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        """
        有理數(rational number)為可以表達為兩個整數比的數
        可以變成分數的都是有理數，有理數都是有限的小數或是無限循環小數，不會有無線不循環小數的存在

        整數長除法 - 當除到餘數時給餘數補零再繼續除，當出現重複的餘數時表時出現循環
        """
        # sign
        sign1 = True if numerator >= 0 else False
        sign2 = True if denominator >= 0 else False

        # abs - 非python : 再把數取絕對值時要處理整數overfloat的問題
        numerator = abs(numerator)
        denominator = abs(denominator)

        # record remainder which has appeared
        repeat_remainder_dict = {}

        # cal decimal
        ans = ""
        r = numerator % denominator

        idx = 0  # record the idx of each num
        while r:
            n = r * 10 // denominator
            r = r * 10 % denominator
            if r in repeat_remainder_dict:  # repeat
                repeat_idx = repeat_remainder_dict[r]
                ans = ans[:repeat_idx + 1] + "(" + ans[repeat_idx + 1:] + str(n) + ")"
                break
            else:
                repeat_remainder_dict[r] = idx
                ans += str(n)
            idx += 1

        q = numerator // denominator
        if ans:
            ans = str(q) + "." + ans
        else:
            ans = str(q)

        if ans != "0" and sign1 ^ sign2:
            ans = "-" + ans

        return ans