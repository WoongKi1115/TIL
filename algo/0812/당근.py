T = int(input())
N = int(input())
C = list(map(int, input().split()))

for tc in range(1,T+1):
    x = 0
    count = 0
    for i in range(N-1):
        if C[i] + 1 == C[i+1]:
            count += 1
        else:
            count = 0

    print(f"#{tc} {count}")