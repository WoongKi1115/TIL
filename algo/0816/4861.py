T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    box = [list(input()) for _ in range(N)]
    result = ''
    for i in range(N):
        for j in range(N - M + 1):
            word_a = ''
            for k in range(M):
                word_a += box[i][j + k]
            if word_a == word_a[::-1]:
                result = word_a
            else:
                word_a = ''
                continue

    for j in range(N):
        for i in range(N - M + 1):
            word_b = ''
            for k in range(M):
                word_b += box[i + k][j]
            if word_b == word_b[::-1]:
                result = word_b
            else:
                word_b = ''
                continue
    print(f"#{tc} {result}")
