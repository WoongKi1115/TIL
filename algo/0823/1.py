visited = [[1, 2, 3], [1, 2, 3, 4, 5, 6, 7]]
ask = 'helo'
def hi(a):
    global ask
    visited[0][1] = a
    ask = a

hi(15)
print(visited)
print(ask)