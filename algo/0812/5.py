def itoa(a):
    i = 10
    s = ""
    while a>0:
        mod = a%i
        s += chr(ord('0') + mod)
        a //= 10
    return s[::-1]

a = 1234
b= itoa(a)
print(b)