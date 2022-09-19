num = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']
def find_code(x):
    result = []
    for i in range(56,7):
        a = x[i:i+7]
        print(a)
        for j in range(10):
            if num[i] == a:
                result.append(i)
    return result