def collatz(n):
    count = 0

    while n != 1 and count < 500:
        #홀수
        if n % 2 == 1:
            n = n*3 + 1
        else:
            n = n // 2
        count+=1
        #여기로 왔다면 n이 1이 됬거나 아니면 반복횟수가 500 이거나.
    
    if count == 500:
        count = -1
    
    return count

print(collatz(11111111111111111111))