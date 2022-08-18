T = int(input())
def paper(n):
    if n == 1:
        return 1
    elif n== 2:
        return 3
    else:
        return paper(n-1) + paper(n-2)*2
for tc in range(1, T+1):
    x = int(int(input())//10)
    print(f"#{tc} {paper(x)}")
