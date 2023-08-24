from test_framework import generic_test

'''
1. check if the two bits are the same
    - >> i and >> j and compare
2. if diff, use bit masks 1 << i and 1 <<j and XOR as x ^ 1 = ~x
'''


def swap_bits(x, i, j):
    if (x >> i) & 1 != x >> j & 1:
        bit_mask = (1 << i) | (1 << j)
        x ^= bit_mask
    return x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('swap_bits.py', 'swap_bits.tsv',
                                       swap_bits))
