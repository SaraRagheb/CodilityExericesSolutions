"""PermCheck Solution.

Checks whether array A is a permutation (contains all numbers from 1 to N exactly once).
Codility Complexity: O(N) Time | O(N) Space.
"""

from typing import List


def check_permutation(A: List[int]) -> int:
    """Determines if an array is a valid permutation.

    Args:
        A (List[int]): Non-empty array of integers.

    Returns:
        int: 1 if array A is a permutation, 0 otherwise.
    """
    if not A:
        return 0

    n = len(A)
    seen_elements = set()

    for num in A:
        # If element is out of range [1..N] or already seen (duplicate), it's not a permutation
        if num < 1 or num > n or num in seen_elements:
            return 0
        seen_elements.add(num)

    return 1 if len(seen_elements) == n else 0


def main():
    # Example usage
    A = [4, 1, 3, 2]
    print(check_permutation(A))  # Expected output: 1 (valid permutation)

    B = [4, 1, 3]
    print(check_permutation(B))  # Expected output: 0 (not a permutation)

if __name__ == "__main__":
    main()