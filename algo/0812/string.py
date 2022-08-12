T = 10
def checklist(a, b):
    i = 0
    j = 0
    count = 0
    while i<x and j < y:
        if b[j] != a[i]:
            j = j-i
            i = -1
        i = i + 1
        j = j + 1
        if i == x:
            count += 1
            i = 0
    return count


for tc in range(1, T+1):
    test = int(input())
    a = input()
    b = input()
    x = len(a)
    y = len(b)
    print(checklist(a, b))
