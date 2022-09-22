import sys
sys.stdin = open("input4.txt", "r")
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    visited = [0]*25
    result = 0
    times = [list(map(int,input().split())) for _ in range(N)]
    times.sort(key= lambda x:x[1])
    print(times)
    Flag = False
    for i in range(N):
        answer = 0
        for j in range(times[i][0], times[i][1]):
            if visited[j] != 0:
                answer = 0
                break
            else:
                visited[j] = 1
                answer = 1
        result += answer
    print(f"#{tc} {result}")