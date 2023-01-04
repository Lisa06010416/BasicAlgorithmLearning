
import math
import copy

"""8.1 Triple Step"""
class get_step_number:
    def get_step_number_dfs(self, n: int):
        
        def dfs(n, count):
            if n == 0:
                return count + 1
            if n >= 3:
                count = dfs(n-3, count)
            if n >= 2:
                count = dfs(n-2, count)
            if n >= 1:
                count = dfs(n-1, count)
            return count

        return dfs(n, 0)

    def get_step_number_bp(self, n: int):
        """ 
        n==0:  1
        n==1:  1
        n==2:  2 
        n==3:  4  (爬到前 1,2,3個台階的和)
        n==4:  7   
        """
        if n <= 0:
            return 0
        dp = [0] * (n + 1)
        dp[0], dp[1], dp[2] = 1, 1, 2
        if n > 0 and n < 3:
            return dp[n]
        
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        return dp[-1]



step_number = get_step_number()
print("answer:", step_number.get_step_number_dfs(3))
print("answer:", step_number.get_step_number_bp(3))     

"""8.1 Robot in a Grid"""
class Robot_in_a_Grid:
    def Robot_in_a_Grid_dfs_memory(self, board):
        invalid_grid = {}
        r, c = len(board), len(board[0])
        def dfs(board, i, j):
            if i >= r or j >= c:
                return False
            if not board[i][j]:
                return False
            if i == r-1 and j == c-1:
                return True
            for m_i, m_j in zip([0, 1],[1, 0]):
                if (i+m_i, j+m_j) not in invalid_grid and dfs(board, i+m_i, j+m_j):
                    return True
            invalid_grid[(i, j)] = None
            return False
        return dfs(board, 0, 0)

board = [
    [1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1]
    ]
print(Robot_in_a_Grid().Robot_in_a_Grid_dfs_memory(board))
board = [
    [1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 0, 0],
    [1, 1, 1, 0, 1],
    [1, 1, 1, 0, 1]
    ]
print(Robot_in_a_Grid().Robot_in_a_Grid_dfs_memory(board))


