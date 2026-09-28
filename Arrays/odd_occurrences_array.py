

from typing import List


def solution(A: List[int]) -> int:
    """
    Finds the unpaired element in an array where all other elements occur an even number of times.

    Time Complexity: O(N)
    Space Complexity: O(1)

    :param A: List of integers.
    :return: The single unpaired integer, or 0 if empty.
    """
    if not A:
        return 0

    unpaired_element = 0
    for number in A:
        unpaired_element ^= number

    return unpaired_element
   

if __name__ == "__main__":
    """Demonstrates the solution with test cases."""
    test_cases = [9, 3, 9, 3, 9, 7, 9]
    print(solution(test_cases))
   