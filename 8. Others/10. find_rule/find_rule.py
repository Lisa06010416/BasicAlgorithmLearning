"""400. Nth Digit"""
class Solution:
    def findNthDigit(self, n: int) -> int:

        """
        1 2 3 4 5 6 7 8 9 => 9

        10 11 12 13 .. 99 =>  9+90*2 = 189

          * -> 9 + 90*2 + (3) => remainder
        100 ... 999 +> 9 + 90*2 + 900*3

        1. n => digital_num
        2. get remainder
        3. q,r = remainder/digital_num -> use q,r to find target digit
           1. if r > 0 -> the q-th number
           2. if r == 0 -> the q-1th number
        """
        if n <= 9:
            return n
        digit_num = 1
        previous_num = 0
        while True:
            temp_num = 9 * (10 ** (digit_num - 1)) * digit_num
            if n > previous_num + temp_num:
                previous_num += temp_num
                digit_num += 1
            else:
                break
            # print(previous_num, temp_num)
        remainder_num = n - previous_num
        q, r = remainder_num // digit_num, remainder_num % digit_num
        # print(digit_num, remainder_num, previous_num, q, r)
        if r > 0:
            # print(10**(digit_num-1) + q)
            return int(str(10 ** (digit_num - 1) + q)[r - 1])
        else:
            return int(str(10 ** (digit_num - 1) + q - 1)[-1])


"""397. Integer Replacement"""
class Solution:
    def integerReplacement(self, n: int) -> int:
        """
        1. recursive
        2. find rule
        2, 4, 8, 16 ..
        11 -> 12 -> 6 -> 3 -> 4 -> 2 -> 1
        11 -> 10 -> 5 -> 4 -> 2 -> 1

        10 -> 5 -> 4 ...

        13 -> 12 -> 6 -> 3 -> 2 -> 1
        13 -> 14 -> 7 -> 8 -> 4 -> 2 -> 1

        while True:
            1. n is even => n = n//2
            2. n is odd =>
               a. if  (n+1)//2%2 == 0 -> n += 1
               b. else n -= 1
        """

        round_time = 0
        while True:
            if n == 1:
                break

            is_even = True if n % 2 == 0 else False
            if is_even:
                n = n // 2
            else:
                if n == 3:
                    n -= 1
                elif (n + 1) % 4 == 0:
                    n += 1
                else:
                    n -= 1
            round_time += 1
        return round_time