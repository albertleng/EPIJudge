from typing import List

from test_framework import generic_test


def h_index(citations: List[int]) -> int:
    total_citation = len(citations)
    citations.sort()
    for index, citation in enumerate(citations):
        if citation >= total_citation - index:
            return total_citation - index

    return 0


if __name__ == '__main__':
    exit(generic_test.generic_test_main('h_index.py', 'h_index.tsv', h_index))
