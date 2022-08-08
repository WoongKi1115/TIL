N = int(input())

for i in range(N):
    num = int(input())
    T = list(map(int,input().split()))
    counting = [0]*101
    max_score = [[0,0]]
    for j in range(len(T)):
            counting[T[j]] += 1
    for k in range(len(counting)):
        if counting[k]>= max_score[0][0]:
            max_score[0]=[counting[k], counting.index(counting[k])]
            print(max_score)
        else:
            continue
    
    # print(f"#{num} {max_score[0][1]}")

