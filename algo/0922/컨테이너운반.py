import sys
sys.stdin = open("input3.txt", "r")
T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    container = list(map(int, input().split()))
    truck = list(map(int,input().split()))
    container = sorted(container)
    truck = sorted(truck)
    result = 0
    for i in range(N-1, -1, -1):
        for j in range(M-1,-1,-1):
            if container[i] <= truck[j]:
                result += container[i]
                truck.pop(j)
                truck.append(0)
                break
            else:
                continue
    print(f"#{tc} {result}")