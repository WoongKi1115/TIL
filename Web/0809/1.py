import sys
x = []
for i in range(28):
    a = int(sys.stdin.readline())
    x.append(a)

y= []
for i in range(1,30):
    if i not in x:
        y.append(i)

y.sort()
for i in range(2):
    print(y[i])