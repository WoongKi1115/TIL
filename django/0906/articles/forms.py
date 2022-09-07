from django import forms
from .models import Article


# class ArticleForm(forms.Form):
#     NATION_A = 'kr'
#     NATION_B = 'ch'
#     NATION_C = 'jp'
#     NATIONS_CHOICES = [
#         (NATION_A, '한국'),
#         (NATION_B, '중국'),
#         (NATION_C, '일본'),
#     ]

#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)
#     nation = forms.ChoiceField(choices=NATIONS_CHOICES)
    # nation = forms.ChoiceField(choices=NATIONS_CHOICES, widget=forms.RadioSelect)


class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'my-title form-control',    # 넣고싶은 속성들을 이 딕셔너리 안에 써줌.
                'placeholder': 'Enter the title',    # 빈 칸에 안내문구 넣어줌. (입력시 사라짐)
                'maxlength': 10,        # 위젯은 유효성 검사에 적용되지 않음. 이건 입력할 때 10자까지만 입력하게끔 이미 제한을 걸어버림. 위젯은 인풋 테그의 표현에만 관여할 뿐임.
            }
        )
    )

    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'my-content form-control',
                'placeholder': 'Enter the content',
                'rows': 5,
                'cols': 50,
            }
        ),
        error_messages={
            'required': '내용 입력하라고..',   # 에러 발생시 나타내고 싶은 메세지 입력하면 나옴
        }
    )

    class Meta:
        model = Article
        fields = '__all__'
        # exclude = ('title',)
