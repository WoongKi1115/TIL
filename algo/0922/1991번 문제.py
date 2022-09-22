def pre(n):
    if n != '.':
        print(n, end='')
        pre(tree[n][0])
        pre(tree[n][1])

def inorder(n):
    if n != '.':
        inorder(tree[n][0])
        print(n, end='')
        inorder(tree[n][1])

def post(n):
    if n != '.':
        post(tree[n][0])
        post(tree[n][1])
        print(n, end='')

tree = {}
N = int(input())
for i in range(N):
    root, left, right = map(str, input().split())
    tree[root]=left, right

pre('A')
print()
inorder('A')
print()
post('A')
