matrix = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]
matrix[0]
matrix[1]

matrix[1][1]
matrix[2][2]

mow = [0, 0]
for x in rnage(3):
    for y in range(3):
        if matrix[x][y]== 1:
            now[0] = x
            now[1] = y
print(f"현재 위치 : {now[0]}행, {nwo[1]}열")

def a(x):
    b = 0
    for a in x:
        b += a
    return b
        