from typing import List

"""190. Reverse Bits"""
class Solution:
    """reverse 32 bits  11001 => 10011"""
    def reverseBits(self, n: int) -> int:
        bin_n = bin(n)[2:]
        return int("0b" + bin_n[::-1] + "0" * (32 - len(bin_n)), 2)


"""191. Number of 1 Bits"""
class Solution:
    """計算輸入bit的1的數量"""
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')


"""371. Sum of Two Integers"""
class Solution(object):
    """在不使用 + - 的情況下做兩數相加"""
    def getSum(self, a:int, b:int):
        """
        用bit做相加 ex 4(100) + 7(111) = 11(1011)
        1. 不考慮進位 1 (1) ，做xor運算
        2. 進位 10 (1010)，做 and運算在左移一位
        3. 和剛好是1.2.兩數相加，要相加的部分在繼續重複1.2.直到2.值為0
        4. 負數的部分，調用 ＆ mask, 且最終的回傳值要用MAX判斷
        """
        # 32 bits integer max
        MAX = 0x7FFFFFFF
        # 32 bits interger min
        MIN = 0x80000000
        # mask to get last 32 bits
        mask = 0xFFFFFFFF
        # print(bin(a), bin(b))
        while b != 0:
            # ^ get different bits and & gets double 1s, << moves carry
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
            # print(bin(a), bin(b))
        # if a is negative, get a's 32 bits complement positive first
        # then get 32-bit positive's Python complement negative
        return a if a <= MAX else ~(a ^ mask)


"""268. Missing Number"""
class Solution:
    """ 給一個組數，找出遺失的數字 ex nums = [3,0,1] => 2
    時間複雜度 O(n) 空間複雜度 O(1)

    相似題：Single Number 1~3
    """
    def missingNumber_math(self, nums: List[int]) -> int:
        # 等差數列求和的公式 - 組數和
        nums_size = len(nums)
        return int((1 + nums_size) * nums_size / 2 - sum(nums))

    def missingNumber_bit(self, nums: List[int]) -> int:
        """
        將少了一個樹的nums跟完整的組數 xor，則相同的變為0，剩下的就是缺少的數
        nums = [3, 0 ,1]
        res = 0
        3(011)  xor  1(001) xor res => res = 010
        0(000)  xor  2(010) xor res => res = 000
        1(001)  xor  3(011) xor res => res = 010
        """
        # 相似題 Single Number 系列題
        # xor
        res = 0
        for i in range(0, len(nums)):
            res ^= (i + 1) ^ nums[i]
            print(i, nums[i], bin(i), bin(nums[i]), bin(i ^ nums[i]))
            print(res, bin(res))
        return res



"""287. Find the Duplicate Number"""
class Solution:
    """Give a array og intergers, has n+1 items, and each val in between 1~n,
    There is only on repeated number, please find out the number
    限制 : 不可以改變輸入的組數，也只能用 constant extra space (不可以用sort)
    solution 1: 鴿籠原理 + binary search
    solution 2: Bit Manipulation
    solution 3: fast/low point (不是常數的空間)
    solution 4: sort and find repeat (會改變nums)
    """
    def findDuplicate(self, nums: List[int]) -> int:
        """
        bit manipulation
        如果兩個數列的數相等，則每一個bit為1的數會相等
        """
        ans = ""
        for i in range(1, 33):
            cnt1 = 0  # 紀錄 nums 中 bit i 為1的數量
            cnt2 = 0  # 紀錄 1-n-1 中 bit i 為1的數量
            for n in nums:
                if len(bin(n)) - 2 >= i and bin(n)[-i] == "1":
                    cnt1 += 1
            for n in range(1, len(nums)):
                if len(bin(n)) - 2 >= i and bin(n)[-i] == "1":
                    cnt2 += 1

            if cnt1 > cnt2:
                ans = "1" + ans
            else:
                ans = "0" + ans
        return int("0b" + ans, 2)
