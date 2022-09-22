import sys
sys.stdin = open("input2.txt", "r")
def Min_sum(sumnum,visited,i):
    if 0 not in visited[2:]:
        sumnum += box[i][0]
        result.append(sumnum)
    else:
        for x in range(1,N):
            if x==i:
                continue
            elif visited[x+1] == 0:
                sumnum += box[i][x]
                visited[x+1] = 1
                # print(sumnum)
                # print(visited)
                Min_sum(sumnum, visited,x)
                sumnum -= box[i][x]
                visited[x+1] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    box = [list(map(int, input().split())) for _ in range(N)]
    visited = [0]*(N+1)
    result = []
    Min_sum(0,visited,0)
    print(f"#{tc} {min(result)}")