"""8.3 Magic Index"""
class MagicIndex:
    #數字不重複，時間複雜度n
    def magic_index_distinct_bigo_n(self, array):
        i = 0
        while i < len(array):
            n = array[i]
            if i==n:
                return True
            elif i < n:
                i = n
            else:
                i += 1
        return False
    
    #數字不重複，時間複雜度logn
    def magic_index_distinct_bigo_logn(self, array):
        left, right = 0, len(array) - 1
        while left <= right:
            mid = left + (right-left)//2
            if mid == array[mid]:
                return True          
            if mid > array[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return False

array = [-5, 1, 2, 9, 10, 19]
print("magic_index_distinct_bigo_n:", MagicIndex().magic_index_distinct_bigo_n(array))
print("magic_index_distinct_bigo_logn:", MagicIndex().magic_index_distinct_bigo_logn(array))
array = [3, 3, 3, 3, 3, 3]
print("magic_index_distinct_bigo_n:", MagicIndex().magic_index_distinct_bigo_n(array))
print("magic_index_distinct_bigo_logn:", MagicIndex().magic_index_distinct_bigo_logn(array))
array = [-9, 5, 7, 11]
print("magic_index_distinct_bigo_n:", MagicIndex().magic_index_distinct_bigo_n(array))
print("magic_index_distinct_bigo_logn:", MagicIndex().magic_index_distinct_bigo_logn(array))


"""8.4 Power Set"""
class PowerSet:
    def power_set(self, elementset: list):
        ans = [[]]  
        for i in range(len(elementset)):
            temp_ans = copy.deepcopy(ans)
            for a in temp_ans:
                a.append(elementset[i])
            ans.extend(temp_ans)           
        return ans

print("Power Set of [1, 2, 3] :", PowerSet().power_set([1, 2, 3]))
assert len(PowerSet().power_set([1, 2, 3, 4, 5, 6, 7])) == math.pow(2,7)


"""8.5 Recursive Multiply"""
class RecursiveMultiply:
    def recursive_multiply(self, x, y):
        ans = 0
        while y >= 2:
            ans += x << 1
            y -=  2
        if y == 1:
            ans += x
        return ans
    
        
print("Recursive Multiply 5, 7 :", RecursiveMultiply().recursive_multiply(5, 7))


"""8.6 Towers of Hanoi"""
class TowersOfHanoi:
    def towers_of_hanoi(self, disk_num):
        def move(disk_num, tower_start, tower_mid, tower_end):
            if disk_num == 1:
                print("Move disk from", tower_start, "to", tower_end)
                return
            move(disk_num-1, tower_start, tower_end, tower_mid)
            print("Move disk from", tower_start, "to", tower_end)
            move(disk_num-1, tower_mid, tower_start, tower_end)
        move(disk_num, 'A', 'B', 'C')

print("\nTowers of Hanoi: 2 disk")
TowersOfHanoi().towers_of_hanoi(3)


"""8.7 Permutations without Dups"""
class PermutationsWithoutDups:
    def get_permutations_dfs(self, s):
        char_list = [i for i in s]
        ans = []

        def dfs(temp_ans):
            if len(temp_ans) == len(s):
                ans.append(temp_ans)

            for i in range(len(s)):
                if char_list[i] != "_":
                    temp = char_list[i]
                    char_list[i] = "_"
                    dfs(temp_ans + [s[i]])
                    char_list[i] = temp
        dfs([])
        return ans

    def get_permutations_bfs(self, s):
        """
        ex s = "abc"
        a
        _a_  => 有兩個位子插入b
        _a_b_ => 有三個位子插入b
        """
        char_list = [i for i in s]
        ans = []
        queue = [[char_list[0]]]

        while queue:
            temp_permu = queue.pop(0)
            temp_len = len(temp_permu)
            for i in range(temp_len+1):
                new_permu = temp_permu[:i] + [s[temp_len]] + temp_permu[i:]
                if len(new_permu) == len(s):
                    ans.append(new_permu)
                else:
                    queue.append(new_permu)
        return ans
                
                

print("\nPermutations without Dups")
print(PermutationsWithoutDups().get_permutations_dfs("abc"))
print(PermutationsWithoutDups().get_permutations_bfs("abc"))


"""8.8 Permutations without Dups
47. Permutations II
"""
class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        res = set()
        def get_all(nums, ans):
            if len(ans) == len(nums):
                ans = tuple(ans)
                if ans not in res:
                    res.add(ans)
                return
            
            for n_idx, n in enumerate(nums):
                if n != "_":
                    nums[n_idx] = "_"
                    get_all(nums, ans + [n])
                    nums[n_idx] = n
        get_all(nums, [])
        return res


"""
8.9 Parens
22. Generate Parentheses
"""
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        def age_ans(temp_n, stack, ans):
            if not stack and len(ans) == n*2:
                res.append(ans)  
                return
            
            if temp_n > 0:
                stack.append(")")
                age_ans(temp_n-1, stack, ans + "(")
                stack.pop()
            
            if stack:
                ans += stack.pop()
                age_ans(temp_n, stack, ans)
                stack.append(")")
        
        age_ans(n, [], "")       
        return res


"""
8.14 Boolean Evaluation
"""
def countParenth(symb, oper, n):
    F = [[0 for i in range(n + 1)]
         for i in range(n + 1)]
    T = [[0 for i in range(n + 1)]
         for i in range(n + 1)]
 
    # base case : 只對一個symbol加括號
    for i in range(n):
        if symb[i] == 'F':
            F[i][i] = 1
        else:
            F[i][i] = 0
 
        if symb[i] == 'T':
            T[i][i] = 1
        else:
            T[i][i] = 0
 
    # Now fill T[i][i+1], T[i][i+2],
    # T[i][i+3]... in order And
    # F[i][i+1], F[i][i+2],
    # F[i][i+3]... in order

    print("i j k")
    for gap in range(1, n):
        i = 0
        for j in range(gap, n):
            T[i][j] = F[i][j] = 0
            for g in range(gap):
 
                # Find place of parenthesization
                # using current value of gap
                k = i + g
                
                print(i,j,k)
                # Store Total[i][k] and Total[k+1][j]
                tik = T[i][k] + F[i][k]
                tkj = T[k + 1][j] + F[k + 1][j]
 
                # Follow the recursive formulas
                # according to the current operator
                if oper[k] == '&':
                    T[i][j] += T[i][k] * T[k + 1][j]
                    F[i][j] += (tik * tkj - T[i][k] *
                                T[k + 1][j])
                if oper[k] == '|':
                    F[i][j] += F[i][k] * F[k + 1][j]
                    T[i][j] += (tik * tkj - F[i][k] *
                                F[k + 1][j])
                if oper[k] == '^':
                    T[i][j] += (F[i][k] * T[k + 1][j] +
                                T[i][k] * F[k + 1][j])
                    F[i][j] += (T[i][k] * T[k + 1][j] +
                                F[i][k] * F[k + 1][j])
            i += 1
    return T[0][n - 1]
        
symbols = "TTFT"
operators = "|&^"
n = len(symbols)
a = countParenth(symbols, operators,  n)
print(a)
