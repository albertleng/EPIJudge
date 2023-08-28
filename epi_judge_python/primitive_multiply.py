from test_framework import generic_test


# Using helper add
# 1. sum - a ^ b, carry - a & b
# 2. Add y to running_sum if x is 1 via looping x >>1 and y << 1
def multiply(x: int, y: int) -> int:
    def add(a: int, b: int) -> int:
        return a if b == 0 else add(a ^ b, (a & b) << 1)

    running_sum = 0
    while x:
        if x & 1:
            running_sum = add(running_sum, y)
        x, y = x >> 1, y << 1

    return running_sum


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('primitive_multiply.py',
                                       'primitive_multiply.tsv', multiply))
