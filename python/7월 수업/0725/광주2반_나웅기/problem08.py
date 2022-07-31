#게임상 아이템 인벤토리에 저장. 인벤토리는 리스트 
# 함수(x=type, y=인벤토리 정보)
item_type='weapon'
inventory=[
{'id': 1, 'name': 'Elder Wand', 'type': 'weapon', 'grade': 'legend'},
{'id': 2, 'name': 'Healing Potion', 'type': 'potion', 'grade': 'normal'},
{'id': 3, 'name': 'Steel Helmet', 'type': 'armor', 'grade':'rare'},
{'id': 4, 'name': 'Long Sword', 'type': 'weapon', 'grade': 'normal'},
]


def found(x,y):
    a = []        #비어있는 리스트 생성
    for i in range(len(y)): # 인벤토리의 리스트 
        if x == y[i]['type']:   #x의 값과 인벤토리 type이 같다면
            a.append(y[i])     #a에 해당 딕셔너리르 추가.
    return a                   #a 출력

print(found('weapon',inventory))
