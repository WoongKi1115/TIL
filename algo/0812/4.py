def my_strcmp(a, b):
    l = 0
    if len(a) > len(b):
        l = len(b)
    else:
        l = len(a)
    for i in range(l):
        if ord(a[i]) > ord(b[i]):
            return 1
            break
        elif ord(a[i]) < ord(b[i]):
            return -1
            break
        else:
            continue
    if len(a) > len(b):
        return 1
    else:
        return -1


print(my_strcmp('Hellowood', 'Hellowo'))

