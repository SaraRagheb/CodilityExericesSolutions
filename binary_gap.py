# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # Implement your solution here
    counting = False
    max_count = 0
    curr_count = 0
    div =  N 
    while div > 0:
        rem = div % 2
        if rem == 1:
            if counting:
                if curr_count > max_count:
                    max_count = curr_count    
            counting = True
            curr_count = 0  
        elif counting:
            curr_count += 1  
        div = div // 2

    return max_count
    pass


if __name__ == "__main__":
    N = int(input().strip())
    print(solution(N))
