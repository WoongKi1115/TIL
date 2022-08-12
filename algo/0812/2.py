def my_reverse(x):
    y = ''
    a = -1
    for i in range(len(x)):
        y += x[a]
        a -= 1
    return y

def my_reverse2(X):
    x = list(X)
    y = ''
    for i in range(len(x)//2):
        x[i], x[len(x)-1-i] = x[len(x)-1-i], x[i]

    for j in range(len(x)):
        y += x[j]
    return y


print(my_reverse('tab tokk ir ag ead'))
print(my_reverse2('string'))