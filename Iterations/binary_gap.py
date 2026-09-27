

def solution(N : int) -> int:
    """
    Finds the maximum binary gap length for a given positive integer N.
    
    A binary gap is a sequence of consecutive zeros surrounded by ones 
    at both ends in the binary representation of N.
    """
    max_gap_length = 0
    current_gap_length = 0
    is_inside_gap = False

    quotient = N

    while quotient > 0:
        remainder = quotient % 2    

        if remainder == 1:
            if is_inside_gap:
                if current_gap_length > max_gap_length:
                    max_gap_length = current_gap_length

            # Mark that a '1' was encountered and reset current count for the next potential gap
            is_inside_gap = True
            current_gap_length = 0

        elif is_inside_gap:
            # Increment zero count only if we are bounded by a preceding '1'
            current_gap_length += 1
        # Integer division by 2 to process the next bit
        quotient = quotient // 2

    return max_gap_length

if __name__ == "__main__":
    test_number = int(input().strip())
    print(solution(test_number))
