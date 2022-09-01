Model
장고의 디자인 패턴 MTV
어제까지는 TV만 사용
데이터를 저장하기 위해서는 Model이 필요.

database
기본 구조
스키마
테이블

스키마 : 데이터베이스의 뼈대
데이터 베이스의 자료구조, 표현 방법, 관계 등을 정의

테이블(액셀과 유사) : 필드와 레코드를 사용해 조직된 데이터 요소들의 집합
필드(열) : 속성, 컬럼
레코드(행) : 튜플, 행

Primary Key
기본 키
각 레코드의 고유한 값(식별자로 사용됨)
기술적으로 다른 항목과 절대로 중복될 수 없는 단일 값

Model을 통해 데이터에 접근하고 조작.
사용하는 데이터들의 필수적인 필드(컬럼)들과 동작(OOP,메서드)들을 포함
모델 쿨랴수 1개 == 데이터베이스 테이블 1개

모델과 데이터베이스는 다른 것.

1. view에서 model에 데이터 요청
2. model에서 database에 데이터 요청
3. database에서 model로, model에서 view로 데이터 전달

즉 model을 통해 데이터를 관리함.
class를 통해 스키마를 만드는 작업.

Migration(매우중요)
makemigrations
필수 명령어
python manage.py makemigrations

models.py에 만들어둔 스키마(설계도)를
migrations 폴더안에 0001nitial.py(최종설계도)로 바꾸어주는 과정
데이터 베이스에 보내기 전의 최종 설계도 (아직 데이터베이스에 보내지 않음)
mirations 폴더에 생성됨

python manage.py migrate
makemigrations로 만든 최종 설계도를 실제 데이터베이스에 반영하는 과정

migrate를 해야 데이터베이스와 model이 동기화가 됨.

기타 명령어
python manage.py showmigrations
[x] 는 있다는 의미.

python manage.py sqlmigrate articles 0001
migrations 폴더 안의 articles 0001이 sql 문으로 바뀌어져서 나옴.

이미 데이터베이스로 넘어간 models.py에 새로운 정보를 추가해서 업데이트하기

models.py에 새로 입력을 넣어줌.
시간과, 업데이트 시간을 적어주려고 함.
장고에서는 이미 존재하는 테이블에 새로운 컬럼을 추가해달라는 요구를 받은 것.
하지만 이 컬럼들은 기본적으로 빈 값으로 추가 안됨.
때문에 기본값을 설정해주어야 함.

auto_now_add vs auto_now 비교 문제 주의

orm
장고와 database의 언어들을 서로 번역해주는 기술
sql을 사용하지 않고 데이터베이스를 조작할 수 있게 해줌.

장점
sql을 잘 몰라도 객체지향 언어로 db조작 가능
객체 지향적 접근으로 인한 높은 생산성

단점
orm만으론 세밀한 데이터베이스 조작을 구현하기 어려움

pip install ipython
python -i
주피터 노트북같이 한줄 쓰면 바로 적용

pip install django-extensions
Django shell
기본 쉘이 안좋기 때문에
python manage.py shell_plus를 활용해서 더 괜찮은 버전 사용.
이거 사용하면 i python도 켜짐

shellplus를 쓰면 모든 모듈들이 자동으로 import됨.

Database API 구문
Article.objects.all()
Article : Model class
objects : manager
all : Queryset API

object manager
모델이 데이터베이스 쿼리작업을 가능하게 하는 인터페이스

query
원하는 데이터를 얻기 위해 데이터베이스에 요청을 보낼 코드를 작성

파이썬으로 작성한 orm에 의해 sql로 변환되어 데이터베이스에 전달.
데이터베이스의 응답데이터를 orm이 queryset이라는 자료 형태로 변환하여 우리에게 전달.

queryset
데이터베이스에게서 전달 받은 객체 목록
순회가 가능한 데이터. 1개 이상의 데이터를 불러와 사용할 수 있음.
orm을 통해 만들어진 자료형. 필터를 걸거나 정렬 수행 가능.

단 데이터베이스가 단일 객체 반환시 queryset이 아닌 모델의 인스턴스로 반환

queryset api 익히기
CRUD
create, read, update, delete

create 방법
1번 째 방법

1. article = Article()
   클래스를 통한 인스턴스 생성
2. article.title
   클래스 변수 명과 같은 이름의 인스턴스 변수를 생성 후 값을 할당.
3. article.save()
   인스턴스로 save 메서드 호출
   입력했던 정보들을 데이터베이스에 올려줌

2번째 방법
인스턴스 생ㅇ성ㅇ시 초기 값을 함께 작성하여 생성.
article = Article(title='second', content='django!')

3번째 방법
Queryset api중 create() 메서드 사용

read
1번 째 방법
all()
전체 데이터를 조회. (전체 쿼리셋 반환)
Article.objects.all()

get()
단일 데이터 조회(유니크한 값만 조회. PK조회할 때 사용)
객체를 찾을 수 없으면 에러
둘 이상의 객체를 찾을 때도 에러 발생.

filter()
지정된 조회 매개변수와 일치하는 객체를 포함하는 새 queryset반환
존재하지 않아도 빈 쿼리셋을 반환.
get은 그냥 객체를 반환, filter은 쿼리셋을 제공.
때문에 pk값을 반환하는데 적합하지 않음.
pk는 get으로 조회하는게 나음.

field lookups
특정 레코드에 대한 조건을 설정하는 방법.
Article.objects.filter(content\_\_ccontains='ja')

update
선 조회 후 변경 후 save()
수정하기 전에 수정하고자 하는 부분 get으로 가져옴.
article = Article.objects.get(pk=1)
article.title = 'byebye'
article.save()

delete
선 조회 후 삭제
article = Article.objects.get(pk=1)
article.delete()

삭제된 부분의 pk는 재사용하지 않고
그 다음 번호로 들어감.

반환시킬 때 쿼리에 제목으로 들어간 부분을 원할 때
**str** 을 사용하면 이름으로 나오게 만듬.
db에 아무련 영향을 끼치지 않으므로 변화했어도 makemigrations 안해도 됨.
models.py에

create 구현 위해서는 2개의 함수 필요
글을 작성할 페이지 리턴
'new' view function
데이터를 받아서 db에 처리하는 함수

가상환경 설정
python -m venv ./venv

source venv/Scripts/activate

requirement.txt 설치
pip install -r requirement.txt
