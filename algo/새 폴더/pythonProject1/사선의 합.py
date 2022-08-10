N = int(input())
x = [list(map(int, input().split())) for _ in range(N)]
s = [0]*(2*N-1)

for i in range(N):
    for j in range(N):
        s[i+j] += x[i][j]
print(s)