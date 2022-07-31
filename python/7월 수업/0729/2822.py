a = []
for i in enumerate(range(8), start = 1):
    x = int(input())
    a.append(x)
 
b = sorted(a,reverse=True)[0:5]
c = []
for i in b:
    for j in range(len(a)):
        if i==a[j]:
            c.append(j)

d= sorted(c)
print(sum(b))
for i in d:
    print(i+1, end = ' ')
