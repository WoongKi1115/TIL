a ={'a' : 1, 'b' : 2}
b = {1,2,3}
for i in a:
    print(a[i])

for i in b:
    print(i)

print()
members = ['민수', '영희', '철수']
for idx, number in enumerate(members):
    print(idx,number)

print(list(enumerate(members, start=1))) #인덱스 값이 1부터 시작. idx가 1부터 나옴
print()
# i 가 2일 때
for i in range(4):
    if i== 2:
        pass
    print(i)
"""
0
1
2
3
"""
print()
number = (1,2,3,4,5)
a,b,c,d,e = number
print(a,b,d,c,e)
print()
def print_family_name(*parents, **pets):
    print("아버지 :",parents[0])
    print("어머니 :",parents[1])
    if pets:
        print("반려동물들..")
        for species, name in pets.items():
            print(f'{species} : {name}')

print_family_name('아부지', '어무이', dog='멍멍이', cat='냥냥이')

print()
a = 0

b = 1

def enclosed():

    a = 10

    c = 3

    def local(c):

        print(a, b, c) #10 1 300

    local(300)

    print(a, b, c) #10 1 3

enclosed()

print(a, b) #0 1

print()

def func1():
    global z
    z = 3


func1()
print(z)

print()
x = 0
def func1():
    x = 1
    def func2():
        nonlocal x
        x = 2
    func1()
    print(x) # 2
func1()
print(x) #0