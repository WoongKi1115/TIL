T = 1
for tc in range(1,T+1):
    num = int(input())
    box = list(map(int,input().split()))
    counting = [0]*101                  #box의 같은 층끼리 몇개가 있는지 찾음.
    for i in box:
        counting[i] += 1
    
    max = 0
    min = 101
    for i in box:
        if i < min:
            min = i
        if i > max:
            max = i

    count = 0
    while count < num:         # max 부분을 min으로 보내주고 해당 값을 1 줄여주고 아래 값에 1을 더해줌.
        counting[max] -= 1      # min은 위와 반대로 값이 더해졌을테니 올라감.
        counting[max-1] += 1
        counting[min] -= 1
        counting[min+1] += 1

        if counting[max] == 0:     # max인 부분이 0이되면 max에 1을 빼줘서 그 다음 값에서 빼게끔 만듬.
            max -= 1
        if counting[min] == 0:
            min += 1
        
        count += 1
    print(f"#{tc} {max-min}")