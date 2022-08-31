from django.db import models

# Create your models here.
# 이 작업은 스키마 작업.
# table을 만들기 전에 설계도를 만드는 작업임.
# title과 content의 테이블을 만드는 작업.
# table의 필수인 기본키는 장고에서 자동으로 만들어줌

class Article(models.Model):
    
    # 클래스 변수가 하나의 필드가 되고, 어떤 타입으로 되어있는지를 작성하는 것. 게시판의 제목이므로 str타입임.
    # title => 필드 이름, model.CarField => 모델 타입
    # CharField 는 max_length가 필수. 길이를 조절할 수 있음.
    # CharField와 TextField는 길이 제한 유무의 차이
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    # db에 아무련 영향을 끼치지 않으므로 변화했어도 makemigrations 안해도 됨.