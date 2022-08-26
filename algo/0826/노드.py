class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Node를 사용해서 트리 만들기
root = Node(1)  # root 노드 만들기

# 2,3 을 root 왼쪽, 오른쪽에 추가
root.left = Node(2)
root.right = Node(3)

# 4,5 를 2번의 왼쪽, 오른쪽에 추가
root.left.left = Node(4)  # Node(2).left
root.left.right = Node(5)  # Node(2).right


# 전위순회
def preorder(node):
    if node:
        print(node.data, end=' ')
        preorder(node.left)
        preorder(node.right)


# 중위순회
def inorder(node):
    if node:
        inorder(node.left)
        print(node.data, end=' ')
        inorder(node.right)


# 후위순회
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=' ')


preorder(root)
print()
inorder(root)
print()
postorder(root)

# 13
# 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
V = int(input())
tree = [Node(i) for i in range(V + 1)]
list1 = list(map(int, input().split()))
# 입력을 두개씩 갈라서 확인
# 앞 => 부모 p
# 뒤 => 자식 c
# while edge_list:
#     p = edge_list.pop(0)
#     c = edge_list.pop(0)
#     # 입력 처리(트리 만들기)
#     # 부모를 기준으로 왼쪽이 있는 경우
#     if tree[p].left:
#         tree[p].right = tree[c] # 부모의 오른쪽에 자식 추가
#     # 부모를 기준으로 왼쪽이 없는 경우
#     else:
#         tree[p].left = tree[c]  # 부모의 왼쪽에 자식 추가
# x = [0]*(V+1)
# for i in range(0,len(list1),2):
#     x[list1[i+1]] = list1[i]
# print(x)
for i in range(0, len(list1), 2):
    if tree[list1[i]].left == None:
        tree[list1[i]].left = tree[list1[i + 1]]
    else:
        tree[list1[i]].right = tree[list1[i + 1]]

preorder(tree[1])




