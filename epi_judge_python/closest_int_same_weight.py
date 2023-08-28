from test_framework import generic_test


# 1. Assume 64-bit
# 2. Find the 2 smallest consecutive bits which are different
# 3. Swap them
# 4. Raise ValueError for all 1s or 0s

def closest_int_same_bit_count(x: int) -> int:
    num_unsigned_bits = 64
    for i in range(num_unsigned_bits - 1):
        if (x >> i) & 1 != (x >> (i + 1)) & 1:
            x ^= (1 << i) | (1 << (i + 1))
            return x
    raise ValueError('No closest integer with same bit count')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('closest_int_same_weight.py',
                                       'closest_int_same_weight.tsv',
                                       closest_int_same_bit_count))
