사용자가 항상 정상적인 요청을 하진 않음. 
때문에 사용자가 입력한 데이터가 유효한지에 대해 체크 필요
유효성 검사를 단순화, 자동화 할 수 있게 하기 위해 장고에서는 form을 활용

form도 model과 동일하게 상속을 통해 받음.

form에서는 textfield가 없음. => charfield를 사용해줘야함.

html에서 label, input 이런 것 없이 forms.py를 만들고 여기에 형식을 만들어주어
html에 {{form}}을 하게 되면 그 형식이 불러와짐

as_p를 활용하면 form 형식 각각을 p로 묶어서 랜더링해줌

형식의 포멧을 바꿀땐 위젯 활용(출력부분 담당)

이제부터는 사용자에게 입력 받는 형식을 form 클래스에서 해주어야 함.(label, input사용 하면 안됨)

model과 form의 형식이 매우 유사
때문에 둘이 같을 때는 form 대신에 modelform을 사용하면 됨
둘이 다르다면 form처럼 따로 써주면 됨.

class ArticleForm(forms.ModelForm):
    model = Article
    fields = '__all__'   <= 모델의 form 모두를 가져오겠다는 의미



이전에까지는 create나 update에서는 받아온 것을 매번 1개씩 적어주었어야함.
하지만 이제는 form.ArticleForm(request.POST)로 한번에 받아오면 됨.
더 편한 방법


if를 활용해 잘못된 경우 다시 쓰게끔 돌려보낼 수 있음.
if form.is_valid():  is_valid는 유효성 검사해주는 함수. 유효하다면 True를 출력
    form.save()

save()는 저장할 것을 출력해줌.
때문에 save()를 따로 변수에 지정해주고
그에 대한 pk같은 정보들을 출력시킬 수 있음

수정을 하기 위해선 instance = article의 형태로 form에 적어주면 
장고가 알아서 수정을 위한 자료구나라고 판단해 처리