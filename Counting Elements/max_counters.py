"""MaxCounters Solution.

Calculates the final values of N counters after applying M operations 
(increment or max_counter) represented by array A.

Codility Complexity: O(N + M) Time | O(N) Space.
"""

from typing import List


def get_max_counters(N: int, A: List[int]) -> List[int]:
    """Applies increment and max_counter operations to N counters.

    Args:
        N (int): Number of counters.
        A (List[int]): Non-empty array of M integers representing operations.

    Returns:
        List[int]: Values of all N counters after performing all operations.
    """
    counters = [0] * N
    current_max = 0
    last_max_counter = 0

    for op in A:
        if 1 <= op <= N:
            idx = op - 1
            # Lazy update: catch up counter if it missed a prior max_counter operation
            if counters[idx] < last_max_counter:
                counters[idx] = last_max_counter

            counters[idx] += 1
            current_max = max(current_max, counters[idx])
        elif op == N + 1:
            # Set threshold instead of re-allocating or re-filling array
            last_max_counter = current_max

    # Final pass to apply lazy updates to any counters that were not updated
    for i in range(N):
        if counters[i] < last_max_counter:
            counters[i] = last_max_counter

    return counters


def main():
    # Example usage
    N = 5
    A = [3, 4, 4, 6, 1, 4, 4]
    print(get_max_counters(N, A))  # Expected output: [3, 2, 2, 4, 2]

if __name__ == "__main__":
    main()