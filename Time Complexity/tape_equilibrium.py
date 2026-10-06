
"""TapeEquilibrium Solution.

Finds the minimum absolute difference between the sum of two parts of an array 
after splitting it at an optimal index P.

Codility Complexity: O(N) Time | O(1) Space.
"""

from typing import List


def get_minimum_difference(A: List[int]) -> int:
    """Calculates the minimal difference achievable by splitting array A.

    Args:
        A (List[int]): A non-empty array of N integers.

    Returns:
        int: The minimal absolute difference between the two split parts.
    """
    total_sum = sum(A)
    left_sum = A[0]
    right_sum = total_sum - left_sum
    min_diff = abs(left_sum - right_sum)

    # Iterate through valid split positions P from index 1 to N - 1
    for p in range(1, len(A) - 1):
        left_sum += A[p]
        right_sum -= A[p]
        current_diff = abs(left_sum - right_sum)
        min_diff = min(min_diff, current_diff)

    return min_diff

def main():
# --- Unit Tests ---
    test_cases = [3, 1, 2, 4, 3]

    print(get_minimum_difference(test_cases))  # Expected output: 1


if __name__ == "__main__":
    main()