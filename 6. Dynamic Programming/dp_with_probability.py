class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        """dp + probability
        在可以抽得牌點數由 [1-maxPts] 間 當抽到點數大於等於 k 就停止時 點數 <= n的機率是多少


        state：
        dp[i] : 表示之前累計的點數為i的機率
        len(dp) = k + maxPts  (因為抽到k點就不會再抽牌,最多抽到k + maxPts -1點)

        translate method: 會需要分3種狀況,

        1. i < maxPts
            dp[i] = 1/maxPts
            累計點數小於小於 maxPts 時點數機率都是一樣的
        2. k >= i > maxPts
            dp[i] = 1/maxPts*(dp[i-1], dp[i-2], ..., dp[i-maxPts]),
            累計點數在 maxPts 到 k之間的點數, ex 11 點 : (1,10), (2,9), ..., (10,1)
                1. 抽最後一張牌的機率都是 1/maxPts
                2. 1/maxPts*dp[1] + 1/maxPts*dp[2] +...+ 1/maxPts*dp[10] = 1/maxPts*(dp[1] + ... + dp[10])
        3. i >= k
            dp[i] = dp[k-1]...+dp[i-maxPts]
            累計點數在 16 以上的情況(大於等於15就不抽牌了) ex i=17 (14,3), (13,4), ... (7, 10)


        ans:
        題目求點數小於等於n, 且大於等於k時的機率 p(<=n|>=k) = p(<=n && >=k) / p(>=k)

        --------- ex n=21, k=15, maxPts=10 ------------

        dp[0] => 1

        dp[1] => 1/10

        dp[2] => 1/10 + 1/10*1/10
                 (0,2)  (1,1)

        dp[3] => 1/10*dp[0] + 1/10*dp[1] + 1/10*dp[2]
                  (0,3)          (1,2)      (2,1)
        ...

        dp[10] => 1/10*dp[0] + 1/10*dp[1] + 1/10*dp[2] + ... + 1/10*dp[9]
                    (0,10)                                        (9,1)



        ...

        dp[15] => 1/10*dp[5] + 1/10*dp[1] + 1/10*dp[2] +...+ 1/10*dp[14]
                  (5,10)                                          (14,1)

        dp[16] => 1/10*dp[5] + ... + 1/10*dp[14]

        """

        # init dp
        dp = [0] * (k + maxPts)
        dp[0] = 1

        # use acculmulate sum to speed up
        # sum_dp = [0]*(k + maxPts)
        # sum_dp[0] = 1

        for i in range(1, len(dp)):
            if i <= k:
                for j in range(max(0, i - maxPts), i):
                    dp[i] += dp[j] / maxPts
            else:
                for j in range(i - maxPts, k):
                    dp[i] += dp[j] / maxPts

        return sum(dp[k:n + 1]) / sum(dp[k:])
