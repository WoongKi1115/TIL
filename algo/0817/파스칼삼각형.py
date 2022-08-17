T = int(input())
def triangle(N):
    a = [1] * N
    if N >= 3:
        for i in range(1,N-1):
            a[i] += N-2
    for i in range(N):
        print(a[i], end = ' ')
    return ''



for tc in range(1,T+1):
    N = int(input())
    for i in range(1,N+1):
        print(triangle(i))
