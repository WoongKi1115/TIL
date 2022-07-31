word = 'ssafy'
print(word)
print(id(word)) # 메모리 주소 확인
word = 'test'
print(word)
print(id(word)) #메모리 주소 확인

print('apple'.find('p'))
print('Title Title'.istitle())
print('@'.isalpha())
print('a,b,c'.split(','))

cafe = ['starbucks', 'tomntoms', 'hollys']
print(cafe, id(cafe))
cafe.append('banapresso')
print(cafe, id(cafe))
cafe = ['starbucks', 'tomntoms', 'hollys']
print(cafe)
cafe.insert(0,'start')
print(cafe)
cafe.insert(len(cafe), 'end')
print(cafe)
cafe.insert(100000, 'end')
print(cafe)


cafe = ['starbucks', 'tomntoms', 'hollys']
