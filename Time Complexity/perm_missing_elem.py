"""PermMissingElem Solution.

Finds the missing element in a given permutation of integers from 1 to N + 1.
Codility Complexity: O(N) Time | O(1) Space.
"""

from typing import List


def get_missing_element(A: List[int]) -> int:
    """Calculates the missing integer in an array containing elements from 1 to N + 1.

    Uses Gauss's summation formula to compute the expected sum and subtracts 
    the actual sum of elements in constant space.

    Args:
        A (List[int]): An array of N distinct integers in the range [1..N + 1].

    Returns:
        int: The single missing integer.
    """
    n = len(A)
    
    # Expected sum of integers from 1 to (N + 1) using Gauss's formula
    expected_sum = (n + 1) * (n + 2) // 2
    actual_sum = sum(A)

    return expected_sum - actual_sum


# --- Unit Tests ---
def main():
    test_cases = [2, 3, 1, 5] 
    print(get_missing_element(test_cases))                
       
if __name__ == "__main__":
    main()