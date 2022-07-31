class Car:
    tire = 4  # 클래스 변수

    def __init__(self,name):  #self => 인스턴스 자기 자신을 뜻하는 파라미터
        #__init__ : 클래스를 통해 인스턴스를 만들 때 무조건 실행되는 메소드
        self.name = name #인스턴스 변수 생성
        
        
car1 = Car('아반떼')
car2 = Car('소나타')
car3 = Car('그랜져')
 
print(car1.tire)
print(car2.tire)
print(car3.tire)
print('-----')
print(car1.name)
print(car2.name)
print(car3.name)