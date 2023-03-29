from typing import List

""" 41. First Missing Positive """
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        constanse space, O(n) time
        1. cannot sort, record dict

         0 1 2
        [1,2,0] -> miss 3

         0 1 2       0 1 2
        [-3,3,1] -> [1,3,-3] -> miss 2

         0   1    2
        [7, -3, 10]  -> miss 1

        * [1,1] -> 相同值不換
        * [4,2,0,1] -> 要回圈換位子

        1. a for loop
            0 < n < len(nums) -1 -> n is a valid num
              move it to correct pos
        2. check the incorrect pos and get ans
        """

        for idx_n in range(len(nums)):
            while idx_n != nums[idx_n] - 1 and \
                    (1 <= nums[idx_n] and nums[idx_n] <= len(nums)):
                n = nums[idx_n]
                if nums[n - 1] == nums[idx_n]:
                    break
                nums[n - 1], nums[idx_n] = nums[idx_n], nums[n - 1]

        for idx_n, n in enumerate(nums):
            if idx_n != n - 1:
                return idx_n + 1

        return len(nums) + 1

"""LeetCode 348. Design Tic-Tac-Toe 设计井字棋游戏"""
class TicTacToe():
    """
    Given n = 3, assume that player 1 is "X" and player 2 is "O" in the board.

    TicTacToe toe = new TicTacToe(3);

    toe.move(0, 0, 1); -> Returns 0 (no one wins)
    |X| | |
    | | | |    // Player 1 makes a move at (0, 0).
    | | | |
    """
    def __init__(self, n):
        self.n = n
        self.row = [0]*n
        self.col = [0] * n
        self.diagonal = [0] * n
        self.anti_diagonal = [0] * n

    def move(self, p_row, p_col, role):
        if role == 1:
            self.row[p_row] += 1
            self.col[p_col] += 1
            if p_row == p_col:
                self.diagonal[p_row] += 1
            if p_row + p_col == self.n - 1:
                self.anti_diagonal[p_row] += 1
        else:
            self.row[p_row] -= 1
            self.col[p_col] -= 1
            if p_row == p_col:
                self.diagonal[p_row] -= 1
            if p_row + p_col == self.n - 1:
                self.anti_diagonal[p_row] -= 1

        if abs(self.row[p_row]) == self.n or \
                abs(self.col[p_col]) == self.n or \
                abs(self.diagonal[p_row]) == self.n or \
                abs(self.anti_diagonal[p_row]) == self.n:
            return 1
        return 0

tic = TicTacToe(3)
print(tic.move(0,0,1))
print(tic.move(1,0,1))
print(tic.move(2,0,1))


"""Palindrome Permutation"""
def check_permutation_palindrome(input_str):
    record_int = 0

    for i in s:
        record_int = record_int ^ (1 << (ord(i) - ord('0')))
    return True if not record_int else False

print("\nPalindrome Permutation: ")
print("aa: ", check_permutation_palindrome("aa"))
print("aac: ", check_permutation_palindrome("aac"))
print("aacd: ", check_permutation_palindrome("aacd"))
print("aacdedc: ", check_permutation_palindrome("aacdedc"))
print("aacdedce: ", check_permutation_palindrome("aacdedce"))
print("'': ", check_permutation_palindrome(""))


"""String Compression"""
def str_compression(char_list):
    """
    input:
    abcdeeeeeeeazz
    ->
    abcde7_____az2
    ->
    ______abcde7az2
    ->
    a1b1c1d1e7a1z2
    """
    p1, p2 = 0, 0
    while p1 < len(char_list):
        while p2 < len(char_list) and char_list[p2] == char_list[p1]:
            p2 += 1
        c_num = p2 - p1

        p1 += 1
        if c_num > 1:
            char_list[p1] = str(c_num)
            p1 += 1
            while p1 < p2:
                char_list[p1] = "_"
                p1 += 1

    p1, p2 = len(char_list)-1, len(char_list)-1
    while p2 >= 0:
        # find space
        while p1 >= 0 and char_list[p1] != "_":
            p1 -= 1

        # find char/digit after space
        p2 = min(p2-1, p1-1)
        while p2 >= 0 and char_list[p2] == "_":
            p2 -= 1
        # swap
        if p2 >= 0:
            char_list[p1], char_list[p2] = char_list[p2], char_list[p1]

    p1, p2 = 0, 0
    # find char/digit after space
    while p2 < len(char_list) and char_list[p2] == "_":
        p2 += 1

    while p2 < len(char_list):
        # + 1?
        add_one = False
        if char_list[p2].isalpha() and \
            (p2 + 1 >= len(char_list) or char_list[p2+1].isalpha()):
            add_one = True

        # swap
        char_list[p1], char_list[p2] = char_list[p2], char_list[p1]

        # move point
        if add_one:
            p1 += 1
            char_list[p1] = "1"
        p1 += 1
        p2 += 1

input = ["a","b","c","e","e","e","e","e","e","x","z","z"]
str_compression(input)
print(input)



