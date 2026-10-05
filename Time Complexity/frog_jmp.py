
"""FrogJmp Solution.

Calculates the minimum number of jumps required to reach or exceed a target position.
Codility Complexity: O(1) Time | O(1) Space.
"""


def minum_num_jumps(X: int, Y: int, D: int) -> int:
    """Calculates the minimum number of jumps from start to target.

    Args:
        X (int): Starting position.
        Y (int): Target position.
        D (int): Jump distance.

    Returns:
        int: Minimum number of jumps required.

    Raises:
        ValueError: If step size (D) is less than or equal to 0, or if target < start.
    """
    if D <= 0:
        raise ValueError("Jump distance (D) must be greater than zero.")
    if Y < X:
        return 0

    # Ceiling division using integer arithmetic: ceil((Y - X) / D)
    distance = Y - X
    return (distance + D - 1) // D


def main ():

    print(minum_num_jumps(10, 85, 30))

    

if __name__ == "__main__":
    main()
