def ReSpace(text, dictionary):
    """
    dfs, dp
    dp[i]: the min wordnum from text[0] to  text[i]
    dp[i] = min(dp[0], ..., dp[j]) if text j-i  is a word
            + 1
    """
    dp = [-1 for _ in range(len(text)+1)]
    dp_text = ["" for _ in range(len(text)+1)]
    dp[0] = 0
    for i in range(len(text)+1):
        for j in range(0, i):     
            if text[j:i] in dictionary and dp[j] >= 0:
                if dp[i] <= 0:
                    dp[i] =  dp[j] + 1
                    dp_text[i] = dp_text[j] + " " + text[j:i]
                else:
                    dp[i] = min(dp[i], dp[j] + 1)
                    if dp[i] > dp[j] + 1:
                        dp_text[i] = dp_text[j] + " " + text[j:i]
    return dp[-1], dp_text[-1]

text = "jesslookedjustliketimherbrother"
dictionary = set(["jess", "looked", "just", "like",  "tim", "her", "brother"])
print(ReSpace(text, dictionary)) # (7, ' jess looked just like tim her brother')
    
