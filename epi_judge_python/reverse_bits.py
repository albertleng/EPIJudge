from test_framework import generic_test


# Solution 1: Using pre-calculated cache
def compute_reverse_bits(i: int) -> int:
    start = 0
    end = 15  # last index of a 16-bit integer

    while start < end:
        if (i >> start) & 1 != (i >> end) & 1:
            bit_mask = (1 << start) | (1 << end)
            i ^= bit_mask
        start += 1
        end -= 1
    return i


def reverse_bits(x: int) -> int:
    precomputed_reverse_bits = [compute_reverse_bits(i) for i in range(65535)]
    mask_size = 16
    bit_mask = 0xFFFF
    return precomputed_reverse_bits[x & bit_mask] << (3 * mask_size) | precomputed_reverse_bits[
        (x >> mask_size) & bit_mask] << (2 * mask_size) | precomputed_reverse_bits[
        (x >> (2 * mask_size)) & bit_mask] << mask_size | precomputed_reverse_bits[(x >> (3 * mask_size)) & bit_mask]


# Solution 2: Without cache. It seems to be faster
# def reverse_bits(i: int) -> int:
#     start = 0
#     end = 63  # last index of a 64-bit integer
#
#     while start < end:
#         if (i >> start) & 1 != (i >> end) & 1:
#             bit_mask = (1 << start) | (1 << end)
#             i ^= bit_mask
#         start += 1
#         end -= 1
#     return i

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits))
