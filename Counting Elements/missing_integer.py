"""MissingInteger Solution.

Finds the smallest positive integer (greater than 0) that does not occur in array A.
Codility Complexity: O(N) Time | O(N) Space.
"""

from typing import List


def get_missing_integer(A: List[int]) -> int:
    """Finds the smallest missing positive integer in array A.

    Args:
        A (List[int]): Non-empty array of N integers.

    Returns:
        int: Smallest positive integer not present in A.
    """
    # Filter and collect all positive integers into a set for O(1) lookup
    positive_nums = {x for x in A if x > 0}

    # Search for the first missing positive integer starting from 1
    smallest_missing = 1
    while smallest_missing in positive_nums:
        smallest_missing += 1

    return smallest_missing


def main():
    # Example usage
    A = [1, 3, 6, 4, 1, 2]
    print(get_missing_integer(A))  # Expected output: 5
    A = [1, 2, 3]
    print(get_missing_integer(A))  # Expected output: 4
    A = [-1, -3]
    print(get_missing_integer(A))  # Expected output: 1

if __name__ == "__main__":
    main()