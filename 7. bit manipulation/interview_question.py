def inserting(n, m, i, j):
    """
    m = 1001(9)
    n = 11 (3)
    i = 1
    j = 2
    """
    clear_mask = -1 << (j + 1)
    capture_mask = (1 << i) - 1
    capture_bits = n & capture_mask
    n = (n & clear_mask) | capture_bits
    m = m << i
    ans = m | n
    return ans


print("----------------- inserting -----------------")
ans = inserting(9, 3, 1, 2)
print(bin(ans))
ans = inserting(1024, 19, 2, 6)
print(bin(ans))


def binary_to_string(double):
    if double > 1 or double < 0:
        return "ERROR"

    ans = "0."
    frac = 0.5
    for _ in range(32):
        if double >= frac:
            double -= frac
            ans += "1"
        else:
            ans += "0"
        frac *= 0.5
        if double == 0:
            return ans
    return "ERROR"


print("\n----------------- binary_to_string -----------------")
ans = binary_to_string(0.625)
print(ans)
ans = binary_to_string(0.7)
print(ans)


def flip_bit_to_win(num):
    previous_len = 0
    current_len = 0
    max_len = 0
    while num > 0:
        if (num & 1) == 1:
            current_len += 1
        else:
            max_len = max(max_len, current_len + previous_len)
            previous_len = current_len
            current_len = 0
        num = num >> 1
    return max_len + 1


print("\n----------------- binary_to_string -----------------")
ans = flip_bit_to_win(1775)
print(ans)


def next_number(num):
    """
    num = 10100
    next largest number = 11001
        1. find the rightmost non tailing 0 (at pos p) and flip to 1
        2. count the 1's num right than p (1_num)
        3. set the bits right than p to 0, and set the right most 1_num bits to 1
    next smallest number = 10010
        1. find the non tailing rightmost 1 (at pos p) and flip to 1
        2. flip the p-1 0 to 1
    """
    # get the next number larger than num
    larger_num = -1
    temp_num = num
    zero_count = 0
    one_count = 0
    while (temp_num & 1 == 0) and (temp_num > 0):
        zero_count += 1
        temp_num >>= 1
    while (temp_num & 1 == 1) and (temp_num > 0):
        one_count += 1
        temp_num >>= 1
    p = one_count + zero_count
    if p >= 1:
        clear_mask = -1 << p
        set_p_mask = 1 << p
        set_one_mask = (1 << one_count - 1) - 1
        larger_num = ((num | set_p_mask) & clear_mask) | set_one_mask

    # get the next number smaller than num
    temp_num = num
    zero_count = 0
    one_count = 0
    while (temp_num & 1 == 1) and (temp_num > 0):
        one_count += 1
        temp_num >>= 1
    while (temp_num & 1 == 0) and (temp_num > 0):
        zero_count += 1
        temp_num >>= 1
    p = one_count + zero_count
    clear_mask = -1 ^ (1 << p)
    set_mask = 1 << p - 1
    small_num = (num & clear_mask) | set_mask

    return larger_num, small_num


print("\n----------------- next_number -----------------")
larger_num, small_num = next_number(5)
print(larger_num, small_num)


def conversation(a, b):
    c = 0
    while a > 0 or b > 0:
        if a & 1 != b & 1:
            c += 1
        a >>= 1
        b >>= 1
    return c


print("\n----------------- conversation -----------------")
ans = conversation(29, 15)
print(ans)


def PairwiseSwap(num):
    """
    num = 1011
    1. get odd bit: 0001
    2. get even bit: 1010
    3. even bit >> 1
    4. odd bit << 1
    5. ans = even bit & odd bit # 0111
    """

    mask1 = 0xAAAAAAAA  # 10101010...1010
    mask2 = 0x55555555  # 01010101...0101

    even_bits = num & mask1
    odd_bits = num & mask2
    return (even_bits >> 1) | (odd_bits << 1)


print("\n----------------- PairwiseSwap -----------------")
ans = PairwiseSwap(23)
print(ans)


def draw_line(screen, w, point1, point2):
    """
    screen has int value from 0 to 255
    [00000000, 00000000, 00000000,       [00000000, 00000000, 00000000,
     00000000, 00000000, 00000000,  =>    00011111, 11111111, 11100000,
     00000000, 00000000, 00000000]        00000000, 00000000, 00000000]

     point1 = 3, 1
     point2 = 19, 1
    """
    x1, y = point1
    x2, y = point2

    x1_byte, x1_bit = x1 // 8 + y*w, x1 % 8
    x2_byte, x2_bit = x2 // 8 + y*w, x2 % 8

    # x1 到 x2 之間的byte全設為1
    for i in range(x1_byte+1, x2_byte):
        screen[i] = 255

    if x1_byte == x2_byte: # x1 x2 在同一個byte內
        mask = ((1 << (x2_bit-x1_bit+1)) - 1) << (7-x2_bit)
        screen[x1_byte] |= mask
    else:
        mask = (1 << (8-x1_bit)) -1
        screen[x1_byte] |= mask

        mask = ((1 << x2_bit) - 1) << (7 - x2_bit)
        screen[x2_byte] |= mask


def show_screen(screen, w):
    print("screen:")
    for idx, byt in enumerate(screen):
        if idx%w == 0 and idx != 0:
            print()
        print(bin(byt), " ", end="")
    print()


print("\n----------------- draw_line -----------------")
screen = [0]*9
show_screen(screen, 3)
draw_line(screen, 3, (3,1), (19,1))
show_screen(screen, 3)

screen = [0]*9
show_screen(screen, 3)
draw_line(screen, 3, (17,1), (19,1))
show_screen(screen, 3)

