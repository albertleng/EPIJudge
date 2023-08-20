from test_framework import generic_test

'''
WRONG REQUIREMENT
input = +ve int, output = int
E.g. 10 (1010) => 4

10 / 2 => 5 / 2 => 2 / 2 => 1 / 2 => 1
1010 => 0101 => 010=> 1 => 0



8 (1000)  => 4
8 / 2 => 4 / 2 => 2 / 2 => 1 / 2 => 1

7 (111) => 3
7 / 2 => 3 / 2 => 1 / 2 => 1 
   
2 (10)

'''

# WRONG REQUIREMENT
# Count bits
# def count_bits(x: int) -> int:
#     num_bit = 0
#     while x > 0:
#         x >>= 1
#         num_bit += 1
#     return num_bit


# Count bit that is set to 1.
'''
Input: + int, Output: int

E.g.
10 (1010) -> 2
Loop through the bits via >> 2, test one bit at a time via AND 1
    - 101(0) & 1 -> 0
    - 10(1) & 1 -> 1
    - 1(0) & 1 -> 0
    - (1) & 1 -> 1
    Sum them up

2 (10) -> 1
    - 1(0) & 1 -> 0
    - (1) & 1 -> 1
    Sum them up

'''


def count_bits(x: int) -> int:
    num_bit = 0
    while x:
        num_bit += x & 1
        x >>= 1
    return num_bit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('count_bits.py', 'count_bits.tsv',
                                       count_bits))
