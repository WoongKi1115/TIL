def Trees(n):
    global tree
    global x
    if n <= N:
        Trees(n * 2)
        tree[n] = x
        x += 1
        Trees(n * 2 + 1)



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0]*(N+1)
    x = 1
    Trees(1)
    result1 = tree[1]
    result2 = tree[N//2]
    print(f"#{tc} {result1} {result2}")
