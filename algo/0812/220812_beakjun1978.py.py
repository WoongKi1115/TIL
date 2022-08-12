N = int(input())
X = list(map(int,input().split()))
def sosu(x):
    a = []
    for i in range(1,x+1):
        if x%i == 0:
            a.append(i)
    if len(a) == 2:
        return 'O'
count = 0
for i in range(N):
    if sosu(X[i]) == 'O':
        count += 1
print(count)