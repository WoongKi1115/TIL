n = 20
q = []
p = 1
m = 0
v = 0
while n > m:
    q.insert(0, (p, 1, m))
    v, c, my = q.pop(-1)
    m += 1
    q.insert(0,(v,c+1,my + c))
    p += 1
print(v)