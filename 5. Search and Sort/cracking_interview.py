def find_duplicate(nums):
    def get_bite(i):
        mask = (1 << i)
        return record_bits & mask
    def set_bite(i):
        mask = 1 << i
        return record_bits | mask
    ans = []
    record_bits = 0
    for n in nums:
        if get_bite(n):
            ans.append(n)
        else:
            record_bits = set_bite(n)
    return ans


print("\nfind_duplicate:")
ans = find_duplicate([1,5,1,10,12,10])
print(ans)


def sorted_matric_search(board, target):
    if not board:
        return (-1, -1)
    m, n = len(board), len(board[0])
    i, j = 0, n-1
    while i < m  and j >= 0:
        if board[i][j] == target:
            return (i, j)
        elif board[i][j] > target:
            j -= 1
        else:
            i += 1
    return (-1, -1)

print("\nsorted_matric_search:")
board = [[1, 2, 3, 4, 5], [2, 10, 13, 14, 17], [6, 11, 20, 21, 24]]
ans = sorted_matric_search(board, 10)
print(ans)
ans = sorted_matric_search(board, 25)
print(ans)
ans = sorted_matric_search(board, 7)
print(ans)
