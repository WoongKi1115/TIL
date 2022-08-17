T = 10
for tc in range(1,T+1):
    testcase = int(input())
    box = [list(input()) for _ in range(100)]
    result = 0
    for i in range(100):
        word_a = ''
        for j in range(100):
            word_a += box[i][j]
        count_a = 0
        for k in range(100):
            for l in range(100,-1,-1):
                if word_a[k:l] == word_a[k:l][::-1]:
                    if count_a < l-k:
                        count_a = l-k
        if count_a > result:
            result = count_a

    for n in range(100):
        word_b = ''
        for m in range(100):
            word_b += box[m][n]
        count_b = 0
        for o in range(100):
            for p in range(100,-1,-1):
                if word_b[o:p] == word_b[o:p][::-1]:
                    if count_b < p-o:
                        count_b = p-o
        if count_b > result:
            result = count_b
    print(f"#{tc} {result}")
