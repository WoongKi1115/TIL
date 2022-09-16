def search(n):
    answer = -1
    for i in range(1, n):
        a = i**3
        if a > n:
            break
        if a == n:
            answer = i
    return answer


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print(f"#{tc} {search(N)}")

