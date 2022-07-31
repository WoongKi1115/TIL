from faker import Faker

import random
import copy
class Pairprogramming:
    #1. 인자로 학생들의 이름으로 이루어진 리스트를 받아서 인스턴스 변수에 할당한다.
    def __init__(self, students):
        self.students = students
    
    def pick(self, n):
        result = set() #결과로 반환할 랜덤으로 뽑은 학생 세트 (중복을 막기 위해서)
        
        while len(result) < n: # 내가 뽑기 원하는 학생수가 될 때까지 계속 세트에 뽑아서 넣기.
            result.add(random.choice(self.students))

        return sorted(list(result))
    
    def match_pair(self):
        result = [] # 결과로 반환할 리스트
        #학생 리스트를 복사해서(깊은 복사)
        #짝을 지어준 학생은 리스트에서 제거.
        #그 다음에 다시 짝ㅇ르 지어줄 학생을 뽑아서 페어링
        #[1,2,3,4,5]
        #[1,2,3]
        #[4,5]
        

        if len(self.students) < 2:
            return None
        if len(self.students) % 2 == 1:
            random_pick = self.pick(3)
            for student in random_pick:
                self.students.remove(student)
            
            result.append(random_pick)
            #뽑은 세명은 짝짓기가 완료 되었으니까 리스트에서 제거해준다. (다음에 또 뽑지 않기 위해서)
            
            #나머지는 짝수니깐 페어링 진행
        while len(self.students) > 0:
            random_pick = self.pick(2)
            for student in random_pick:
                self.students.remove(student)
            result.append(random_pick) #뽑아온 2명을 리스트에 추가

        return result

students = []
fake = Faker('fr_FR')

for i in range(11):
    students.append(fake.name())

print(students)

pair1 = Pairprogramming(students)
print(pair1.students)

print(pair1.pick(5))
print(pair1.match_pair())