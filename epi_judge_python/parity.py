from test_framework import generic_test

'''
The parity of a binary word is 1 if the numbe of 1s in the word is odd; otherwise, it is 0.
'''


# 1. Bruce Force
# def parity(x: int) -> int:
#     result = 0
#     while x:
#         result ^= x & 1
#         x >>= 1
#     return result


# 2. Via looping of resetting the 1st bit of x and XOR result
# def parity(x: int) -> int:
#     result = 0
#     while x:
#         result ^= 1
#         x &= x - 1 # Reset the 1st set bit
#     return result

# 3.
# def parity(x: int) -> int:
#     x ^= x >> 32
#     x ^= x >> 16
#     x ^= x >> 8
#     x ^= x >> 4
#     x ^= x >> 2
#     x ^= x >> 1
#
#     return x & 1

def compute_parity(x: int) -> int:
    result = 0
    while x:
        result ^= 1
        x &= x - 1
    return result


MASK_SIZE = 16
BIT_MASK = 0xFFFF


def parity(x: int) -> int:
    # Create a lookup table for 16-bit numbers
    parity_lookup = [compute_parity(i) for i in range(65536)]

    return (parity_lookup[x & BIT_MASK] ^
            parity_lookup[(x >> MASK_SIZE) & BIT_MASK] ^
            parity_lookup[(x >> (2 * MASK_SIZE)) & BIT_MASK] ^
            parity_lookup[(x >> (3 * MASK_SIZE)) & BIT_MASK])


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
