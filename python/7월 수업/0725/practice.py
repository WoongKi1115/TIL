a = [1,2,3]
b = a[:]
print(a,b) # [1, 2, 3] [1, 2, 3]
print(id(a))
print(id(b))
b[0] = 5 
print(a,b) # [1, 2, 3] [5, 2, 3]