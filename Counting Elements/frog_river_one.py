"""FrogRiverOne Solution.

Finds the earliest time when a frog can jump to the other side of a river 
of width X, given leaves falling at position A[K] at time K.

Codility Complexity: O(N) Time | O(X) Space.
"""

from typing import List


def get_earliest_time(X: int, A: List[int]) -> int:
    """Finds the earliest second at which leaves cover all positions from 1 to X.

    Args:
        X (int): Target river position / required distance (1 to X).
        A (List[int]): Array where A[K] represents the position where a leaf falls at time K.

    Returns:
        int: The earliest second (index) when all positions from 1 to X are covered, 
             or -1 if the frog can never cross.
    """
    if not A or X <= 0:
        return -1

    covered_positions = set()

    for second, position in enumerate(A):
        # Only track positions within the required river width
        if position <= X:
            covered_positions.add(position)

            # Check if all required positions from 1 to X have leaves
            if len(covered_positions) == X:
                return second

    return -1

def main():
    # Example usage
    X = 5
    A = [1, 3, 1, 4, 2, 3, 5, 4]
    print(get_earliest_time(X, A))  # Expected output: 6

if __name__ == "__main__":
    main()