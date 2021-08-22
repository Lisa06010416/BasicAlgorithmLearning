class Solution:
    """
    give a integer n, encode n in behind way:
    0 = 000000,
    ...,
    999,999 = 999999,
    1,000,000 = 00000A,
    1,000,001 = 00001A,
    ...,
    _ = 99999A,
    _ = 00000B,
    ...,
    _ = 00000Z,
    _ = 00001Z,
    ...,
    _ = 99999Z,
    _ = 0000AZ,
    ...,
    _ = 9ZZZZZ,
    _ = AZZZZZ,
    ...,
    X - 1 = YZZZZZ,
    X = ZZZZZZ.
    """
    def encoder(self, n):
        """
        1000000進位的轉換
        :return:
        """
        result = ""
        remainder = n%1000000
        while n//1000000 > 0:
            quotient = n//1000000
            remainder = n%1000000
            print(n, quotient, quotient%26)
            result += chr((quotient-1)%26+ord('A'))
            n = (quotient//26-1)*1000000 + remainder
        result = str(remainder)+result
        result = "0"*(6-len(result))+result
        return result

s = Solution()
a = s.encoder(25000000)
print(a)
