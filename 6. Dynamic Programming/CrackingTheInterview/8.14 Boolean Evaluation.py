"""
8.14 Boolean Evaluation
"""


def print_array(array, text):
    print(f"{text} : ")
    for a in array:
        print(a)
    print()


def get_num(symbols, operators, ans):
    T = [[0]*len(symbols) for i in range(len(symbols))]   #T[i][j] = 在 symbols[i]-symbols[j] 加上括號結果會是True的數量
    F = [[0]*len(symbols) for i in range(len(symbols))]   #T[i][j] = 在 symbols[i]-symbols[j] 加上括號結果會是True的數量

    # Base Case
    for i in range(len(symbols)):
        T[i][i] = 1 if symbols[i] else 0
        F[i][i] = 0 if symbols[i] else 1
    
    # 轉移方程式
    for jump in range(1, len(symbols)): # 要跨幾的symbol加括號
        for i in range(len(symbols)): # 重第幾個symbol開始加括號
            j = i + jump # 括號加到到第幾個symbol
            if j >= len(symbols):
                break
            for k in range(i, j): # 在第k個symbol斷開，使用operators[k]
                total_ik = T[i][k] + F[i][k]
                total_kj = T[k+1][j] + F[k+1][j]
                if operators[k] == "&":
                    T[i][j] += T[i][k] * T[k+1][j]
                    F[i][j] += total_ik * total_kj - T[i][k] * T[k+1][j]
                elif operators[k] == "|":
                    T[i][j] += total_ik * total_kj - F[i][k] * F[k+1][j]
                    F[i][j] += F[i][k] * F[k+1][j]
                elif operators[k] == "^":
                    T[i][j] += T[i][k] * F[k+1][j] + F[i][k] * T[k+1][j]
                    F[i][j] += T[i][k] * T[k+1][j] + F[i][k] * F[k+1][j]
                print("jump:", jump, "i:", i, "j:", j, "k:", k, "total_ik", total_ik, "total_kj", total_kj)
                print_array(T, "T:")
                print_array(F, "F:")
    
    if ans:
        return T[0][len(symbols)-1]
    else:
        return F[0][len(symbols)-1]



symbols, operators, ans = [1,1,0,1], ["|", "&", "^"], 1
print(get_num(symbols, operators, ans))
