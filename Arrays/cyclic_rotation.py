
from typing import List


def solution(A: List[int], K: int) -> List[int]:
    """Rotates an array A to the right by K steps.

    Parameters:
        A (List[int]): The array of integers to be rotated.
        K (int): The number of positions to shift right.

    Returns:
        List[int]: The shifted array.
    """
    if not A:
        return []

    # Handle shifts larger than array length
    K %= len(A)

    # Perform circular rotation using array slicing
    return A[-K:] + A[:-K]


if __name__ == "__main__":
    # Quick sanity checks
    print(solution([3, 8, 9, 7, 6], 3))  # Output: [9, 7, 6, 3, 8]
    print(solution([0, 0, 0], 1))        # Output: [0, 0, 0]
    print(solution([1, 2, 3, 4], 4))     # Output: [1, 2, 3, 4]
    print(solution([], 5))               # Output: []